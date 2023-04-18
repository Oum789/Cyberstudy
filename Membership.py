class Membership():
    def __init__(self, tier, info):
        self.__tier = tier
        self.__info = info

    def get_tier(self):
        return self.__tier
    
    def get_info(self):
        return self.__info
    
    def view_membership(self):
        return {"Tier":self.__tier, "Info":self.__info}