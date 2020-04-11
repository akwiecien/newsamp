import os
import sys

def join_por(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    aggregeted_csv = []
    for file in files:
        if file.startswith("LAM_BRA"):
            fr = open(os.path.join(dir_path, file), 'r')
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line)
                else:
                    aggregeted_csv.append(line)
            os.remove(file)

    fw = open(os.path.join(dir_path,"LAM_POR_"+kick_off_date+".csv"), 'w')
    for item in aggregeted_csv:
        fw.write(item.encode('utf8'))

def join_spa(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir_path)
    aggregeted_csv = []
    for file in files:
        if not file.startswith("LAM_BRA"):
            fr = open(os.path.join(dir_path, file), 'r')
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line)
                else:
                    aggregeted_csv.append(line)
            os.remove(file)

    fw = open(os.path.join(dir_path,"LAM_SPA_"+kick_off_date+".csv"), 'w')
    for item in aggregeted_csv:
        fw.write(item.encode('utf8'))

if __name__ == "__main__":
    join_por(sys.argv[1])
    join_spa(sys.argv[1])