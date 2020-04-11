import sys
import xml.dom.minidom
import os
import random
import datetime
# import requests

filter_categories = ['800-8400','800-8300','800-8200','800-8000','700-7851','700-7850','700-7600','700-7450','700-7300','700-7000','600-6950','600-6900','600-6800','600-6700','600-6600','600-6500','600-6400','600-6300','600-6200','600-6100','600-6000','550-5520','500-5100','500-5000','300-3200','300-3100','300-3000','200-2300','200-2200','200-2100','200-2000','100-1100','100-1000']

country_sample_numbers = [
    # EEU
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
    {'country':'KAZ', 'counts': [1,1,1,1,1]},
    # WEU
    {'country':'NLD', 'counts': [2,2,7,7,7]},
    {'country':'SWE', 'counts': [2,2,7,7,7]},
    {'country':'BEL', 'counts': [1,1,4,4,5]},
    {'country':'PRT', 'counts': [1,1,4,4,5]},
    {'country':'AUT', 'counts': [1,1,2,3,3]},
    {'country':'DNK', 'counts': [1,1,2,3,3]},
    {'country':'NOR', 'counts': [1,1,2,3,3]},
    {'country':'FIN', 'counts': [1,1,2,3,3]},
    {'country':'CHE', 'counts': [1,1,2,3,3]},
    {'country':'IRL', 'counts': [1,1,1,1,1]},
    {'country':'LUX', 'counts': [1,1,1,1,1]},
    {'country':'MLT', 'counts': [1,1,1,1,1]},
    {'country':'ISL', 'counts': [1,1,1,1,1]},
    # APAC
    {'country':'THA', 'counts': [4,10,10,12,12]},
    {'country':'IDN', 'counts': [4,4,9,9,9]},
    {'country':'VNM', 'counts': [2,2,2,7,7]},
    {'country':'MYS', 'counts': [1,2,4,4,4]},
    {'country':'PHL', 'counts': [1,1,2,3,3]},
    {'country':'TWN', 'counts': [1,1,2,3,3]},
    {'country':'SGP', 'counts': [1,1,2,3,3]},
    {'country':'HKG', 'counts': [1,1,1,1,1]},
    {'country':'IND', 'counts': [15,15,35,35,35]},
    {'country':'BGD', 'counts': [1,1,1,1,1]},
    {'country':'NPL', 'counts': [1,1,1,1,1]},
    {'country':'LKA', 'counts': [1,1,1,1,1]},
    # NA
    {'country':'CAN', 'counts': [12,12,32,32,32]},
    {'country':'BHS', 'counts': [2,2,2,2,2]},
    {'country':'CYM', 'counts': [1,1,1,1,1]},
    {'country':'JAM', 'counts': [2,2,2,2,2]},
    {'country':'VGB', 'counts': [1,1,1,1,1]},
    # LAM
    {'country':'BRA', 'counts': [7,8,20,20,20]},
    
    {'country':'MEX', 'counts': [3,3,8,8,8]},
    {'country':'ARG', 'counts': [2,2,2,2,2]},
    {'country':'COL', 'counts': [1,1,1,1,1]},
    {'country':'CHL', 'counts': [1,1,1,1,1]},
    {'country':'PER', 'counts': [1,1,1,1,1]},
    {'country':'ECU', 'counts': [1,1,1,1,1]},
    {'country':'PRY', 'counts': [1,1,1,1,1]},
    {'country':'PAN', 'counts': [1,1,1,1,1]},
    {'country':'VEN', 'counts': [1,1,1,1,1]},
    # BIG 7
    {'country':'AUS', 'counts': [15,15,40,40,40]},
    {'country':'DEU', 'counts': [15,15,40,40,40]},
    {'country':'ESP', 'counts': [15,15,40,40,40]},
    {'country':'GBR', 'counts': [15,15,20,20,20]},
    {'country':'ITA', 'counts': [15,15,40,40,40]},
    {'country':'FRA', 'counts': [15,15,40,40,40]},
    {'country':'USA', 'counts': [15,15,40,40,40]},
]

def main(country, region, kick_off_date):
    randomed_list = read_samples(country)  
    csv_list = create_csv_list(country, region, randomed_list)
    save_csv_list(csv_list, country, region, kick_off_date)
  
def read_samples(country):
    randomed_list = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fw = open (os.path.join(dir_path, "xml", country+"_tmp.csv"), 'rb')
    for line in fw:
        randomed_list.append(line)
    fw.close()
    os.remove(os.path.join(dir_path, "xml", country+"tmp.csv"))
    return randomed_list

def create_csv_list(country, region, randomed_list):
    print("sampling: "+country)
    csv_list = []
    for i in range(0,3):
        random.shuffle(randomed_list)
        csv_list = []
        givenCountry = [x for x in country_sample_numbers if x['country']==country][0]
        current_counts = {
            'r1': givenCountry['counts'][0],
            'r2': givenCountry['counts'][1],
            'r3': givenCountry['counts'][2],
            'r4': givenCountry['counts'][3],
            'r5': givenCountry['counts'][4]
        }
        if region == "EEU":
            csv_list.append(
                "place_id,name,phone,house_number,street_basename,street_type,city,state,country,postal,nt_cat_id,nt_cat_name,pd_cat_id,pd_cat_name,lat,lon,isplace,isopen,isname,isaddr,isphone,reality_score,full_house_number,district"
            )
        else:
            csv_list.append(
                "place_id,name,phone,house_number,street_basename,street_type,city,state,country,postal,nt_cat_id,nt_cat_name,pd_cat_id,pd_cat_name,lat,lon,isplace,isopen,isname,isaddr,isphone,reality_score"
            )
        for item in randomed_list:
            doc = xml.dom.minidom.parseString(item)
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

            if region != "LAM":
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
            if region == "EEU":
                csv_list.append(
                    placeid
                    +","+fix_quote(name)
                    +","+fix_quote(phone)
                    +","+fix_quote(house_number)
                    +","+fix_quote(street_basename)
                    +","+fix_quote(street_type)
                    +","+fix_quote(city)
                    +","+fix_quote(state)
                    +","+fix_quote(country)
                    +","+fix_quote(postal)
                    +","+fix_quote(country)
                    +","+fix_quote(poi_category_id)
                    +","+fix_quote(poi_category_name)
                    +","+fix_quote(lcms_category_id+"|"+lcms_category_name)
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
                )
            else:
                csv_list.append(
                    placeid
                    +","+fix_quote(name)
                    +","+fix_quote(phone)
                    +","+fix_quote(house_number)
                    +","+fix_quote(street_basename)
                    +","+fix_quote(street_type)
                    +","+fix_quote(city)
                    +","+fix_quote(state)
                    +","+fix_quote(country)
                    +","+fix_quote(postal)
                    +","+fix_quote(country)
                    +","+fix_quote(poi_category_id)
                    +","+fix_quote(poi_category_name)
                    +","+fix_quote(lcms_category_id+"|"+lcms_category_name)
                    +","+lat
                    +","+lon
                    +","+isplace
                    +","+isopen
                    +","+isname
                    +","+isaddr
                    +","+isphone
                    +","+reality_score
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

def save_csv_list(csv_list, country, region, kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(dir_path, kick_off_date,region+"_"+country+"_"+kick_off_date+".csv")
    if region == "BIG7":
        file_name = os.path.join(dir_path, kick_off_date, country+"_"+kick_off_date+".csv")
    fo = open(file_name, 'wb')
    for line in csv_list:
        fo.write(line.encode('UTF-8')+"\r\n")
        # fo.write(line+"\t\n")

def fix_quote(input):
    if "," in input:
        return "\""+input+"\""
    return input

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
