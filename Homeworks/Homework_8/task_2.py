# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle


def csv_to_pickle_string(path):
    with open(path, "r", encoding='utf-8') as c:
        csv_string = ''
        for line in c:
            csv_string += line
        pkl = pickle.dumps(csv_string)
        return pkl


print(csv_to_pickle_string('task_1.csv'))
