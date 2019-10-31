
'''
class Wrapped:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

x = Wrapped ([1, 2, 3])
x.append(4)
print(x.wrapped)
x = Wrapped ({'a': 1, 'b': 2})
print(x.keys())
'''



import random

class Barels:
    bug = []
    selected_barell = 0
    def __init__(self):
        self.bug = self.filling_bag()

    def filling_bag(self):
        return_bug = []
        for index in range(1, 91):
            return_bug.append(index)
        return return_bug

    def choose_barel(self):
        if self.selected_barell == 0:
            self.selected_barell = random.choice(self.bug)
        else:
            self.bug.remove(self.selected_barell)
            self.selected_barell = random.choice(self.bug)

class Card:
    def __init__(self):
        self.first_string = self.generate_string()
        self.second_string = self.generate_string()
        self.tree_string = self.generate_string()

    def generate_string(self):
        string = []
        for _ in range(9):
            string.append("")
        index = 0
        while index < 5:
            cell_number = random.randint(0, 8)
            if string[cell_number] == "":
                string[cell_number] = random.randint(1, 91)
                index += 1
        return string

    def print_string(self, string):
        output_string = ""
        for index in string:
            output_string = output_string + str(index) + " "
        print(output_string)

    def print_card(self):
        self.print_string(self.first_string)
        self.print_string(self.second_string)
        self.print_string(self.tree_string)

    def find_number(self, string, number):
        try:
            index = string.index(number)
            string[index] = "-"
        except ValueError:
            return 0

    def check_win(self):
        if self.first_string.count("-") == 5\
        and self.second_string.count("-") == 5 \
        and self.tree_string.count("-") == 5: \
            return 0

    def find_number_card(self, number):
        check_first_string = self.find_number(self.first_string, number)
        check_second_string = self.find_number(self.second_string, number)
        check_tree_string = self.find_number(self.tree_string, number)
        if check_first_string == 0 and check_second_string == 0 and check_tree_string == 0:
            return 0

if __name__ == "__main__":
    input_user = ''
    barels = Barels()
    gamer_card = Card()
    comp_card = Card()
    while True:
        barels.choose_barel()
        print(f"Новый бочонок: {barels.selected_barell} (осталось {len(barels.bug)})")
        print("----Ваша карточка-----")
        gamer_card.print_card()
        print("----------------------")
        print("--Карточка комьютера--")
        comp_card.print_card()
        print("----------------------")
        input_user = input("Зачеркнуть?(Y/N)")
        if input_user == 'y':
            if gamer_card.find_number_card(barels.selected_barell) == 0:
                print("У вас в карточке нет такого значения. Конец игры")
                break
            else:
                comp_card.find_number_card(barels.selected_barell)
        elif input_user == 'n':
            if gamer_card.find_number_card(barels.selected_barell) != 0:
                print("У вас в карточке есть такое значение, вы ошиблись. Конец игры")
                break
            else:
                comp_card.find_number_card(barels.selected_barell)
        else:
            print("Неверный ввод, выход")
            break
        if gamer_card.check_win() == 0:
            print("Поздравляю, вы выиграли!")
        if comp_card.check_win() == 0:
            print("Вы проиграли. Компьютер закрыл все значения")
