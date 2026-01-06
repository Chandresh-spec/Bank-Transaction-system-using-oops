from abc import ABC,abstractmethod



class Payment():
    @abstractmethod
    def pay(self,amt):
        pass



class Googlepay(Payment):
    def pay(self,amt):
        print(amt)




class PhonePay(Payment):
    def pay(self,amt):
        print(amt)



def make_payment(gateway:Payment,amt):
    gateway.pay(amt)



make_payment(Googlepay(),100)
make_payment(PhonePay(),200)