from abc import ABC,abstractmethod




class PaymentGateway(ABC):
    def __init__(self,bal):
        self._bal=bal
    
    @abstractmethod
    def pay(self,amt,pin):
        pass



class Googlepay(PaymentGateway)  :
        def __init__(self,pin,bal):
            self.__pin=pin
            super().__init__(bal)
        
        
        def pay(self,amt,pin):
            if self.__pin!=pin:
                print("Invalid Pin")
                return
            elif self._bal<amt:
                 print("Insufficient Amount")
                 return
            else:
                 self._bal-=amt
                 print(f"An amount of {amt} is debited")



class CreditCard(PaymentGateway)  :
        def __init__(self,accpin,bal):
            self.__accpin=accpin
            super().__init__(bal)
        
        
        def pay(self,amt,pin):
            if self.__accpin!=pin:
                print("Invalid Pin")
                return
            elif self._bal<amt:
                 print("Insufficient Amount")
                 return
            
            else:
                self._bal-=amt
                print(f"An amount of {amt} is debited")



def make_payment(gateway:PaymentGateway,amt,pin):
     gateway.pay(amt,pin)


make_payment(Googlepay(101,2000),101,300)
make_payment(CreditCard(101,2000),200,101)

            
                 
                  
        