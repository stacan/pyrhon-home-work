#hw6

#easy
'''
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, vert=({"x": 1, "y": 1}, {"x": 5, "y": 10}, {"x": 10, "y": 1})):
        self.a = math.sqrt((vert[1]["x"] - vert[0]["x"])**2 + (vert[1]["y"] - vert[0]["y"])**2)
        self.b = math.sqrt((vert[2]["x"] - vert[1]["x"])**2 + (vert[2]["y"] - vert[1]["y"])**2)
        self.c = math.sqrt((vert[2]["x"] - vert[0]["x"])**2 + (vert[2]["y"] - vert[0]["y"])**2)

    def get_perimeter(self):
        p = self.a + self.b + self.c
        return round(p, 2)

    def get_area(self):
        try:
            p = self.get_perimeter() / 2
            s = (math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"
        return round(s, 2)

    def get_height(self):
        try:
            s = self.get_area()
            h_ab = round((2 * s) / self.a, 2)
            h_bc = round((2 * s) / self.b, 2)
            h_ca = round((2 * s) / self.c, 2)
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"
        return {"H ab": h_ab, "H bc": h_bc, "H ca": h_ca}

print("--- Задача-1 ---")
vertices_1 = ({"x": 4, "y": 3}, {"x": 16, "y": -6}, {"x": 20, "y": 16})
vertices_2 = ({"x": -6, "y": 1}, {"x": 2, "y": 4}, {"x": 2, "y": -2})
vertices_3 = ({"x": 7, "y": 8}, {"x": -4, "y": 5}, {"x": -1, "y": -4})

triangle_1 = Triangle(vertices_1)
print("Треугольник №1, периметр --> {}, площадь --> {}, высоты --> {}".format(
    triangle_1.get_perimeter(), triangle_1.get_area(), triangle_1.get_height()))
triangle_2 = Triangle(vertices_2)
print("Треугольник №2, периметр --> {}, площадь --> {}, высоты --> {}".format(
    triangle_2.get_perimeter(), triangle_2.get_area(), triangle_2.get_height()))
triangle_3 = Triangle(vertices_3)
print("Треугольник №2, периметр --> {}, площадь --> {}, высоты --> {}".format(
    triangle_3.get_perimeter(), triangle_3.get_area(), triangle_3.get_height()))

print("-" * 16)



import math

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, vert=({"x": 0, "y": 5}, {"x": -2, "y": 4}, {"x": 4, "y": 2}, {"x": 3, "y": 4})):
        self.x1, self.x2, self.x3, self.x4 = vert[0]["x"], vert[1]["x"], vert[2]["x"], vert[3]["x"]
        self.y1, self.y2, self.y3, self.y4 = vert[0]["y"], vert[1]["y"], vert[2]["y"], vert[3]["y"]
        self.a = round(math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2)), 2)
        self.b = round(math.sqrt(((self.x3 - self.x2)**2) + ((self.y3 - self.y2)**2)), 2)
        self.c = round(math.sqrt(((self.x4 - self.x3)**2) + ((self.y4 - self.y3)**2)), 2)
        self.d = round(math.sqrt(((self.x1 - self.x4)**2) + ((self.y1 - self.y4)**2)), 2)

    def isosceles(self):
        try:
            if (((self.a == self.c) and ((self.x4 - self.x1) / self.d == (self.x3 - self.x2) / self.b)) or
                ((self.b == self.d) and ((self.x3 - self.x4) / self.c == (self.x2 - self.x1) / self.a)) or
               ((self.a == self.c) and (self.b == self.d)) or ((self.b == self.d) and (self.c == self.a))):
                return True
            else:
                return False
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"
    def get_perimeter(self):
        p = self.a + self.b + self.c + self.d
        return round(p, 2)

    def get_area(self):
        try:
            h = math.sqrt(self.a**2 - ((((self.d - self.b)**2) + (self.a**2 - self.c**2)) / (2 * (self.d - self.b)))**2)
            s = ((self.b + self.d) / 2) * h
        except (ValueError, ZeroDivisionError):
            return "Ошибка, возможно значения координат не корректны"
        return round(s, 2)


# ---------------тесты задачи 2--------------------------------------------------
print("--- Задача-2 ---")
trap_0 = Trapeze()
print("\nТрапеция 0")
print(f'{"Точки образуют равнобедренную трапецию" if trap_0.isosceles() else "Точки не образуют равнобедренную трапецию"}')
print(f'Стороны --> a:{trap_0.a}, b:{trap_0.b}, c:{trap_0.c}, d:{trap_0.d}')
print(f'Периметр --> {trap_0.get_perimeter()}')
print(f'Площадь --> {trap_0.get_area()}')

trap_ver_1 = ({"x": -2, "y": -2}, {"x": -3, "y": 1}, {"x": 7, "y": 7}, {"x": 3, "y": 1})
trap_1 = Trapeze(trap_ver_1)
print("\nТрапеция 1")
print(f'{"Точки образуют равнобедренную трапецию" if trap_1.isosceles() else "Точки не образуют равнобедренную трапецию"}')
print(f'Стороны --> a:{trap_1.a}, b:{trap_1.b}, c:{trap_1.c}, d:{trap_1.d}')
print(f'Периметр --> {trap_1.get_perimeter()}')
print(f'Площадь --> {trap_1.get_area()}')

trap_ver_2 = ({"x": -20, "y": -15}, {"x": -10, "y": 8}, {"x": 10, "y": 8}, {"x": 20, "y": -15})
trap_2 = Trapeze(trap_ver_2)
print("\nТрапеция 2")
print(f'{"Точки образуют равнобедренную трапецию" if trap_2.isosceles() else "Точки не образуют равнобедренную трапецию"}')
print(f'Стороны --> a:{trap_2.a}, b:{trap_2.b}, c:{trap_2.c}, d:{trap_2.d}')
print(f'Периметр --> {trap_2.get_perimeter()}')
print(f'Площадь --> {trap_2.get_area()}')
print("-" * 16)


#normal

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.



# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


from random import *

FAMILY = ("Хокаге", "Самохвалов", "Брызгин", "Раев", "Черноземов")
NAME = ("Илья", "Федор", "Наруто", "Нестор", "Джон")
SUBJECT = ("Математика", "Химия", "Биология", "История", "Аниме")
LETTER = ("А", "Б", "В", "Г", "Д")


class School():
    def __init__(self, name):
        self.name = name
        self.Classes = []

    def addClass(self, Clas):
        self.Classes.append(Clas)
        
#1.Получить полный список всех классов школы
    def showClasses(self):
        print('Школа {} содержит:'.format(self.name))
        for itm in self.Classes:
            print('класс {}'.format(itm.name))

    def showClass(self, name):
        for itm in self.Classes:
            if itm.name == name: itm.showClass()



# 3.Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
    def showPupilInfo(self, name):
        for cl in self.Classes:
            for pup in cl.Pupils:
                if pup.name == name:
                    for teach in cl.Teachers:
                        print('Ученик {} класс {} преподаватель {} предмет {}'.format(pup.name, cl.name, teach.name,
                                                                                      teach.subject))

#4.Узнать ФИО родителей указанного ученика
    def showPupilParents(self, name):
        for cl in self.Classes:
            for pup in cl.Pupils:
                if pup.name == name: pup.showParents()

    def genSchool(self, classes, pupils, subjects):
        for idx in range(int(classes)):
            xclass = Class(str(random.randint(1, 11)) + random.choice(LETTER))
            self.addClass(xclass)
            for i in range(int(pupils)):
                xclass.addPupil(Pupil(random.choice(FAMILY) + ' ' + random.choice(NAME) + random.choice(NAME),
                                      random.choice(FAMILY) + ' ' + random.choice(NAME) + random.choice(NAME),
                                      random.choice(FAMILY) + 'а ' + random.choice(NAME) + random.choice(NAME)))
            for i in range(int(subjects)):
                xclass.addTeacher(random.choice(FAMILY) + random.choice(NAME) + random.choice(NAME),
                                  random.choice(SUBJECT))


class Class():
    def __init__(self, name):
        self.name = name
        self.Pupils = []
        self.Teachers = []

    def addPupil(self, pupil):
        self.Pupils.append(pupil)

    def addTeacher(self, name, subject):
        self.Teachers.append(Teacher(name, subject))

# 2.Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
    def showClass(self):
        print('Класс {} содержит:'.format(self.name))
        for itm in self.Pupils:
            print('ученик {}'.format(itm.name))


class Pupil():
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def showParents(self):
        print('Отец - {}, Мать - {}'.format(self.father, self.mother))


class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        

#hard
# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os


workers_file = os.path.join('data', 'workers')	
hours_file = os.path.join('data', 'hours_of')

hours = []
workers = []

with open(hours_file, 'r', encoding='UTF-8') as f:      # создаем список с данными по ФИО и отработанным часам
    lines = f.readlines()[1:]
    for line in lines:
        if '\n' in line:
            hours.append(line[:-1])
        else:
            hours.append(line)

with open(workers_file, 'r', encoding='UTF-8') as f:    # создаем список с данными по ФИО и должностям и базовому окладу
    lines = f.readlines()[1:]
    for line in lines:
        if '\n' in line:
            workers.append(line[:-1])
        else:
            workers.append(line)

full_workers = []

for itm in workers:
    for itm2 in hours:
        if itm.split()[0] in itm2 and itm.split()[1] in itm2:
            full_workers.append(itm + ' ' + itm2.split()[-1])   # список из двух файлов, где создержатся все данные по
                                                                # работникам, включая отработанные часы


class Staff:

     def __init__(self, worker_data):
        worker_data = worker_data.split()
        self.name = worker_data[0]
        self.surname = worker_data[1]
        self.full_salary = int(worker_data[2])
        self.post = worker_data[3]
        self.hours_rule = int(worker_data[4])
        self.hours_done = int(worker_data[5])

@property
def calculate_salary(self):
        salary = 0
        if self.hours_done < self.hours_rule:
            salary = self.full_salary * (self.hours_done/self.hours_rule)
        elif self.hours_done == self.hours_rule:
            salary = self.full_salary
        else:
            salary = self.full_salary + ((self.hours_done - self.hours_rule) * (self.full_salary/self.hours_rule))
        return round(salary, 2)


workers_lst = [Staff(itm) for itm in full_workers]   # создаем список объектов Staff

print(full_workers)


def factory_salary(lst):    # узнать общий фонд оплаты труда
    common_salary = 0
    for itm in lst:
        a = itm.calculate_salary
        common_salary += a
    return common_salary



# a = workers_lst[1].calculate_salary
# print(a)
# print(factory_salary(workers_lst))

'''
# Решение 2

import os

workers_file = os.path.join('data', 'workers')      # путь к файлу работников
hours_file = os.path.join('data', 'hours_of')       # путь к файлу отработанных часов

workers = []

with open(workers_file, 'r', encoding='UTF-8') as f:    # создаем список с данными по ФИО и должностям и базовому окладу
    lines = f.readlines()[1:]
    for line in lines:
        if '\n' in line:
            workers.append(line[:-1])
        else:
            workers.append(line)

class Staff:


     def __init__(self, worker_data):	    
        worker_data = worker_data.split()	        
        self.name = worker_data[0]	        
        self.surname = worker_data[1]	        
        self.full_salary = worker_data[2]	        
        self.post = worker_data[3]	        
        self.hours_rule = int(worker_data[4])
            
@property
def hours_worked(self):
    hours_worked = 0
    with open(hours_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if self.name in line and self.surname in line:
                    hours_worked = int(line.split()[-1])
    return hours_worked

@property
def calculate_salary(self): # вычисляем зарплату конкретного рабочего
    salary = 0
    if self.hours_worked < self.hours_rule:
            salary = self.full_salary * (self.hours_worked/self.hours_rule)
    elif self.hours_worked == self.hours_rule:
            salary = self.full_salary
    else:
            salary = self.full_salary + ((self.hours_worked - self.hours_rule) * (self.full_salary/self.hours_rule))
    return round(salary, 2)     # не оформляем красиво в виде строки, чтобы можно было использовать в расчетах    

workers_lst = [Staff(itm) for itm in workers]   # создаем список объектов Staff


def factory_salary(lst):
    s = 0
    for itm in workers_lst:
        s += itm.calculate_salary
    return f'ФОТ всей фабрики составляет {s}'


# a = workers_lst[4].calculate_salary
#
# b = factory_salary(workers_lst)
# print(a)
# print(b)
