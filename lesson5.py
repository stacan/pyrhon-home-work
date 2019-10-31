
import os
import sys
from shutil import copyfile

def create_dir(name):
    try:
        os.mkdir(name)
        return ('Папка ' + name + ' создана')
    except FileExistsError:
        return ('Папка ' + name + ' существует')


def list_dir():
    return filter(lambda x: os.path.isdir(x), os.listdir())


# функции для решения normal
def del_dir(name):
    try:
        os.rmdir(name)
        return ('Папка ' + name + ' удалена')
    except FileNotFoundError:
        return ('Папка ' + name + ' не существует ')


def set_dir(name):
    try:
        curr_dir = os.getcwd()
        os.chdir(curr_dir + r'\\' + name)
        return ('Путь изменён на ' + os.getcwd())
    except Exception as e:
        return e


# -------------действия-----------------------------------------------
if __name__ == "__main__":
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
    for i in range(9):
        print(create_dir('dir_' + str(i + 1)))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
    listdir = list_dir()
    print(list(listdir))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# filename = sys.argv[0]
    filename = os.path.basename(sys.argv[0])
    copyfile(filename, filename[0:-3] + '_copy' + '.py')

for i in range(9):
    print(del_dir('dir_' + str(i + 1)))

# print (create_dir('newdir'))
# print (set_dir('newdir'))
# print (set_dir('../'))

import hw05_easy as hw

intro = "1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\n0. Выход\n"
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
answer = ''

while answer != '0':
    answer = input (intro)
    if answer in ('1', '3', '4'):
        dirname = input ('Введите название папки: ')
        if answer == '1':
            print (hw.set_dir(dirname))
        elif answer == '3':
            print(hw.del_dir(dirname))
        elif answer == '4':
            print(hw.create_dir(dirname))
    elif answer == '2':
        print (list(hw.list_dir()))