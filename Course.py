class Course:
    def __init__(self,diff,duration,genre,title,price):
        self.__diff = diff
        self.__duration = duration
        self.__genre = genre
        self.__title = title
        self.__price = price
    
    def get_diff(self):
        return self.__diff
    
    def get_duration(self):
        return self.__duration
    
    def get_genre(self):
        return self.__genre
    
    def get_title(self):
        return self.__title
    
    def get_price(self):
        return self.__price

class CourseCatalog:
    def __init__(self):
        self.course_list = [] #list of course object

    def add_course_to_list(self,Course):
        self.course_list.append(Course)

    def search_by_diff(self,keyword):
        filtered_list = []
        for i in range (len(self.course_list)):
            if self.course_list[i].get_diff() == keyword:
                filtered_list.append(self.course_list[i])

        return filtered_list

    def search_by_duration(self,min,max):
        filtered_list = []
        for i in range (len(self.course_list)):
            if self.course_list[i].get_duration() >= min and self.course_list[i].get_duration() <= max:
                filtered_list.append(self.course_list[i])

        return filtered_list

    def search_by_genre(self,keyword):
        filtered_list = []
        for i in range (len(self.course_list)):
            if self.course_list[i].get_genre() == keyword:
                filtered_list.append(self.course_list[i])

        return filtered_list
        
    def search_by_title(self,keyword):
        filtered_list = []
        for i in range (len(self.course_list)):
            if self.course_list[i].get_title().find(keyword) > -1:
                filtered_list.append(self.course_list[i])

        return filtered_list
    
class CourseBought(Course):
    def __init__(self, expired_date, progress,course_owner,diff,duration,genre,title,price):
        Course.__init__(self,diff,duration,genre,title,price)
        self.__expired_date = expired_date
        self.__progress = progress
        self.__course_owner = course_owner

    def get_expired_date(self):
        return self.__expired_date
    
    def get_progress(self):
        return self.__progress
    
    def get_course_owner(self):
        return self.__course_owner

class CourseBoughtCatalog:
    def __init__(self):
        self.__course_owned = [] #list of CourseBought Object

    def add_course_to_list(self,Course,username):
        for i in range (len(Course)):
            Course[i] = CourseBought("expired_date",0,username,Course[i].get_diff(),Course[i].get_duration(),Course[i].get_genre(),Course[i].get_title(),Course[i].get_price())
            self.__course_owned.append(Course[i])

    def download_material():
        pass

    def activate_course():
        pass
            