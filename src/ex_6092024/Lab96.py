class Bank:
    def __init__(self,account_number,balance):
        self.balance=balance
        self.__account_number=account_number

    def deposit(self,amount):
        self.balance=self.balance+amount
    def chcek_balanc(self):
        print(self.balance)

    def showme_account(self,is_auth):
        if is_auth==True:
            print(self.__account_number)
        else:
            print("not allowed")

icici=Bank(account_number=9788098,balance=2400)
icici.deposit(100)
icici.chcek_balanc()
icici.showme_account(True)
