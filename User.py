class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password
    
    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password 
    
    def view_profile(self):
        return [self.__username, self.__email, self.__password]
    
    def view_receipt(self):
        pass

    def view_certificate(self):
        pass

