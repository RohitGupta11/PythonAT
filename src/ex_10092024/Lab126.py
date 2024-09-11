#custom exception-own
import os
class MycustomException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)

    balance=100
    withdraw=int(input("enter the amunt you want to withdraw:"))
    if withdraw>balance:
        raise MycustomException("balance is low")
    else:
        print("remaining balance:",(balance-withdraw))