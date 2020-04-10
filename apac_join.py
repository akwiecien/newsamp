import os
import sys

def join(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    first = False
    aggregeted_csv = []
    for file in files:
        if not ".csv" in file and not "APAC_" in file:
            continue
        if "APAC_IND" in file or "APAC_BGR" in file or "APAC_NPL" in file or "APAC_LKA" in file:
            fr = open(os.path.join(dir_path, file), 'r')
            for line in fr:
                if "place_id," in line and first == False:
                    aggregeted_csv.append(line)
                if not "place_id," in line:
                    aggregeted_csv.append(line)
        os.remove(file)
    fw = open(os.path.join(dir_path,"RN_"+kick_off_date+".csv"), 'w')
    for item in aggregeted_csv:
        fw.write(item.encode('utf8')+"\r\n")


if __name__ == "__main__":
    join(sys.argv[0])