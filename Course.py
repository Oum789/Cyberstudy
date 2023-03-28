class Course:
    def __init__(self,diff,duration,genre,title,price,Teacher):
        self.__diff = diff
        self.__duration = duration
        self.__genre = genre
        self.__title = title
        self.__price = price
        self.__teacher = Teacher
    
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
        self.course_list = [] #list of course object

    def add_course_to_list(self,Course):
        self.course_list.append(Course)

    def remove_course_from_list(self,Course):
        self.course_list.remove(Course)

    def view_course(self,Course):
        return [Course.get_diff(), Course.get_duration(), Course.get_genre(),
                Course.get_title(), Course.get_price()]

    def view_teacher(self, Course):
        return [Course.get_teacher().get_teacher_name(),Course.get_teacher().get_bio()]