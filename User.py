class User:
    def __init__(self,name , email, password):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__receipt_list = []
    
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_receipt(self):
        return self.__receipt_list
    
    def add_receipt_to_list(self,Receipt):
        self.__receipt_list.append(Receipt)

class UserList:
    def __init__(self) -> None:
        self.__user_list = []

    def add_user_to_list(self,User):
        self.__user_list.append(User)

    def find_user(self,name):
        for i in self.__user_list:
            username = i.get_name()
            if username.find(name) > -1:
                return i
        return 0

    def check_password(self,mail,pw):
        for i in range (len(self.__user_list)):
            user = self.__user_list[i]
            if mail == user.get_email() and pw == user.get_password():
                return 1
        return 0
    