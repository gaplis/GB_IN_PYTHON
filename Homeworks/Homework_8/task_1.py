# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle


def pickle_to_csv(pickle_path, result_path):
    with (
        open(pickle_path, 'rb') as f_read,
        open(result_path, 'w', encoding='utf-8', newline='') as f_write
    ):
        pkl = pickle.load(f_read)
        headers = pkl[0].keys()
        csv_writer = csv.DictWriter(f_write, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(pkl)


pickle_to_csv('../../Seminars/Seminar_8/pickles/task_4.pickle', 'task_1.csv')
