import os
import sys

def join(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    first = False
    aggregeted_csv = []
    for file in files:
        if file.startswith("NA_"):
            fr = open(os.path.join(dir_path, file), 'r')
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line)
                else:
                    aggregeted_csv.append(line)
            os.remove(file)

    fw = open(os.path.join(dir_path,"NA_ALL_"+kick_off_date+".csv"), 'w')
    for item in aggregeted_csv:
        fw.write(item.encode('utf8'))


if __name__ == "__main__":
    join(sys.argv[1])