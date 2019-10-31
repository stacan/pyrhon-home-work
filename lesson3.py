#easy

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


def my_round(number, ndigits):
    new_string = f'%.{ndigits}f'
    return (new_string % number)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#########################################################################
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))



def lucky_ticket(ticket_number):
    new_string = str(ticket_number)
    if len(new_string) != 6:
        return 'Не счастливый'
    else:
        sum_first_half = int(new_string[0]) + int(new_string[1]) + int(new_string[2])
        sum_second_half_string = int(new_string[3]) + int(new_string[4]) + int(new_string[5])
    if sum_first_half == sum_second_half_string:
        return 'Счастливый'
        
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

#########################################################################################

#normal

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass


def fibonacci(first, last):
    res = []
    num1 = 0
    num2 = 1 
    for i in range(last + 1):
        if i >= first: res.append(num2)
        num1, num2 = num2, num2 + num1
    return res


fst = int(input("Введите номер первого элемента: "))
lst = int(input("Введите номер второго элемента: "))
print(fibonacci(fst, lst))


###########################################################################
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

def sort_to_max(origin_list):
    number = 1
    while number < len(origin_list):
        for index in range(len(origin_list) - 1):
            if origin_list[index] > origin_list[index + 1]:
                origin_list[index], origin_list[index + 1] = origin_list[index + 1], origin_list[index]
        number += 1
    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])



######################################################################################
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def myfilter(function, filter_list):
    output_list = []
    for index in filter_list:
        if function(index) == True:
            output_list.append(index)
    return output_list

input_list = [1, 2, 3, 4, '5', 6, 7, 8, 9, 0]
print(myfilter((lambda x: x == '5'), input_list))

#######################################################################################
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print("Задача 4: ")
print()


def parallelogramm(a1, a2, a3, a4):
    def central(a, b):
        return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

    if a1 == a3:
        return "не является параллелограмом"
    elif central(a1, a3) == central(a2, a4):
        return "является параллелограмом"


print("Фигура с вершинами:", (1, 1), (1, 1), (1, 1), (1, 1), parallelogramm((1, 1), (1, 1), (1, 1), (1, 1)))
print("Фигура с вершинами:", (0, 0), (2, 2), (8, 2), (6, 0), parallelogramm((0, 0), (2, 2), (8, 2), (6, 0)))


