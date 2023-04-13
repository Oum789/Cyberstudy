class ShopCart:
    def __init__(self,total_price):
        self.__total_price = total_price
        self.__buying_list = [] #list of Course Object
        
    def get_total_price(self):
        return self.__total_price

    def get_buying_list(self):
        return self.__buying_list
    
    def reset_buying_list(self):
        self.__buying_list = []

    def add_to_cart(self,Course):
        price = Course.get_price()
        self.update_price(price)
        self.__buying_list.append(Course)

    def update_price(self,price):
        self.__total_price += price

    def initiate_payment(self,money):
        if money == self.__total_price:
            return 1
        else:
            return 0    

    def add_to_course_bought():
        pass

class Receipt:
    def __init__(self,receipt_payment,order_date,order):
        self.__receipt_payment = receipt_payment
        self.__order_date = order_date
        self.__order = order

    def save_receipt():
        pass