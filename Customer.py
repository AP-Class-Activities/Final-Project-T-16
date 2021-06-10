'''
This class gathers customers' information.
More details will be added!






'''


class  Customer:
    def __init__(self, id, name, family, phone, wallet, address):
        self.__id = id
        self.__name = name
        self.__family = family
        self.__phone = phone
        self.__wallet = wallet
        self.__address = address


        if id[0:2] not in ['CU'] or len(id)!=8: 
            raise ValueError('Your ID is not valid!')
        self.__id = id

        if len(phone)!=11: 
            raise ValueError('Your phone number is not valid!')
        self.__phone = phone 

 



    #setters and getters
    @property
    def ID(self): 
        return self.__id
    
    @ID.setter
    def ID(self,value): 
        self.__id = value

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def family(self): 
        return self.__family

    @family.setter
    def family(self,value): 
        self.__family = value

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
    def address(self): 
        return self.__address
    
    @address.setter
    def address(self,value): 
        self.__address = value





    def __str__(self): 
        return 'ID: {}   name: {} {}   phone: {}   Wallet: {} Coin    address: {}'\
            .format(self.ID,self.name, self.family, self.phone, self.wallet, self.address)
   


#example Customer code:  
s = Customer('CU123123', 'ali', 'ali', '09', 1000, 70 )
print(s)
print
