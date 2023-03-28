from Course import CourseCatalog, Course
from Teacher import Teacher
from Membership import Membership

def main():
    catalog = CourseCatalog()

    #init teacher
    teacher1 = Teacher("AMONG","Very good at sleeping")
    teacher2 = Teacher("GUS","i love cat")

    # init membership
    member1 = Membership("Bronze", "can fly")
    member2 = Membership("Silver", "can teleport")

    #init course
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

    # viewcourse
    result = catalog.view_course(catalog.course_list[2])
    print(result)

    #view techer
    result = catalog.view_teacher(catalog.course_list[2])
    print(result)

    # view membership <-- button instead
    result = member1.view_membership()
    print(result)
        
main()
