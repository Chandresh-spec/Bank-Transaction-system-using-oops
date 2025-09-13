class Bank:
    def __init__(self,bank_num,bal):
        self.ban_num=bank_num
        self.bal=bal

        
    def deposite(self,amount):
        self.bal=self.bal+amount

        print(f"${amount}has been added to your account your balance is{self.bal}")
    

    def withdraw(self,amount):
        self.bal-=amount
        print(f" the amount of {amount} has been withdraw from your bank account and your balance iss", {self.bal})
    


    def bal(self):
        print(f" your balance is {self.bal}")
        




b1=Bank(101010,500)

b1.deposite(500)




    