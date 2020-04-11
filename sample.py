import sys
import xml.dom.minidom
import os
import random
import datetime

def main(country, num_files):   
    randomed_list = do_sample(country, num_files)
    print(len(randomed_list))
    save_tmp(randomed_list, country)


def do_sample(country, number_of_files):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(os.path.join(dir_path, 'xml', country))
    randomed_list = []
    if int(number_of_files)<6:
        for file in files:
            print('reading file: '+file)
            base_path = os.path.join(dir_path, 'xml', country)
            content = open(os.path.join(base_path,file), 'r')
            for line in content:
                if len(line)>1000:
                    randomed_list.append(line)
            content.close()
    else:  
        slice_number = int((300000/(int(number_of_files)-1)))
        for file in files:
            print('reading file: '+file)
            base_path = os.path.join(dir_path, 'xml', country)
            content = open(os.path.join(base_path,file), 'r')
            tempList = []
            for line in content:
                if len(line)>1000:
                    tempList.append(line)
            content.close()
            random.shuffle(tempList)
            sl = slice_number
            if sl>len(tempList):
                sl = len(tempList)
            randomed_list = randomed_list + tempList[:sl]
    return randomed_list     

def save_tmp(randomed_list, country):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fw = open(os.path.join(dir_path, "xml", country+"_tmp.csv"), 'a+b')
    for line in randomed_list:
        fw.write(line)
    fw.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
