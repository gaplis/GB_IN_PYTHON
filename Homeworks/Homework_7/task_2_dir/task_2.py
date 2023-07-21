# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами

from task_2_dir.module.task_2_1 import fill_file
from task_2_dir.module.task_2_2 import gen_names
from task_2_dir.module.task_2_3 import work_with_files
from task_2_dir.module.task_2_4 import *

fill_file(7, 'task_1.txt')

gen_names(5, 'task_2.txt')

work_with_files("task_1.txt", "task_2.txt", "task_3.txt")

create('task_4', txt=3, bin=6, jpg=9)
group_files('my_dir')
