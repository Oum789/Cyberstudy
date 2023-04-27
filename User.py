import re
class User:
    def __init__(self, picture, name , email, password):
        self.__picture = picture
        self.__name = name
        self.__email = email
        self.__password = password
        self.__receipt_list = []
    
    def get_picture(self):
        return self.__picture

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def view_profile(self):
        return {"picture": self.get_picture(), "name": self.get_name(), "email": self.get_email(),"password": self.get_password()}
    
    def add_receipt_to_list(self,Receipt):
        self.__receipt_list.append(Receipt)
    
    def change_password(self,new_password,old_password):
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        if self.get_password() == old_password and self.get_password() != new_password and re.match(password_pattern, new_password):
            self.__password = new_password
            return {"status" : "password successfully changed", "new password" : self.get_password()}
        elif self.get_password() != old_password:
            return {"status": "ERROR : incorrect old password"}
        elif self.get_password() == new_password:
            return {"status" : "ERROR : same password"}
        elif re.match(password_pattern, new_password) == None:
            return {"status" : "invalid password -> \n1) Has minimum 8 characters in length. \n2) At least one uppercase English letter. \n3) At least one lowercase English letter. \n4) At least one digit."}

        
    def change_username(self,new_username,user_list,password):
        username_pattern = r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$'
        if password == self.get_password() and re.match(username_pattern, new_username) :
            for i in user_list.user_list:
                    if i.get_name() != new_username:
                        pass
                    else:
                        return {"status" : "This username has been used"}
            self.__name = new_username
            return {"status" : "username successfully changed", "new username" : self.get_name()}
        elif password != self.get_password():
            return {"status" : "ERROR : incorrect password"}
        elif re.match(username_pattern, new_username) == None:
            return {"status" : "invalid username -> \n1) Username must be 6-30 characters long. \n2) Username may only contain: Uppercase and lowercase letters, \nNumbers from 0-9 and Special characters (_ - .). \n3) Username may not: Begin or finish with characters (_ - .), \nHave more than one sequential character (_ - .)inside."}
        
        
    def change_email(self,new_email,user_list,password):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if password == self.get_password() and re.fullmatch(email_pattern, new_email) :
            for i in user_list.user_list:
                    if i.get_email() != new_email:
                        pass
                    else:
                        return {"status" : "This email has been used"}
            self.__email = new_email
            return {"status" : "email successfully changed", "new email" : self.get_email()}
        elif password != self.get_password():
            return {"status" : "ERROR : incorrect password"}
        elif re.fullmatch(email_pattern, new_email) == None:
            return{"status" : "invalid email -> xxx@xxx.xxx"}
        
    def change_picture(self, picture):
        self.__picture = picture

        


    
class UserList:
    def __init__(self) -> None:
        self.__user_list = []

    def add_user_to_list(self,User):
        self.__user_list.append(User)

    def register(self, picture, username, email, password, con_password):
        username_pattern = r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$'
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        user_format = re.match(username_pattern, username)
        email_format = re.fullmatch(email_pattern, email)
        password_format_1 = re.match(password_pattern, password)
        password_format_2 = re.match(password_pattern, con_password)

        if user_format and email_format and password_format_1 and password_format_2 and password == con_password:
            user = {}
            user[username] = User(picture, username,email,password)
            self.add_user_to_list(user[username])
            return {"status" : "register successfully"}
        elif user_format == None:
            return {"status" : "invalid username -> \n1) Username must be 6-30 characters long. \n2) Username may only contain: Uppercase and lowercase letters, \nNumbers from 0-9 and Special characters (_ - .). \n3) Username may not: Begin or finish with characters (_ - .), \nHave more than one sequential character (_ - .)inside."}
        elif email_format == None:
            return{"status" : "invalid email -> xxx@xxx.xxx"}
        elif password_format_1 == None or password_format_2 == None:
            return {"status" : "invalid password -> \n1) Has minimum 8 characters in length. \n2) At least one uppercase English letter. \n3) At least one lowercase English letter. \n4) At least one digit."}
        elif password != con_password:
            return {"status" : "Two passwords doesn't match"}
        
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
                return user
        return 0