import json
from Course import CourseCatalog, Course, CourseBoughtCatalog
from User import User, UserList
from Teacher import Teacher
from typing import Optional
from fastapi import FastAPI

app = FastAPI()




def main():
    user_list = UserList()
    catalog = CourseCatalog()
    user1_course_bought = CourseBoughtCatalog()

    #init course
    course1 = Course(177013,1,2.46,"business","AMOGUS",0)
    catalog.add_course_to_list(course1)

    course2 = Course(555,1,3.18,"entertain","A",1000)
    catalog.add_course_to_list(course2)

    course3 = Course(2000,1,1.12,"entertain","B",1234)
    catalog.add_course_to_list(course3)

    course4 = Course(1,2,4.13,"math","THIS_IS_NAME",1000)
    catalog.add_course_to_list(course4)

    course5 = Course(777,2,4.6,"science","GENSHIN_BAD",500)
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
    user1_course_bought.add_course_to_list([course1,course2],user1)
    
    #present user
    user_now = user1

    @app.get("/viewed_profile")
    async def get_profile() -> dict:
        user1_profile = user1.view_profile()
        return user1_profile
    
    @app.get("/viewed_course_bought")
    async def get_course_bought() -> dict:
        user1_course = user1_course_bought.view_bought_course()
        return user1_course

    @app.post("/change_password")
    async def change_password(data: dict) -> dict:
        old_password = data["old password"]
        new_password = data["new password"]
        pass_change_status = user_now.change_password(new_password, old_password)
        return pass_change_status
    
    @app.post("/change_username")
    async def change_username(data: dict) -> dict:
        new_username = data["new username"]
        password = data["password"]
        user_change_status = user_now.change_username(new_username,user_list,password)
        return user_change_status
    
    @app.post("/change_email")
    async def change_email(data: dict) -> dict:
        new_email = data["new email"]
        password = data["password"]
        user_email_status = user_now.change_email(new_email,user_list,password)
        return user_email_status

        

        

    #view profile 
    #viewed_profile = user1.view_profile()
    #print(viewed_profile)

    # #view CourseBought
    # viewd_course_bought = user1_course_bought.view_bought_course()
    # print(viewd_course_bought)




    # user_change_status = user1.change_username("jew",user_list,"ASDFJKL")
    # print(user_change_status)





main()