class Teacher:
    def __init__(self,teacher_pic,teacher_name,bio,highlight,teacher_autograph,no_student_teached,course_teached):
        self.teacher_pic = teacher_pic
        self.teacher_name = teacher_name
        self.bio = bio
        self.highlight = highlight
        self.teacher_autograph = teacher_autograph
        self.no_student_teached = no_student_teached
        self.course_teached = [] #list of Course Object

class CourseProgress:
    def init(self, expired_date, progress,course):
        self.expired_date = expired_date
        self.progress = progress
        self.course = [] #list of Course Object

class User:
    def init(self, profile_pic, name , email, password, interest,certificate,course_prog,receipt,mem_tier):
        self.profile_pic = profile_pic
        self.name = name
        self.email = email
        self.password = password
        self.interest = interest
        self.certificate = [] #list of Certificate Object
        self.course_prog = [] #list of CourseProgress Object
        self.receipt = [] #list of Receipt Object
        self.mem_tier = mem_tier #Membership Object

class Membership:
    def init(self, start_date, expired_date, tier):
        self.start_date = start_date
        self.expired_date = expired_date
        self.tier = tier


        