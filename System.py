class System:
    def __init__(self,user_now,login_status,admin_status):
        self.__user_now = user_now
        self.__login_status = login_status
        self.__admin_status = admin_status

    def get_user_now(self):
        return self.__user_now
    
    def get_login_status(self):
        return self.__login_status
    
    def get_admin_status(self):
        return self.__admin_status

    def set_user_now(self,user):
        self.__user_now = user

    def set_login_status(self,status):
        self.__login_status = status

    def set_admin_status(self,status):
        self.__admin_status = status
