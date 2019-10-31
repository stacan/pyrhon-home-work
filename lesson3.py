#easy

# �������-1:
# �������� �������, ����������� ���������� ������������ ���������� �����
# �� ���-�� ������ (���-�� ������ ���������� ������ ����������).
# ���������� ������ ����������� �� �������������� �������� (0.6 --> 1, 0.4 --> 0).
# ��� ������� ������ �� ����������� ���������� ������� � ������� �� ������ math.

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
# �������-2:
# ��� ������������ ����� ������. ����������, �������� �� ����� ����������.
# ������� ����������� � ���� �������.
# ����� ��������� ����������, ���� ����� ��� ������ � ��������� ���� �����.
# !!!P.S.: ������� �� ������ ������ print'���

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))



def lucky_ticket(ticket_number):
    new_string = str(ticket_number)
    if len(new_string) != 6:
        return '�� ����������'
    else:
        sum_first_half = int(new_string[0]) + int(new_string[1]) + int(new_string[2])
        sum_second_half_string = int(new_string[3]) + int(new_string[4]) + int(new_string[5])
    if sum_first_half == sum_second_half_string:
        return '����������'
        
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

#########################################################################################

#normal

# �������-1:
# �������� �������, ������������ ��� ��������� � n-�������� �� m-��������.
# ������� ���������� ���� ������� ����� 1 1

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


fst = int(input("������� ����� ������� ��������: "))
lst = int(input("������� ����� ������� ��������: "))
print(fibonacci(fst, lst))


###########################################################################
# ������-2:
# �������� �������, ����������� ����������� ������ �� �����������.
# ��� ���������� ����������� ����� �������� (�������� �����������).
# ��� ������� ������ ������ ������ ������������ ���������� ������� � ����� sort()


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
# ������-3:
# �������� ����������� ���������� ����������� ������� filter.
# ����������, ������ ������ ������������ ���� ������� filter.

def myfilter(function, filter_list):
    output_list = []
    for index in filter_list:
        if function(index) == True:
            output_list.append(index)
    return output_list

input_list = [1, 2, 3, 4, '5', 6, 7, 8, 9, 0]
print(myfilter((lambda x: x == '5'), input_list))

#######################################################################################
# ������-4:
# ���� ������ ����� �1(�1, �1), �2(x2 ,�2), �3(x3 , �3), �4(�4, �4).
# ����������, ����� �� ��� ��������� ���������������.

print("������ 4: ")
print()


def parallelogramm(a1, a2, a3, a4):
    def central(a, b):
        return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

    if a1 == a3:
        return "�� �������� ���������������"
    elif central(a1, a3) == central(a2, a4):
        return "�������� ���������������"


print("������ � ���������:", (1, 1), (1, 1), (1, 1), (1, 1), parallelogramm((1, 1), (1, 1), (1, 1), (1, 1)))
print("������ � ���������:", (0, 0), (2, 2), (8, 2), (6, 0), parallelogramm((0, 0), (2, 2), (8, 2), (6, 0)))


