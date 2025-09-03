class User():

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__balance = 0
        self.product1 = 100
        self.product2 = 50
        self.product3 = 300
        self.product4 = 150
        self.orders = []

    def add_id(self, id:int):
        self.__id = id
        return 'Мы добавили id'

    def get_id(self):
        return self.__id

    def add_name(self, name:str):
        self.__name = name
        return 'Мы добавили имя'

    def get_name(self):
        return self.__name
    
    def add_balance(self, balance:int):
        self.__balance += balance
        return 'Мы добавили баланс'

    def get_balance(self):
        return self.__balance
    
    def add_product1(self, product1:int):
        self.product1 = product1
        return 'Мы добавили продукт'

    def get_product1(self):
        return self.product1
    
    def add_product2(self, product2:int):
        self.product2 = product2
        return 'Мы добавили продукт'

    def get_product2(self):
        return self.product2
    
    def add_product3(self, product3:int):
        self.product3 = product3
        return 'Мы добавили продукт'

    def get_product3(self):
        return self.product3
    
    def add_product4(self, product4:int):
        self.product4 = product4
        return 'Мы добавили продукт'

    def get_product4(self):
        return self.product4
    
    def add_orders(self, name_order:str) -> str:
        self.orders.append(name_order)
        return "Мы добавили заказ"
    
    def get_orders(self) -> list:
        return self.orders
    
    def minus_balance(self, item:int):
        self.__balance -= item
        return "Мы отняли ваш баланс"
    
    def about(self):
        return f"""
Имя: {self.__name},
Баланс: {self.__balance},
Id: {self.__id},
Ваши покупки: {self.orders};
"""

user = User()