import os
import sys

def join(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(os.path.join(dir_path, kick_off_date))
    first = False
    aggregeted_csv = []
    for file in files:
        if "APAC_IND" in file or "APAC_BGR" in file or "APAC_NPL" in file or "APAC_LKA" in file:
            fr = open(os.path.join(dir_path, kick_off_date, file), 'r')
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line)
                else:
                    aggregeted_csv.append(line)
            os.remove(os.path.join(dir_path, kick_off_date, file))

    fw = open(os.path.join(dir_path, kick_off_date, "RN_"+kick_off_date+".csv"), 'w')
    for item in aggregeted_csv:
        fw.write(item.encode('utf8'))


if __name__ == "__main__":
    join(sys.argv[1])