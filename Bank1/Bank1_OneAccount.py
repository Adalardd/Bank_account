# Без ООП
# Банк. Версия 1
# Единственный счет

accountName = "Иванов И.И."
accountBalance = 100
accountPassword = "qwerty"

while True:
    print()
    print("Добро пожаловать,", accountName, "!")
    print("Нажмите b, чтобы увидеть баланс.")
    print("Нажмите d, чтобы внести депозит.")
    print("Нажмите w, чтобы снять депозит.")
    print("Нажмите s, чтобы увидеть учетную запись.")
    print("Нажмите q, чтобы выйти.")
    print()

    action = input("Что вы хотите сделать? ")
    action = action.lower() # переводим в нижний регистр
    action = action[0] # используем первую букву

    print()

    if action == "b":
        print("Ваш баланс: ")
        userPassword = input("Пожалуйста, введите ваш пароль: ")
        if userPassword != accountPassword:
            print("Неверный пароль.")
        else:
            print("Ваш баланс составляет", accountBalance, "рублей.")

    elif action == "d":
        print("Внесите депозит: ")
        userDepositAmount = input("Какую сумму Вы хотите внести? ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Пожалуйста, введите ваш пароль: ")

        if userDepositAmount < 0:
            print("Вы ввели отрицательное значение.")
        
        elif userPassword != accountPassword:
            print("Неверный пароль.")

        else: # OK
            accountBalance = accountBalance + userDepositAmount
            print("Ваш новый балан составляет: ", accountBalance, "рублей.")

    elif action == "s": # отображаем
        userPassword = input("Пожалуйста, введите ваш пароль: ")
        if userPassword != accountPassword:
            print("Неверный пароль.")
        else:
            print("Учетная запись: ")
            print("\tИмя: ", accountName)
            print("\tБаланс: ", accountBalance)
            print("\tПароль: ", accountPassword)
            print()

    elif action == "q":
        break

    elif action == "w":
        print("Снятие депозита: ")

        userWithdrawAmount = input("Какую сумму Вы хотите снять? ")
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input("Пожалуйста, введите ваш пароль: ")
        if userWithdrawAmount < 0:
            print("Вы ввели отрицательное значение.")
        elif userPassword != accountPassword:
            print("Неверный пароль.") 
    elif userWithdrawAmount > accountBalance:
        print("Недостаточно средств.")
    
    else: # OK
        accountBalance = accountBalance - userWithdrawAmount
        print("Ваш новый баланс составляет: ", accountBalance, "рублей.")

print("Готово.")