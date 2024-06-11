# Без ООП
# Банк 2
# Единственный счет
accountName = ""
accountBalance = 0
accountPassword = ""

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print("\tИмя", accountName)
    print("\tБаланс", accountBalance)
    print("\tПароль", accountPassword)
    print()

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print("Неверный пароль.")
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print("Вы ввели отрицательное значение.")
        return None

    if password != accountPassword:
        print("Неверный пароль.")
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print("Вы ввели отрицательное значение.")
        return None

    if password != accountPassword:
        print("Неверный пароль.")
        return None

    if amountToWithdraw > accountBalance:
        print("Недостаточно средств.")
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance

newAccount("Иванов И.И.", 100, "qwerty") # создание аккаунта

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
            print("Ваш новый баланс составляет: ", accountBalance, "рублей.")

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
        newBalance = withdraw(userWithdrawAmount, userPassword)
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