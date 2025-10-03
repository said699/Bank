import pickle
from typing import BinaryIO

class Bank:
    def __init__(self, check):
        self.__check = check

    def show_check(self):
        return self.__check

    def replenishment(self):
        while True:
            try:
                sum_to_addition = int(input('Введите сумму которую хотите закинуть на счёт: '))
                self.__check += sum_to_addition
                print('Операция прошла успешно!\n')
                break

            except ValueError:
                print('Не верный ввод!\n')

    def withdrawal(self):
        while True:
            try:
                sum_to_removale = int(input('Введите сумму которую хотите снять: '))
                if sum_to_removale > self.__check:
                    print('На счету недостаточно средств!\n')

                elif sum_to_removale == self.__check:
                    choice = input('Вы точно хотите снять все средства: ').lower()
                    if choice == 'да':
                        self.__check -= sum_to_removale
                        print('Операция прошла успешно!\n')
                        break

                    elif choice == 'нет':
                        print('Как пожелаеете\n')
                        break

                    else:
                        print('Не известная команда!\n')

                elif sum_to_removale <= self.__check:
                    self.__check -= sum_to_removale
                    print('Операция прошла успешно!\n')
                    break

            except ValueError:
                print('Не верный ввод!\n')


FILENAME = 'file.dat'
check_now = 0

try:
    with open(FILENAME, 'rb') as file:
        check_now = pickle.load(file)
except (FileNotFoundError, EOFError):
    print('Файл не найден!')

user_check = Bank(check_now)

while True:
    user_choice = input('Введите операцию (Вывод/Выход/Снятие/Пополнение): ').lower()

    if user_choice in ('вывод', '1'):
        print(user_check.show_check())

    elif user_choice in ('выход', '2'):
        with open(FILENAME, 'wb') as file:
            pickle.dump(user_check.show_check(), file)

        print('До свидания!')
        break

    elif user_choice in ('снятие', '3'):
        user_check.withdrawal()

    elif user_choice in ('пополнение', '4'):
        user_check.replenishment()

    else:
        print('Не извесная операция!\n')