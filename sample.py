import sys
import xml.dom.minidom
import os
import random
import datetime

run_date = "20200410"

filter_categories = ['800-8400','800-8300','800-8200','800-8000','700-7851','700-7850','700-7600','700-7450','700-7300','700-7000','600-6950','600-6900','600-6800','600-6700','600-6600','600-6500','600-6400','600-6300','600-6200','600-6100','600-6000','550-5520','500-5100','500-5000','300-3200','300-3100','300-3000','200-2300','200-2200','200-2100','200-2000','100-1100','100-1000']

country_sample_numbers = [
    {'country':'TUR', 'counts': [13,13,33,33,33]},
    {'country':'POL', 'counts': [5,5,10,10,10]},
    {'country':'RUS', 'counts': [3,3,8,8,8]},
    {'country':'ROU', 'counts': [2,2,7,7,7]},
    {'country':'GRC', 'counts': [2,2,5,5,6]},
    {'country':'CZE', 'counts': [1,2,4,4,4]},
    {'country':'HUN', 'counts': [1,2,4,4,4]},
    {'country':'HRV', 'counts': [1,1,2,3,3]},
    {'country':'BGR', 'counts': [1,1,2,3,3]},
    {'country':'SVK', 'counts': [1,1,1,1,1]},
    {'country':'KAZ', 'counts': [1,1,1,1,1]}
]

def main(country, region):
    randomed_list = do_sample(country)
    csv_list = create_csv_list(country, randomed_list)
    save_csv_list(csv_list, country, region)

def do_sample(country):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(os.path.join(dir_path, 'xml', country))
    number_of_files = len(files)
    slice_number = int((120000/number_of_files)*1.25)
    randomed_list = []
    for file in files:
        print('reading file: '+file)
        base_path = os.path.join(dir_path, 'xml', country)
        content = open(os.path.join(base_path,file), 'r')
        tempList = []
        for line in content:
            if len(line)>1000:
                tempList.append(file+line)
        if number_of_files == 1:
            return tempList
        random.shuffle(tempList)
        sl = slice_number
        if sl>len(tempList):
            sl = len(tempList)
        randomed_list = randomed_list + tempList[:sl]
    return randomed_list     

def create_csv_list(country, randomed_list):
    random.shuffle(randomed_list)
    print("sampling: "+country)
    csv_list = []
    for i in range(0,3):
        givenCountry = [x for x in country_sample_numbers if x['country']==country][0]
        current_counts = {
            'r1': givenCountry['counts'][0],
            'r2': givenCountry['counts'][1],
            'r3': givenCountry['counts'][2],
            'r4': givenCountry['counts'][3],
            'r5': givenCountry['counts'][4]
        }
        csv_list.append(
            "place_id,name,phone,house_number,street_basename,street_type,city,state,country,postal,nt_cat_id,nt_cat_name,pd_cat_id,pd_cat_name,lat,lon,isplace,isopen,isname,isaddr,isphone,reality_score,full_house_number,district,from_file"
        )
        for item in randomed_list:
            doc = xml.dom.minidom.parseString(item[11:])
            placeid = ""
            name = ""
            phone = ""
            house_number = ""
            street_basename = ""
            street_type = ""
            city = ""
            state = ""
            postal = ""
            lcms_category_id = ""
            lcms_category_name = ""
            poi_category_id = ""
            poi_category_name = ""
            lat = ""
            lon = ""
            isplace = "-0.1"
            isopen = "-0.1"
            isname = "-0.1"
            isaddr = "-0.1"
            isphone = "-0.1"
            reality_score = ""
            full_house_number = "NULL"
            district = ""

            # category lcms ---------------------------------------------
            categories = doc.getElementsByTagName('Category')
            for category in categories:
                if category.hasAttribute('primaryFlag') and category.getAttribute('primaryFlag') == "true" and category.getAttribute('categorySystem') == "navteq-lcms":
                    categoryIdNode = category.getElementsByTagName('CategoryId')
                    if categoryIdNode:
                        lcms_category_id = categoryIdNode[0].firstChild.data
                    categoryNameNode = category.getElementsByTagName('Text')
                    if categoryNameNode:
                        lcms_category_name = categoryNameNode[0].firstChild.data
                    break
            
            # Qyality scoring ----------------------------------------
            attributes = doc.getElementsByTagName('Attribute')
            for attr in attributes:
                if attr.hasAttribute('key') and attr.getAttribute('key') == "isPlace":
                    isplace = attr.firstChild.data
                if attr.hasAttribute('key') and attr.getAttribute('key') == "isOpen":
                    isopen = attr.firstChild.data
                if attr.hasAttribute('key') and attr.getAttribute('key') == "isNameCorrect":
                    isname = attr.firstChild.data
                if attr.hasAttribute('key') and attr.getAttribute('key') == "isAddressCorrect":
                    isaddr = attr.firstChild.data
                if attr.hasAttribute('key') and attr.getAttribute('key') == "isPhoneCorrect":
                    isphone = attr.firstChild.data
                if attr.hasAttribute('key') and attr.getAttribute('key') == "reality_score":
                    reality_score = attr.firstChild.data

            if not lcms_category_id[:8] in filter_categories:
                continue
            if check_counts(current_counts, float(reality_score)) == False:
                continue
            # place id --------------------------------------------------
            placeIdNode = doc.getElementsByTagName('PlaceId')
            if placeIdNode:
                placeid = placeIdNode[0].firstChild.data
            # name --------------------------------------------------------
            names = doc.getElementsByTagName('Name')
            for n in names:
                if n.hasAttribute('primaryFlag') and n.getAttribute('primaryFlag') == "true":
                    baseTextNodes = n.getElementsByTagName("BaseText")
                    for baseText in baseTextNodes:
                        name = baseTextNodes[0].firstChild.data
                        break
            # phone -------------------------------------------------------
            contacts = doc.getElementsByTagName("Contact")
            for contact in contacts:
                if contact.hasAttribute('type') and contact.getAttribute('type') == "PHONE":
                    phone = contact.getElementsByTagName('ContactString')[0].firstChild.data
                    break

            # house number ------------------------------------------------
            houseNumberNode = doc.getElementsByTagName('HouseNumber')
            if houseNumberNode:
                house_number = houseNumberNode[0].firstChild.data

            # street base name --------------------------------------------------
            streetNameNode = doc.getElementsByTagName('StreetName')
            if streetNameNode:
                street_basenameNode = streetNameNode[0].getElementsByTagName('BaseName')
                if street_basenameNode:
                    street_basename = street_basenameNode[0].firstChild.data
                street_typeNode = street_basenameNode[0].getElementsByTagName('StreetType')
                if street_typeNode:
                    street_type = street_typeNode[0].firstChild.data
            # city ----------------------------------------------------------------
            level4 = doc.getElementsByTagName('Level4')
            if level4:
                city = level4[0].firstChild.data
            # state ------------------------------------------------------------------
            level2 = doc.getElementsByTagName('Level2')
            if level2:
                state = level2[0].firstChild.data
            # postal -----------------------------------------------------------------
            postalNode = doc.getElementsByTagName('PostalCode')
            if postalNode:
                postal = postalNode[0].firstChild.data

            # category poi ---------------------------------------------
            categories = doc.getElementsByTagName('Category')
            for category in categories:
                if category.getAttribute('categorySystem') == "navteq-poi":
                    categoryIdNode = category.getElementsByTagName('CategoryId')
                    if categoryIdNode:
                        poi_category_id = categoryIdNode[0].firstChild.data
                    categoryNameNode = category.getElementsByTagName('Text')
                    if categoryNameNode:
                        poi_category_name = categoryNameNode[0].firstChild.data
                    break
            # coordinates ---------------------------------------------------
            geoPositoins = doc.getElementsByTagName('GeoPosition')
            for geoPosition in geoPositoins:
                if geoPosition.hasAttribute('type') and geoPosition.getAttribute('type') == "ROUTING":
                    latNode = geoPosition.getElementsByTagName('Latitude')
                    if latNode:
                        lat = latNode[0].firstChild.data
                    lonNode = geoPosition.getElementsByTagName('Longitude')
                    if lonNode:
                        lon = lonNode[0].firstChild.data
                    break
            # full house number ----------------------------------------------
            additionalDataNodes = doc.getElementsByTagName('AdditionalData')
            for additData in additionalDataNodes:
                if additData.hasAttribute('key') and additData.getAttribute('key') == "FullHouseNumber":
                    full_house_number = additData.firstChild.data

            print(item[:11])
            csv_list.append(
                placeid
                +","+name
                +","+phone
                +","+house_number
                +","+street_basename
                +","+street_type
                +","+city
                +","+state
                +","+country
                +","+postal
                +","+country
                +","+poi_category_id
                +","+poi_category_name
                +","+lcms_category_id+"|"+lcms_category_name
                +","+lat
                +","+lon
                +","+isplace
                +","+isopen
                +","+isname
                +","+isaddr
                +","+isphone
                +","+reality_score
                +","+full_house_number
                +","+district
                +","+item[:11]
            )

            if check_counts_finished(current_counts):
                break
        if check_counts_finished(current_counts):
            break

    return csv_list

def check_counts(current_counts, score):
    if score < 0.21:
        if current_counts['r1']>0:
            current_counts['r1'] = current_counts['r1'] - 1
            return True
        else:
            return False
    if score >= 0.21 and score < 0.28:
        if current_counts['r2']>0:
            current_counts['r2'] = current_counts['r2'] - 1
            return True
        else:
            return False
    if score >= 0.28 and score < 0.55:
        if current_counts['r3']>0:
            current_counts['r3'] = current_counts['r3'] - 1
            return True
        else:
            return False
    if score >= 0.55 and score < 0.8:
        if current_counts['r4']>0:
            current_counts['r4'] = current_counts['r4'] - 1
            return True
        else:
            return False
    if score >= 0.8:
        if current_counts['r5']>0:
            current_counts['r5'] = current_counts['r5'] - 1
            return True
        else:
            return False

def check_counts_finished(current_counts):
    c1 = current_counts['r1']
    c2 = current_counts['r2']
    c3 = current_counts['r3']
    c4 = current_counts['r4']
    c5 = current_counts['r5']
    if c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0 and c5 == 0:
        return True
    return False

def save_csv_list(csv_list, country, region):
    file_name = region+"_"+country+"_"+run_date+".csv"
    fo = open (file_name, 'w')
    for line in csv_list:
        fo.write(line.encode('utf8')+"\t\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
