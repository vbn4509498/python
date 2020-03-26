class Drink :
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.__name = new_name
    def get_price(self):
        return  self.price
    def set_price (self,new_price):
        self.__price = new_price