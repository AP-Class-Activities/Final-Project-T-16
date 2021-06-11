'''
This class gathers Products' information.
More details will be added!






'''


class  Product:
    def __init__(self, id, name, Category, Size, Wight, Price):
        self.__id = id
        self.__name = name
        self.__Category = Category
        self.__Size = Size
        self.__Wight = Wight
        self.__Price = Price


        if id[0:2] not in ['PR'] or len(id)!=8: 
            raise ValueError('Produc ID is not valid!')
        self.__id = id


 



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
    def Category(self): 
        return self.__Category

    @Category.setter
    def Category(self,value): 
        self.__Category = value

    @property
    def Size(self): 
        return self.__Size

    @Size.setter
    def Size(self,value): 
        self.__Size = value

    @property
    def Wight(self): 
        return self.__Wight

    @Wight.setter
    def Wight(self,value): 
        self.__Wight = value

    @property
    def Price(self): 
        return self.__Price
    
    @Price.setter
    def Price(self,value): 
        self.__Price = value





    def __str__(self): 
        return 'ID: {}   Name: {}, {}   Size: {}Inch   Wight: {}g    Price: {} Coin'\
            .format(self.ID,self.name, self.Category, self.Size, self.Wight, self.Price)
   


#example Client code:  
P = Product('P123123', 'IPhone', 'Tech', 6, 2000, 100 )
print(P)
print
