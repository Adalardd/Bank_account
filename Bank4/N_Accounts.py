# Без ООП
# Банк 4
# Любое количество счетов - со списками

accountNamesList = []
accountBalanceList = []
accountPasswordList = []

def newAccount(name, balance, password):
	global accountNameList, accountBalanceList, accountPasswordList
	accountNamesList.append(name)
	accountBalanceList.append(balance)
	accountPasswordList.append(password)

def show(accountNumber):
	global accountNameList, accountBalanceList, accountPasswordList
	print("Аккаунт", accountNumber)
	print("\tИмя", accountNameList(accountNumber))
	print("\tБаланс", accountBalanceList(accountNumber))
	print("\tПароль", accountPasswordList(accountNumber))
	print()

def getBalance(accountNumber, password):
	global accountNameList, accountBalanceList, accountPasswordList
	if password != accountPasswordList(accountNumber):
		print("Неверный пароль.")
		return None
	return accountBalanceList(accountNumber)	
