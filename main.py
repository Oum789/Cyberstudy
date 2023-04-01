from Course import CourseCatalog, Course, CourseBoughtCatalog
from User import User, UserList
from Teacher import Teacher

def main():
    user_list = UserList()
    catalog = CourseCatalog()
    course_bought = CourseBoughtCatalog()

    #init course
    course1 = Course(1,2.46,"business","AMOGUS",0)
    catalog.add_course_to_list(course1)

    course2 = Course(1,3.18,"entertain","A",1000)
    catalog.add_course_to_list(course2)

    course3 = Course(1,1.12,"entertain","B",1234)
    catalog.add_course_to_list(course3)

    course4 = Course(2,4.13,"math","THIS_IS_NAME",1000)
    catalog.add_course_to_list(course4)

    course5 = Course(2,4.6,"science","GENSHIN_BAD",500)
    catalog.add_course_to_list(course5)

    #init user
    user1 = User("Bank","qwertyuiop@gmail.com","ASDFJKL")
    user_list.add_user_to_list(user1)

    user2 = User("Fubuki","a@gmail.com","amogus")
    user_list.add_user_to_list(user2)

    user3 = User("Rimi","iLoveShrek@gmail.com","passworD")
    user_list.add_user_to_list(user3)

    #init teacher
    Guys = Teacher("Guys","like to eat an noodles",1,course1)
    Floyd = Teacher("Floyd","wanna eat rabbit",1,course2)

    #add to CourseBoughtCatalog
    course_bought.add_course_to_list([course1,course2],user1)

    #view profile 
    viewed_profile = user1.view_profile()
    print(viewed_profile)

    #view CourseBought
    viewd_course_bought = course_bought.view_bought_course()
    print(viewd_course_bought)

main()