import re
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
        return {"name": self.get_name(), "email": self.get_email(),"password": self.get_password()}
    
    def change_password(self,new_password,old_password):
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        if self.__password == old_password:
            if self.__password != new_password:
                if re.match(password_pattern, new_password):
                    self.__password = new_password
                    return {"status" : "password successfully changed", "new password" : self.get_password()}
                else:
                    return {"status" : "invalid password -> 1) Has minimum 8 characters in length. 2) At least one uppercase English letter. 3) At least one lowercase English letter. 4) At least one digit."}
            else:
                return {"status" : "ERROR : same password"}
        else:
            return {"status": "ERROR : incorrect old password"}
        
    def change_username(self,new_username,user_list,password):
        username_pattern = r'^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$'
        if password == self.get_password():
            if re.match(username_pattern, new_username):
                for i in user_list.user_list:
                    if i.get_name() != new_username:
                        pass
                    else:
                        return {"status" : "This username has been used"}
                self.__name = new_username
                return {"status" : "username successfully changed", "new username" : self.get_name()}
            else:
                return {"status" : "invalid username -> 1) Username must be 6-30 characters long. 2) Username may only contain: Uppercase and lowercase letters, Numbers from 0-9 and Special characters (_ - .). 3) Username may not: Begin or finish with characters (_ - .), Have more than one sequential character (_ - .)inside."}
        else:
            return {"status" : "ERROR : incorrect password"}
        
    def change_email(self,new_email,user_list,password):
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if password == self.get_password():
            if(re.fullmatch(email_pattern, new_email)):
                for i in user_list.user_list:
                    if i.get_email() != new_email:
                        pass
                    else:
                        return {"status" : "This email has been used"}
                self.__email = new_email
                return {"status" : "email successfully changed", "new email" : self.get_email()}
            else:
                return{"status" : "invalid email -> xxx@xxx.xxx"}
        else:
            return {"status" : "ERROR : incorrect password"}

    
class UserList:
    def __init__(self) -> None:
        self.user_list = []

    def add_user_to_list(self,User):
        self.user_list.append(User)

    # def check_password(self,mail,pw):
    #     for i in range (len(self.user_list)):
    #         user = self.user_list[i]
    #         if mail == user.get_email() and pw == user.get_password():
    #             return "Login Successful"
    #     return "Your password or username is not correct"
    