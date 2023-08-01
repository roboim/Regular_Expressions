## Читаем файл в формате CSV
import csv

def read_rows_csv(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def write_rows_csv(filename, data):
    with open(filename, "w", encoding="UTF-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(data)
