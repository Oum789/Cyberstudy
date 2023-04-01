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
    
    