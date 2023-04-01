class User:
    def __init__(self,name , email, password):
        self.__name = name
        self.__email = email
        self.__password = password
    
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def view_profile(self):
        return [self.get_name(),self.get_email(),self.get_password()]
    
class UserList:
    def __init__(self) -> None:
        self.user_list = []

    def add_user_to_list(self,User):
        self.user_list.append(User)

    def check_password(self,mail,pw):
        for i in range (len(self.user_list)):
            user = self.user_list[i]
            if mail == user.get_email() and pw == user.get_password():
                return "Login Successful"
        return "Your password or username is not correct"
    