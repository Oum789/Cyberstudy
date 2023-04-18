from Course import CourseBookmark, CourseCatalog, Course
from Teacher import Teacher
from Membership import Membership
from User import User
from fastapi import FastAPI

app = FastAPI()

catalog = CourseCatalog()

user1_bookmark = CourseBookmark()

# init teacher
teacher1 = Teacher("AMONG","Very good at sleeping")
teacher2 = Teacher("GUS","i love cat")

# init user
user1 = User("Finn", "funnyfin@gmail.com", "12345678")
user2 = User("Arm", "9arm888@gmail.com", "87654321")

# init membership
member1 = Membership("Bronze", "can fly")
member2 = Membership("Silver", "can teleport")

# init course amd add course
course1 = Course(1,2.46,"business","AMOGUS",0,teacher1)
catalog.add_course_to_list(course1)

course2 = Course(1,3.18,"entertain","A",1000,teacher2)
catalog.add_course_to_list(course2)

course3 = Course(1,1.12,"entertain","B",1234,teacher2)
catalog.add_course_to_list(course3)

course4 = Course(2,4.13,"math","THIS_IS_NAME",1000,teacher1)
catalog.add_course_to_list(course4)

course5 = Course(2,4.6,"science","GENSHIN_BAD",500,teacher2)
catalog.add_course_to_list(course5)

# add to bookmark
user1_bookmark.add_course_to_bookmark([course1,course2],user1)

# view course (like click on catalog page)
# result = catalog.view_course(catalog.course_list[2])
# print("view couse :", result)
@app.get("/view_course")
async def view_course() -> dict:
    return catalog.view_course(catalog.course_list[2])

# view techer
# result = catalog.view_teacher(catalog.course_list[2])
# print("view teacher :", result)
@app.get("/view_teacher")
async def view_teacher() -> dict:
    return catalog.view_teacher(catalog.course_list[2])

# view membership <-- button instead
# result = member1.view_membership()
# print("view membership :", result)
@app.get("/view_membership")
async def view_membership() -> dict:
    return member1.view_membership()

# view all user1 bookmarked
@app.get("/view_bookmark")
async def view_bookmark() -> dict:
    show_bookmark = user1_bookmark.view_bookmark()
    return show_bookmark

# view receipt
# result = 1
# print("view receipt :", result)


        

