
import os
import sys
from shutil import copyfile

def create_dir(name):
    try:
        os.mkdir(name)
        return ('����� ' + name + ' �������')
    except FileExistsError:
        return ('����� ' + name + ' ����������')


def list_dir():
    return filter(lambda x: os.path.isdir(x), os.listdir())


# ������� ��� ������� normal
def del_dir(name):
    try:
        os.rmdir(name)
        return ('����� ' + name + ' �������')
    except FileNotFoundError:
        return ('����� ' + name + ' �� ���������� ')


def set_dir(name):
    try:
        curr_dir = os.getcwd()
        os.chdir(curr_dir + r'\\' + name)
        return ('���� ������ �� ' + os.getcwd())
    except Exception as e:
        return e


# -------------��������-----------------------------------------------
if __name__ == "__main__":
# ������-1:
# �������� ������, ��������� ���������� dir_1 - dir_9 � �����,
# �� ������� ������� ������ ������.
# � ������ ������, ��������� ��� �����.
    for i in range(9):
        print(create_dir('dir_' + str(i + 1)))

# ������-2:
# �������� ������, ������������ ����� ������� ����������.
    listdir = list_dir()
    print(list(listdir))

# ������-3:
# �������� ������, ��������� ����� �����, �� �������� ������� ������ ������.
# filename = sys.argv[0]
    filename = os.path.basename(sys.argv[0])
    copyfile(filename, filename[0:-3] + '_copy' + '.py')

for i in range(9):
    print(del_dir('dir_' + str(i + 1)))

# print (create_dir('newdir'))
# print (set_dir('newdir'))
# print (set_dir('../'))

import hw05_easy as hw

intro = "1. ������� � �����\n2. ����������� ���������� ������� �����\n3. ������� �����\n4. ������� �����\n0. �����\n"
# ��� ������ ������� 1, 3, 4 ��������� ����������� �������� �����
answer = ''

while answer != '0':
    answer = input (intro)
    if answer in ('1', '3', '4'):
        dirname = input ('������� �������� �����: ')
        if answer == '1':
            print (hw.set_dir(dirname))
        elif answer == '3':
            print(hw.del_dir(dirname))
        elif answer == '4':
            print(hw.create_dir(dirname))
    elif answer == '2':
        print (list(hw.list_dir()))