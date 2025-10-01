class Bank:
    def __init__(self, check):
        self.check = check

    def show_check(self):
        print(f'Нынешнее состояние вашего счёта: {self.check}\n')

    def account_replenishment(self):
        while True:
            try:
                sum_to_addition = int(input('Введите сумму которую хотите закинуть на счёт: '))
                self.check += sum_to_addition
                print('Операция прошла успешно!\n')
                break

            except ValueError:
                print('Не верный ввод!\n')

    def withdrawal_account(self):
        while True:
            try:
                sum_to_removale = int(input('Введите сумму которую хотите снять: '))
                if sum_to_removale > self.check:
                    print('На счету недостаточно средств!\n')
                    break

                elif sum_to_removale == self.check:
                    choice = input('Вы точно хотите снять все средства: ').lower()
                    if choice == 'да':
                        self.check -= sum_to_removale
                        print('Операция прошла успешно!\n')
                        break

                    elif choice == 'нет':
                        print('Как пожелаеете\n')
                        break

                    else:
                        print('Не известная команда!\n')

                elif sum_to_removale <= self.check:
                    self.check -= sum_to_removale
                    print('Операция прошла успешно!\n')
                    break

            except ValueError:
                print('Не верный ввод!\n')

    def __str__(self):
        return 'Это класс Bank!'

user_check = Bank(0)

while True:
    user_choice = input('Введите операцию (Вывод/Выход/Снятие/Пополнение): ').lower()

    if user_choice == 'вывод' or user_choice == '1':
        user_check.show_check()

    elif user_choice == 'выход' or user_choice == '2':
        print('До свидания!')
        break

    elif user_choice == 'снятие' or user_choice == '3':
        user_check.withdrawal_account()

    elif user_choice == 'пополнение' or user_choice == '4':
        user_check.account_replenishment()

    else:
        print('Не извесная операция!\n')