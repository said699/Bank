class Bank:
    def __init__(self, check):
        self.check = check

    def show_check(self):
        print(f'Нынешнее состояние вашего счёта: {self.check}')

    def account_replenishment(self):
        sum_to_addition = int(input('Введите сумму которую хотите закинуть на счёт: '))
        self.check += sum_to_addition

    def withdrawal_account(self):
        sum_to_removale = int(input('Введите сумму которую хотите снять: '))
        if sum_to_removale > self.check:
            print('На счету недостаточно средств!')

        elif sum_to_removale == self.check:
            choice = input('Вы точно хотите снять все средства: ').lower()
            if choice == 'да':
                self.check -= sum_to_removale
            elif choice == 'нет':
                print('Как пожелаеете')

        elif sum_to_removale <= self.check:
            self.check -= sum_to_removale

    def __str__(self):
        return 'Это класс Bank!'

user_check = Bank(0)

while True:
    user_choice = input('Введите операцию (Вывод/Выход/Снятие/Пополнение): ').lower()

    if user_choice == 'снятие':
        user_check.withdrawal_account()
    elif user_choice == 'пополнение':
        user_check.account_replenishment()
    elif user_choice == 'вывод':
        user_check.show_check()
    elif user_choice == 'выход':
        break    
    else:
        print('Не извесная операция!')