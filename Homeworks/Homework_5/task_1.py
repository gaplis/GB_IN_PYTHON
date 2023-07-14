# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def path_split(path):
    *path, file_name, file_extension = path.replace('.', '\\').split('\\')
    path = '\\'.join(path)
    return path, file_name, file_extension


my_path = "C:\\Users\\gapli\\Downloads\\GB_IN_PYTHON\\Homeworks\\Homework_5\\task_1.py"
print("path = {}\nfile_name = {}\nfile_extension = {}".format(*path_split(my_path)))