# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

from pathlib import Path


def func_rename(path, new_name, old_ext, new_ext):
    direct = Path(path)
    find_ext = [i for i in direct.iterdir() if i.suffix[1:] == old_ext]
    for e, f in enumerate(find_ext, start=1):
        Path.rename(f, Path(f"{path}/{f.stem}({new_name}_{e}).{new_ext}"))


func_rename('.', 'file_№', 'txt', 'text')
