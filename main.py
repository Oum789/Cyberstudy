from Course import CourseCatalog, Course, CourseBoughtCatalog
from User import User, UserList
from Payment import ShopCart,Receipt

from fastapi import FastAPI,Body,Request,File,UploadFile,Form,status
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

'''def main():'''
templates = Jinja2Templates(directory='htmldirectory')

app = FastAPI()

user_list = UserList()
catalog = CourseCatalog()
cart = ShopCart(0)
course_bought = CourseBoughtCatalog()

login_status = 0
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

#Templates
@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html",context={"request": request})

@app.get("/search", response_class=HTMLResponse)
def search(request: Request):
    return templates.TemplateResponse("search.html",context={"request": request})

@app.get("/jail")
def jail(request: Request):  
    return templates.TemplateResponse('jail.html', context={'request': request})

@app.get("/home_page")
def home_page(request: Request):  
    return templates.TemplateResponse('home_page.html', context={'request': request})

@app.get("/payment")
def payment(request: Request):  
    return templates.TemplateResponse('payment.html', context={'request': request,"statuss":""})

@app.get("/admin")
def admin(request: Request):
    return templates.TemplateResponse("admin.html",context={"request": request,"status_add_course":"","status_remove_course":"","status_edit_course":""})

#Method Endpoints
@app.post("/course")
async def course(request: Request, ids : str = Form(None)):
    course = catalog.find_course(int(ids))
    diff = course.get_diff()
    duration = course.get_duration()
    genre = course.get_genre()
    title = course.get_title()
    price = course.get_price()
    id_dict = {0:ids}
    print(id_dict)
    return templates.TemplateResponse("view_course.html",context={"request": request,
                                                                  "cart_message":"",
                                                                  "diff":diff,
                                                                  "duration":duration,
                                                                  "genre":genre,
                                                                  "title":title,
                                                                  "price":price,
                                                                  "ids":id_dict})

@app.post("/course_guest")
async def course(request: Request, ids : str = Form(None)):
    course = catalog.find_course(int(ids))
    diff = course.get_diff()
    duration = course.get_duration()
    genre = course.get_genre()
    title = course.get_title()
    price = course.get_price()
    id_dict = {0:ids}
    print(id_dict)
    return templates.TemplateResponse("view_course_guest.html",context={"request": request,
                                                                  "cart_message":"",
                                                                  "diff":diff,
                                                                  "duration":duration,
                                                                  "genre":genre,
                                                                  "title":title,
                                                                  "price":price,
                                                                  "ids":id_dict})

@app.post("/add_to_cart")
def add_to_cart(request: Request, ids : str = Form(None)):
    course = catalog.find_course(int(ids))
    cart.add_to_cart(course)
    # print(cart.__buying_list)
    diff = course.get_diff()
    duration = course.get_duration()
    genre = course.get_genre()
    title = course.get_title()
    price = course.get_price()
    id_dict = {0:ids}
    print(id_dict)
    return templates.TemplateResponse("view_course.html",context={"request": request,
                                                                  "cart_message":"Added to cart",
                                                                  "diff":diff,
                                                                  "duration":duration,
                                                                  "genre":genre,
                                                                  "title":title,
                                                                  "price":price,
                                                                  "ids":id_dict})

@app.post("/checkpass")
async def login(request: Request, email : str = Form(None),password : str = Form(None)):
    statuss = user_list.check_password(email,password)  
    if statuss == 1:
        # return templates.TemplateResponse('home_page.html', context={'request': request, 'result': "Login Successful"})
        login_status = 1
        redirect_url = request.url_for('home_page')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    # "Login Successful"
    if statuss == 0:
        # return templates.TemplateResponse('jail.html', context={'request': request, 'result': "Your password or username is not correct"})
        redirect_url = request.url_for('jail')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    # "Your password or username is not correct"

@app.post('/back')
async def add(request: Request):
    redirect_url = request.url_for('login')    
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)

# return {"status":status}

# testcase login
# {"email":"qwertyuiop@gmail.com",
#  "password":"ASDFJKL"}


@app.post("/add_course")
async def add_course(request: Request, ids : str = Form(None),diff : str = Form(None),duration : str = Form(None),genre : str = Form(None),title : str = Form(None),price : str = Form(None)):
    if ids == None or diff == None or duration == None or genre == None or title == None or price == None:
        redirect_url = request.url_for('admin')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        check = catalog.admin_add_course_to_list(int(ids),diff,int(duration),genre,title,int(price))
        if check == 0:
            return templates.TemplateResponse("admin.html",context={"request": request,"status_add_course": "ID already taken"})
        else:
            return templates.TemplateResponse("admin.html",context={"request": request,"status_add_course": "Course Added"})

# testcase add_course
# {"id":123456,
#  "diff":2,
#  "duration":4.6,
#  "genre":"math",
#  "title":"Minecraft_Physics",
#  "price":5000}

@app.post("/remove_course")
async def remove_course(request: Request, ids : str = Form(None)):
    if ids == None:
        redirect_url = request.url_for('admin')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        course_selected = catalog.find_course(int(ids))
        if course_selected == 0:
            return templates.TemplateResponse("admin.html",context={"request": request,"status_remove_course": "ID not found"})
        else:
            catalog.remove_course_from_list(course_selected)
            return templates.TemplateResponse("admin.html",context={"request": request,"status_remove_course": "Course Removed"})
    # print(catalog.course_list[-1].get_title())

# testcase remove_course
# {"id":123456}

@app.post("/edit_course")
async def edit_course(request: Request, ids : str = Form(None),diff : str = Form(None),duration : str = Form(None),genre : str = Form(None),title : str = Form(None),price : str = Form(None)):
    if ids == None or diff == None or duration == None or genre == None or title == None or price == None:
        redirect_url = request.url_for('admin')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        check = catalog.edit_course_from_list(int(ids),diff,int(duration),genre,title,int(price))
        if check == 0:
            return templates.TemplateResponse("admin.html",context={"request": request,"status_edit_course": "ID not found"})
        else:
            return templates.TemplateResponse("admin.html",context={"request": request,"status_edit_course": "Course Editted"})

@app.get("/view_cart")
async def view_shopcart(request:Request):
    result = cart.view_cart()
    if result == {}:
        return {}
    else :
        return templates.TemplateResponse('after_search.html', context={'request': request, 'result': result})
    
@app.post("/search_title")
async def search_title(request:Request,keyword : str = Form(None)):
    if keyword == None:
        redirect_url = request.url_for('search')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        result = catalog.search_by_title(keyword)
        if result == {}:
            return {}
        else :
            return templates.TemplateResponse('after_search.html', context={'request': request, 'result': result})
    

# testcase search_title
# {"title":"A"}

@app.post("/search_diff")
async def search_diff(request:Request,diff : str = Form(None)):
    if diff == None:
        redirect_url = request.url_for('search')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        result = catalog.search_by_diff(int(diff))
        if result == {}:
            return {}
        else :
            return templates.TemplateResponse('after_search.html', context={'request': request, 'result': result})

# testcase search_diff
# {"diff":2}

@app.post("/search_genre")
async def search_genre(request:Request,genre : str = Form(None)):
    if genre == None:
        redirect_url = request.url_for('search')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        result = catalog.search_by_genre(genre)
        if result == {}:
            return {}
        else :
            return templates.TemplateResponse('after_search.html', context={'request': request, 'result': result})

# testcase search_genre
# {"genre":"science"}

@app.post("/search_duration")
async def search_duration(request:Request,duration_min : str = Form(None),duration_max : str = Form(None)):
    if duration_min == None or duration_max == None:
        redirect_url = request.url_for('search')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        result = catalog.search_by_duration(int(duration_min),int(duration_max))
        if result == {}:
            return {}
        else :
            return templates.TemplateResponse('after_search.html', context={'request': request, 'result': result})

# testcase search_duration
# {"min":1,
#  "max":4}

cart.add_to_cart(catalog.course_list[2])
cart.add_to_cart(catalog.course_list[3])
print(cart.get_total_price())

@app.post("/paying")
async def pay(request:Request,username : str = Form(None),money : str = Form(None)):
    if username == None or money == None:
        redirect_url = request.url_for('payment')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        total_price = cart.get_total_price()
        if int(money) == int(total_price) and user_list.find_user(username) != 0:
            user = user_list.find_user(username)
            course_bought.add_course_to_list(cart.get_buying_list(),user.get_name())
            receipt = Receipt("receipt_pic.png","order_date",1)
            user.add_receipt_to_list(receipt)
            cart.reset_buying_list()
            return templates.TemplateResponse('payment_status.html', context={'request': request, "statuss":"Successful"})
        else:
            return templates.TemplateResponse('payment.html', context={'request': request, "statuss":"Please insert correct amount of money and username"})
        
# testcase payment
# {"money":2234,
#  "username":"Rimi"}