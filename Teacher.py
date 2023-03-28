class Teacher:
    def __init__(self,teacher_name,bio):
        self.__teacher_name = teacher_name
        self.__bio = bio

    def get_teacher_name(self):
        return self.__teacher_name
    
    def get_bio(self):
        return self.__bio