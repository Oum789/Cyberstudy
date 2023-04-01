class Teacher:
    def __init__(self,teacher_name,bio,no_student_teached,course_teached):
        self.__teacher_name = teacher_name
        self.__bio = bio
        self.__no_student_teached = no_student_teached
        self.__course_teached = [] #list of Course Object
