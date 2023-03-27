from Course import CourseCatalog, Course, CourseBoughtCatalog
from User import User, UserList
from Payment import ShopCart

def main():
    user_list = UserList()
    catalog = CourseCatalog()
    cart = ShopCart(0)
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

    #searchCourse
    '''
    result = catalog.search_by_diff(66)
    if result == []:
        print("NOT FOUND")

    else :
        for i in range (len(result)):
            print(result[i].title)
    '''

    #login
    '''
    checkpass = user_list.check_password("a@gmail.com","amogus")
    print(checkpass)
    '''

    #payment
    '''
    cart.add_to_cart(catalog.course_list[2])
    cart.add_to_cart(catalog.course_list[0])
    check_money = cart.initiate_payment(1234)

    if check_money == 1:
        print("Payment Successful")
        course_bought.add_course_to_list(cart.get_buying_list(),user1.get_name())
    else:
        print("Payment Failed, Please try again")
    '''
main()