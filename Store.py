'''
This class is store's information.
More details will be added!






'''


class  Seller:
    def __init__(self, name, phone, wallet, Coordinate=0):
        self.__name = name
        self.__phone = phone
        self.__wallet = wallet
        self.__Coordinate = Coordinate


    if len(phone)!=11: 
            raise ValueError('Your phone number is not valid!')
    self.__phone = phone        


 



    #setters and getters

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def phone(self): 
        return self.__phone

    @phone.setter
    def phone(self,value): 
        self.__phone = value

    @property
    def wallet(self): 
        return self.__wallet

    @wallet.setter
    def wallet(self,value): 
        self.__wallet = value

    @property
    def Coordinate(self): 
        return self.__Coordinate
    
    @Coordinate.setter
    def Coordinate(self,value): 
        self.__Coordinate = value





    def __str__(self): 
        return 'name: {}   phone: {}   Wallet: {} Coin    Coordinate: {}'\
            .format(self.name, self.phone, self.wallet, self.Coordinate)
   


#example client code:  
s = Seller('Divar', '0133333', 1000 )
print(s)
print
