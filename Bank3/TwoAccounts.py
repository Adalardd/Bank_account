# Без ООП
# Банк 3
# Два счета

account0Name = ""
account0Balance = 0
account0Password = ""
account1Name = ""
account1Balance = 0
account1Password = ""
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
	global account0Name, account0Balance, account0Password
	global account1Name, account1Balance, account1Password

	if accountNumber == 0:
		account0Name = account0Name
		account0Balance = balance
		account0Password = password

	if accountNumber == 1:
		account1Name = name
		account1Balance = balance
		account1Password = password

def show():
	global account0Name, account0Balance, account0Password
	global account1Name, account1Balance, account1Password

	if account0Name != "":
		print("Аккаунт 0")
		print("\tИмя", accountName)
		print("\tБаланс", accountBalance)
		print("\tПароль", accountPassword)
		print()

	if account1Name != "":
		print("Аккаунт 1")
		print("\tИмя", accountName)
		print("\tБаланс", accountBalance)
		print("\tПароль", accountPassword)
		print()

def getBalance(accountNumber, password):
	global account0Name, account0Balance, account0Password
	global account1Name, account1Balance, account1Password

	if accountNumber == 0:
		if password != account0Password:
			print("Неверный пароль.")
			return None
		return account0Balance
	if accountNumber == 1:
		if password != account1Password:
			print("Неверный пароль.")
			return None
		return account1Balance
    	
def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToDeposit < 0:
            print("Вы ввели отрицательное значение.")
            return None
            
        if password != account0Password:
            print("Неверный пароль.")
            return None
        
        account0Balance = account0Balance + amountToDeposit
        return account0Balance

    if accountNumber == 1:
        if amountToDeposit < 0:
            print("Вы ввели отрицательное значение.")
            return None
            
        if password != account1Password:
            print("Неверный пароль.")
            return None
        
        account1Balance = account1Balance + amountToDeposit
        return account1Balance
  
def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if amountToWithdraw < 0:
            print("Вы ввели отрицательное значение.")
            return None

        if password != account0Password:
            print("Неверный пароль.")
            return None

        if amountToWithdraw > account0Balance:
            print("Вы не можете вывести больше, чем есть на Вашем счету.")
            return None

        account0Balance = account0Balance - amountToWithdraw
        return account0Balance

    if accountNumber == 1:
        if amountToWithdraw < 0:
            print("Вы ввели отрицательное значение")
            return None

        if password != account1Password:
            print("Неверный пароль.")
            return None

        if amountToWithdraw > account1Balance:
            print("Вы не можете вывести больше, чем есть на Вашем счету.")
            return None

        account1Balance = account1Balance - amountToWithdraw
        return account1Balance

# Создаем тестовый аккаунт

newAccount(nAccounts, "Иванов И.И.", 100, "qwerty") # создание аккаунта
nAccounts = 1

while True:
    print()
    #print("Добро пожаловать,", accountName, "!")
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
        userAccountNumber = input("Пожалуйста, введите Ваш номер аккаунта: ")
        userAccountNumber = int(userAccountNumber)
        userPassword = input("Пожалуйста, введите Ваш пароль: ")
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print("Ваш баланс: ", theBalance, "рублей.")

    elif action == 'd':
        print("Внесите депозит:")
        userAccountNumber= input("Пожалуйста, введите Ваш номер аккаунта: ")
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input("Какую сумму Вы хотите внести? ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Пожалуйста, введите Ваш пароль: ")
        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print("Ваш новый баланс: ", newBalance, "рублей.")
        
    elif action == 'n':
        print("Создание нового аккаунта: ")
        userName = input("Как Вас зовут? ")
        userStartingAmount = input("Какая сумма у Вас есть для открытия счета? ")
        userStartingAmount = int(userStartingAmount)
        userPassword = input("Придумайте пароль: ")

        newAccount(nAccounts, userName, userStartingAmount, userPassword)
        print("Ваш новый аккаунт: ", nAccounts)
        nAccounts = nAccounts + 1

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

    elif action == 'q':
        break

    elif action == 'w':
        print("Снятие депозита: ")
        userAccountNumber = input("Пожалуйста, введите Ваш номер аккаунта: ")
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input("Пожалуйста, введи сумму которую Вы хотите снять: ")
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input("Пожалуйста, введи пароль: ")
 
        newBalance = withdraw(userAccountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("Ваш новый баланс: ", newBalance, "рублей.")
        
print('Done')            				    				