import os
import sys

def join_por(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(os.path.join(dir_path, kick_off_date))
    aggregeted_csv = []
    for file in files:
        if file.startswith("LAM_BRA"):
            fr = open(os.path.join(dir_path, kick_off_date, file), 'rb')
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line.decode("UTF-8"))
                else:
                    aggregeted_csv.append(line.decode("UTF-8"))
            os.remove(os.path.join(dir_path, kick_off_date, file))

    fw = open(os.path.join(dir_path, kick_off_date, "LAM_POR_"+kick_off_date+".csv"), 'wb')
    for item in aggregeted_csv:
        fw.write(item.encode("UTF-8"))

def join_spa(kick_off_date):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(os.path.join(dir_path, kick_off_date))
    aggregeted_csv = []
    for file in files:
        if file.startswith("LAM_") and not file.startswith("LAM_BRA"):
            fr = open(os.path.join(dir_path, kick_off_date, file), 'rb')
            for line in fr:
                if line.startswith("place_id"):
                    if len(aggregeted_csv)==0:
                        aggregeted_csv.append(line.decode("UTF-8"))
                else:
                    aggregeted_csv.append(line.decode("UTF-8"))
            os.remove(os.path.join(dir_path, kick_off_date, file))

    fw = open(os.path.join(dir_path, kick_off_date, "LAM_SPA_"+kick_off_date+".csv"), 'wb')
    for item in aggregeted_csv:
        fw.write(item.encode('UTF-8'))

if __name__ == "__main__":
    join_por(sys.argv[1])
    join_spa(sys.argv[1])