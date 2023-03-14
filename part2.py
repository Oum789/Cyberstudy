class Course:
    def __init__(self,course_pic,genre,course_name,price,promote,duration,difficulty,detail,course_doc,chapter_count,ex_cert,comments,teacher):
        self.course_pic = course_pic
        self.genre = genre
        self.course_name = course_name
        self.price = price
        self.promote = promote
        self.duration = duration
        self.difficulty = difficulty
        self.detail = detail
        self.course_doc = course_doc
        self.chapter_count = chapter_count
        self.ex_cert = ex_cert
        self.comments = [] #list of Comment Object
        self.teacher = teacher #Teacher Object
        
class Certificate:
    def __init__(self,day_finished,autograph,name,course_name):
        self.day_finished = day_finished
        self.autograph = autograph #Teacher Object
        self.name = name #User Object
        self.course_name = course_name #Course Object

class Comment:
    def __init__(self,comment,time_stamp,commentor):
        self.comment = comment
        self.time_stamp = time_stamp
        self.commentor = commentor #User Object