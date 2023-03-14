class ShopCart:
    def __init__(self,total_price,course):
        self.total_price = total_price
        self.course = [] #list of Course Object

class Payment:
    def __init__(self,order_number,buy_list):
        self.order_number = order_number
        self.buy_list = buy_list #ShopCart Object

class Receipt:
    def __init__(self,receipt_payment,order_date,order):
        self.receipt_payment = receipt_payment
        self.order_date = order_date
        self.order = order #Payment Object
