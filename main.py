from Course import CourseCatalog, Course, CourseBoughtCatalog
from User import User, UserList
from Payment import ShopCart,Receipt

from fastapi import FastAPI

'''def main():'''

app = FastAPI()

user_list = UserList()
catalog = CourseCatalog()
cart = ShopCart(0)
course_bought = CourseBoughtCatalog()

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

#searchCourse
# result = catalog.search_by_title("A")
# if result == []:
#     print("NOT FOUND")
# else :
#     print(result)

# #login
# def login(email,password):
#     status = user_list.check_password(email,password)
#     print(status)

# #payment
# cart.add_to_cart(catalog.course_list[2])
# cart.add_to_cart(catalog.course_list[3])
# check_money = cart.initiate_payment(2234)

# if check_money == 1:
#     print("Payment Successful")
#     course_bought.add_course_to_list(cart.get_buying_list(),user1.get_name())
#     receipt = Receipt("receipt_pic.png","order_date",1)
#     user1.add_receipt_to_list(receipt)
# else:
#     print("Payment Failed, Please try again")

# #addcourse
# newcourse = Course(2,4.6,"math","Minecraft_Physics",5000)
# catalog.add_course_to_list(newcourse)

# #editcourse
# catalog.edit_course("genre","science",catalog.course_list[-1])
# print(catalog.course_list[-1].get_genre())

# #removecourse
# for i in range (len(catalog.course_list)):
#     print(catalog.course_list[i].get_title())
# print("agsasgasg")
# catalog.remove_course_from_list(catalog.course_list[2])
# for i in range (len(catalog.course_list)):
#     print(catalog.course_list[i].get_title())

@app.post("/login")
async def login(data: dict) -> dict:
    email = data["email"]
    password = data["password"]
    status = user_list.check_password(email,password)
    return {"status":status}

# testcase login
# {"email":"qwertyuiop@gmail.com",
#  "password":"ASDFJKL"}


@app.post("/add_course")
async def add_course(data: dict) -> dict:
    ids = data["id"]
    diff = data["diff"]
    duration = data["duration"]
    genre = data["genre"]
    title = data["title"]
    price = data["price"]
    newcourse = Course(ids,diff,duration,genre,title,price)
    catalog.add_course_to_list(newcourse)
    # print(catalog.course_list[-1].get_title())
    return {"status": "Course_Added"}

# testcase add_course
# {"id":123456,
#  "diff":2,
#  "duration":4.6,
#  "genre":"math",
#  "title":"Minecraft_Physics",
#  "price":5000}

@app.post("/remove_course")
async def remove_course(data: dict) -> dict:
    ids = data["id"]
    course_selected = catalog.find_course(ids)
    if course_selected == 0:
        status = "Course_id_not_found"
    else:
        catalog.remove_course_from_list(course_selected)
        status = "Course_removed"
    
    # print(catalog.course_list[-1].get_title())
    return {"status":status}

# testcase remove_course
# {"id":123456}

@app.post("/search_title")
async def search_title(data: dict) -> dict:
    title = data["title"]
    result = catalog.search_by_title(title)
    if result == {}:
        return {"status":"NOT FOUND"}
    else :
        return result

# testcase search_title
# {"title":"A"}

@app.post("/search_diff")
async def search_diff(data: dict) -> dict:
    diff = data["diff"]
    result = catalog.search_by_diff(diff)
    if result == {}:
        return {"status":"NOT FOUND"}
    else :
        return result

# testcase search_diff
# {"diff":2}

@app.post("/search_genre")
async def search_genre(data: dict) -> dict:
    genre = data["genre"]
    result = catalog.search_by_genre(genre)
    if result == {}:
        return {"status":"NOT FOUND"}
    else :
        return result

# testcase search_genre
# {"genre":"science"}

@app.post("/search_duration")
async def search_duration(data: dict) -> dict:
    duration_min = data["min"]
    duration_max = data["max"]
    result = catalog.search_by_duration(duration_min,duration_max)
    if result == {}:
        return {"status":"NOT FOUND"}
    else :
        return result

# testcase search_duration
# {"min":1,
#  "max":4}

cart.add_to_cart(catalog.course_list[2])
cart.add_to_cart(catalog.course_list[3])

@app.post("/payment")
async def pay(data:dict) -> dict:
    money = data["money"]
    username = data["username"]
    total_price = cart.get_total_price()
    if money == total_price:
        user = user_list.find_user(username)
        course_bought.add_course_to_list(cart.get_buying_list(),user.get_name())
        receipt = Receipt("receipt_pic.png","order_date",1)
        user.add_receipt_to_list(receipt)
        print(user.get_receipt())
        print(course_bought.get_list())
        cart.reset_buying_list()
        return {"status":"Payment Complete"}
    else:
        return {"status":"Payment Failed"}

# testcase payment    
# {"money":2234,
#  "username":"Rimi"}