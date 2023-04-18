class Course:
    def __init__(self,diff,duration,genre,title,price,teacher):
        self.__diff = diff
        self.__duration = duration
        self.__genre = genre
        self.__title = title
        self.__price = price
        self.__teacher = teacher

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
    
    def get_teacher(self):
        return self.__teacher

class CourseCatalog:
    def __init__(self):
        self.course_list = [] # list of course object

    def add_course_to_list(self,Course):
        self.course_list.append(Course)

    def remove_course_from_list(self,Course):
        self.course_list.remove(Course)

    def view_course(self, Course):
        return {"difficulty":Course.get_diff(), "duration":Course.get_duration(), 
                "genre":Course.get_genre(), "title":Course.get_title(), "price":Course.get_price(),
                "teacher":Course.get_teacher()}

    def view_teacher(self, Course):
        return {"Teacher Name":Course.get_teacher().get_teacher_name(), "Teacher Bio":Course.get_teacher().get_bio()}
    

class CourseBookmark:
    def __init__(self):
        self.bookmark_list = []
    
    def add_course_to_bookmark(self, Course, username):
        for i in range(len(Course)):
            self.bookmark_list.append({"difficulty":Course[i].get_diff(), "duration":Course[i].get_duration(), 
                "genre":Course[i].get_genre(), "title":Course[i].get_title(), "price":Course[i].get_price(),
                "teacher":Course[i].get_teacher()})
            # self.bookmark_list.append(Course[i])

    def remove_course_from_bookmark(self, Course):
        self.bookmark_list.remove(Course)

    def view_bookmark(self):
        self.bookmark_keys = []
        
        for i in range(len(self.bookmark_list)):
            self.bookmark_keys.append("bookmark%s" % str(i+1))

        bookmark_dict = dict(zip(self.bookmark_keys, self.bookmark_list))
        return bookmark_dict

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