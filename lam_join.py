import os
import sys

def join_por(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(os.path.join(dir_path, kick_off_date))
    aggregeted_csv = []
    for file in files:
        if file.startswith("LAM_BRA"):
            fr = open(os.path.join(dir_path, kick_off_date, file), 'r', encoding="utf-8")
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line)
                else:
                    aggregeted_csv.append(line)
            os.remove(file)

    fw = open(os.path.join(dir_path, kick_off_date, "LAM_POR_"+kick_off_date+".csv"), 'w', encoding="utf-8")
    for item in aggregeted_csv:
        fw.write(item)

def join_spa(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(os.path.join(dir_path, kick_off_date))
    aggregeted_csv = []
    for file in files:
        if not file.startswith("LAM_BRA"):
            fr = open(os.path.join(dir_path, kick_off_date, file), 'r', encoding="utf-8")
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line)
                else:
                    aggregeted_csv.append(line)
            os.remove(os.path.join(dir_path, kick_off_date, file))

    fw = open(os.path.join(dir_path, kick_off_date, "LAM_SPA_"+kick_off_date+".csv"), 'w', encoding="utf-8")
    for item in aggregeted_csv:
        fw.write(item.encode('utf8'))

if __name__ == "__main__":
    join_por(sys.argv[1])
    join_spa(sys.argv[1])