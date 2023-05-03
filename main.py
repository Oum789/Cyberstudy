from Course import CourseCatalog, Course, CourseBoughtCatalog
from User import User, UserList,Admin
from Payment import ShopCart
from System import System
from fastapi import FastAPI, Request, Form, status, UploadFile
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

import base64

'''def main():'''
templates = Jinja2Templates(directory='htmldirectory')

app = FastAPI()

user_list = UserList()
catalog = CourseCatalog()
cart = ShopCart(0)
course_bought = CourseBoughtCatalog()

#init course
course1 = Course(177013,1,2.46,"business","AMOGUS",0,
                 "Teach you about how to be a successful imposter",
                 ["http://www.youtube.com/embed/NlOF03DUoWc",
                  "http://www.youtube.com/embed/WCGtg5JJjd0",
                  "http://www.youtube.com/embed/UPR0i498PxU"],
                  ["Not Watched","Not Watched","Not Watched"])
catalog.add_course_to_list(course1)

course2 = Course(555,1,3.18,"entertain","A",1000,
                 "English Alphabet but only the first one",
                 ["http://www.youtube.com/embed/UPR0i498PxU"],["Not Watched"])
catalog.add_course_to_list(course2)

course3 = Course(2000,1,1.12,"entertain","B",1234,
                 "Extension from A, now we learn about 2nd character",
                 [],[])
catalog.add_course_to_list(course3)

course4 = Course(1,2,4.13,"math","THIS_IS_NAME",1000,
                 "Q#(&T)*T#WYB*)OB T($*OL#QYTBBV$QWBO) (Math is hard but my pen is Harder)",
                 [],[])
catalog.add_course_to_list(course4)

course5 = Course(777,2,4.6,"science","GENSHIN_BAD",500,
                 "Go touch some grass idiot",
                 [],[])
catalog.add_course_to_list(course5)

#init user
user1 = User(0,"Bank","qwertyuiop@gmail.com","ASDFJKL")
user_list.add_user_to_list(user1)

user2 = User(0,"Fubuki","a@gmail.com","amogus")
user_list.add_user_to_list(user2)

user3 = User(0,"Rimi","iLoveShrek@gmail.com","passworD")
user_list.add_user_to_list(user3)

guest = User(0,"Guest","","")

ad = Admin(0,"Admin","b@gmail.com","a")

#System
system = System(guest,False,False)
profile_picture = None 

@app.get("/home", response_class=HTMLResponse)
async def home_tem(request: Request):    
    return templates.TemplateResponse("home.html", {"request": request, "username": system.get_user_now().get_name(),
                                                     "login_status": system.get_login_status(), "admin_status": system.get_admin_status(), "catalog": catalog.course_list})

@app.post("/home", response_class=HTMLResponse)
async def home(request: Request, ids : str = Form(None)): 
    if system.get_login_status():
        return_ids = ids
        if system.get_user_now().check_bookmark(return_ids) == 1:
            system.get_user_now().add_to_bookmark(catalog.find_course(int(ids)))
        return templates.TemplateResponse("home.html", {"request": request, "username": system.get_user_now().get_name(), "login_status": system.get_login_status(), "catalog": catalog.course_list, "ids": return_ids})
    else:
        redirect_url = request.url_for('login')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request): 
    system.set_login_status(False)
    system.set_admin_status(False)
    cart.reset_buying_list()
    return templates.TemplateResponse("home.html", {"request": request, "username": system.get_user_now().get_name(), "login_status": system.get_login_status(), "catalog": catalog.course_list})

@app.get("/view_profile", response_class=HTMLResponse)
async def view_profile_tem(request: Request):
    profile = system.get_user_now().view_profile()
    return templates.TemplateResponse("view_profile.html", {"request": request, "picture": profile["picture"], "name": profile["name"], "email": profile["email"], "password": profile["password"]})

@app.get("/view_course_bought", response_class=HTMLResponse)
async def view_course_bought_tem(request: Request):
    my_course = course_bought.view_bought_course(system.get_user_now().get_name())
    return templates.TemplateResponse("view_course_bought.html", {"request": request, "my_course": my_course})

@app.get("/view_receipt", response_class=HTMLResponse)
async def view_receipt_tem(request: Request):
    return templates.TemplateResponse("view_receipt.html",{"request": request, "receipt": system.get_user_now().get_receipt()})

@app.get("/view_certificate", response_class=HTMLResponse)
async def view_certificate_tem(request: Request):
    course_owned = course_bought.get_owned_list(system.get_user_now().get_name())
    return templates.TemplateResponse("view_certificate.html",{"request": request, "my_course": course_owned})

@app.get("/view_bookmark", response_class=HTMLResponse)
async def view_bookmark_tem(request: Request):
    bookmark = system.get_user_now().get_bookmark()
    return templates.TemplateResponse("view_bookmark.html", {"request": request, "bookmark": bookmark})

@app.post("/view_bookmark", response_class=HTMLResponse)
async def view_bookmark_delete(request: Request, ids: str = Form(None)):
    bookmark = system.get_user_now().get_bookmark()
    bookmark.remove(catalog.find_course(int(ids)))
    return templates.TemplateResponse("view_bookmark.html", {"request": request, "bookmark": bookmark})

@app.get("/change_picture", response_class=HTMLResponse)
async def change_picture_tem(request: Request):
    return templates.TemplateResponse("change_picture.html", {"request": request})

@app.post("/change_picture", response_class=HTMLResponse)
async def change_picture(request: Request, picture: UploadFile = Form(None)):
    if picture == None:    
        return templates.TemplateResponse("change_picture.html", {"request": request, "picture": changed_picture, "status": "Please Input Your Data"})
    else:    
        print(picture)
        try:
            contents = picture.file.read()
            with open("uploaded_" + picture.filename, "wb") as f:
                f.write(contents)
        except Exception:
                return {"message": "There was an error uploading the file"}
        finally:
            picture.file.close()
        
        changed_picture = base64.b64encode(contents).decode("utf-8")    
        system.get_user_now().change_picture(changed_picture)    
        return templates.TemplateResponse("change_picture.html", {"request": request, "picture": changed_picture, "status": "Your picture has been changed"})

@app.get("/change_username", response_class=HTMLResponse)
async def change_username_tem(request: Request):
    return templates.TemplateResponse("change_username.html", {"request": request})

@app.post("/change_username", response_class=HTMLResponse)
async def change_username(request: Request, new_username: str = Form(None), password: str = Form(None)):
    if new_username == None or password == None:
        return templates.TemplateResponse("change_username.html", {"request": request, "status": "ERROR : Please Input Your Data"})
    else:
        user_change_status = system.get_user_now().change_username(new_username, user_list, password)
        return templates.TemplateResponse("change_username.html", {"request": request, "status": user_change_status["status"]})

@app.get("/change_email", response_class=HTMLResponse)
async def change_email_tem(request: Request):
    return templates.TemplateResponse("change_email.html", {"request": request})

@app.post("/change_email", response_class=HTMLResponse)
async def change_email(request: Request, new_email: str = Form(None), password: str = Form(None)):
    if new_email == None or password == None:
        return templates.TemplateResponse("change_email.html", {"request": request, "status": "ERROR : Please Input Your Data"})
    else:
        email_change_status = system.get_user_now().change_email(new_email, user_list, password)
        return templates.TemplateResponse("change_email.html", {"request": request, "status": email_change_status["status"]})

@app.get("/change_password", response_class=HTMLResponse)
async def change_password_tem(request: Request):
    return templates.TemplateResponse("change_password.html", {"request": request})

@app.post("/change_password", response_class=HTMLResponse)
async def change_password(request: Request, old_password: str = Form(None), new_password: str = Form(None)):
    if old_password == None or new_password == None:
        return templates.TemplateResponse("change_password.html", {"request": request, "status": "ERROR : Please Input Your Data"})
    else:
        password_change_status = system.get_user_now().change_password(new_password, old_password)
        return templates.TemplateResponse("change_password.html", {"request": request, "status": password_change_status["status"]})

@app.get("/register", response_class=HTMLResponse)
async def register_tem(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, picture: UploadFile = Form(None), username: str = Form(None), email: str = Form(None), password: str = Form(None), con_password: str = Form(None)):
    if picture == None or username == None or email == None or password == None or con_password == None  :
        return templates.TemplateResponse("register.html", {"request": request, "status": "ERROR : Please Input Your Data"})
    else:
        try:
            contents = picture.file.read()
            with open("uploaded_" + picture.filename, "wb") as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            picture.file.close()
    
        profile_picture = base64.b64encode(contents).decode("utf-8")
        result = user_list.register(profile_picture, username, email, password, con_password)

        if result["status"] == "register successfully":
            redirect_url = request.url_for('login')
            return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
        else:
            return templates.TemplateResponse("register.html", {"request": request, "status": result["status"]})


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
    detail = course.get_detail()
    id_dict = {0:ids}
    print(id_dict)
    if system.get_login_status() == True:
        return templates.TemplateResponse("view_course.html",context={"request": request,
                                                                  "cart_message":"",
                                                                  "diff":diff,
                                                                  "duration":duration,
                                                                  "genre":genre,
                                                                  "title":title,
                                                                  "price":price,
                                                                  "detail":detail,
                                                                  "ids":id_dict})
    else:
       return templates.TemplateResponse("view_course_guest.html",context={"request": request,
                                                                  "cart_message":"",
                                                                  "diff":diff,
                                                                  "duration":duration,
                                                                  "genre":genre,
                                                                  "title":title,
                                                                  "price":price,
                                                                  "detail":detail,
                                                                  "ids":id_dict})

@app.post("/add_to_cart")
def add_to_cart(request: Request, ids : str = Form(None)):
    course = catalog.find_course(int(ids))
    check2 = cart.check_ids(ids)
    check = course_bought.check_course_bought(system.get_user_now().get_name(),ids)
    print(check)
    if check == 0 or check2 == 0:
        diff = course.get_diff()
        duration = course.get_duration()
        genre = course.get_genre()
        title = course.get_title()
        price = course.get_price()
        detail = course.get_detail()
        id_dict = {0:ids}
        return templates.TemplateResponse("view_course.html",context={"request": request,
                                                                  "cart_message":"Course Already Added",
                                                                  "diff":diff,
                                                                  "duration":duration,
                                                                  "genre":genre,
                                                                  "title":title,
                                                                  "price":price,
                                                                  "detail":detail,
                                                                  "ids":id_dict})
    else:
        cart.add_to_buying_list(course)
        # print(cart.__buying_list)
        diff = course.get_diff()
        duration = course.get_duration()
        genre = course.get_genre()
        title = course.get_title()
        price = course.get_price()
        detail = course.get_detail()
        id_dict = {0:ids}
        print(id_dict)
        return templates.TemplateResponse("view_course.html",context={"request": request,
                                                                  "cart_message":"Added to cart",
                                                                  "diff":diff,
                                                                  "duration":duration,
                                                                  "genre":genre,
                                                                  "title":title,
                                                                  "price":price,
                                                                  "detail":detail,
                                                                  "ids":id_dict})
    
@app.post("/clear_cart")
def clear_cart(request : Request):
    result = cart.reset_buying_list()
    return templates.TemplateResponse("shopcart.html", {"request":request, "result":result, "price": cart.get_total_price()})

@app.post("/checkpass")
async def login(request: Request, email : str = Form(None),password : str = Form(None)):
    user = user_list.check_password(email,password)
    admins = ad.check_pass(email,password) 
    if admins == 1:
        system.set_login_status(True)
        system.set_admin_status(True)        
        system.set_user_now(ad)
        redirect_url = request.url_for('home')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    elif user == 0:
        redirect_url = request.url_for('jail')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        system.set_login_status(True)
        system.set_user_now(user)
        redirect_url = request.url_for('home')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)


@app.post('/back')
async def add(request: Request):
    redirect_url = request.url_for('login')    
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)

# return {"status":status}

# testcase login
# {"email":"qwertyuiop@gmail.com",
#  "password":"ASDFJKL"}


@app.post("/add_course")
async def add_course(request: Request, ids : str = Form(None),diff : str = Form(None),duration : str = Form(None),
                     genre : str = Form(None),title : str = Form(None),price : str = Form(None),detail: str = Form(None),
                     video : str = Form(None)):
    if ids == None or diff == None or duration == None or genre == None or title == None or price == None or detail == None or video == None:
        redirect_url = request.url_for('admin')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        video_list = video.split(",")
        statuss = []
        for i in range(len(video_list)):
            statuss.append("Not Watched")
        check = catalog.admin_add_course_to_list(int(ids),diff,int(duration),genre,title,int(price),detail,video_list,statuss)
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
async def edit_course(request: Request, ids : str = Form(None),diff : str = Form(None),duration : str = Form(None),
                     genre : str = Form(None),title : str = Form(None),price : str = Form(None),detail: str = Form(None),
                     video : str = Form(None)):
    if ids == None or diff == None or duration == None or genre == None or title == None or price == None or detail == None or video == None:
        redirect_url = request.url_for('admin')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        video_list = video.split(",")
        statuss = []
        for i in range(len(video_list)):
            statuss.append("Not Watched")
        check = catalog.edit_course_from_list(int(ids),diff,int(duration),genre,title,int(price),detail,video,statuss)
        if check == 0:
            return templates.TemplateResponse("admin.html",context={"request": request,"status_edit_course": "ID not found"})
        else:
            return templates.TemplateResponse("admin.html",context={"request": request,"status_edit_course": "Course Editted"})

@app.get("/view_cart")
async def view_shopcart(request:Request):
    result = cart.view_cart()
    price = cart.get_total_price()
    return templates.TemplateResponse('shopcart.html', context={'request': request, 'result': result,'price':price})
        
@app.post("/search_title")
async def search_title(request:Request,keyword : str = Form(None)):
    if keyword == None:
        redirect_url = request.url_for('search')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        result = catalog.search_by_title(keyword)
        if result == {}:
            return templates.TemplateResponse('search_not_found.html', context={'request': request})
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
            return templates.TemplateResponse('search_not_found.html', context={'request': request})
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
            return templates.TemplateResponse('search_not_found.html', context={'request': request})
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
            return templates.TemplateResponse('search_not_found.html', context={'request': request})
        else :
            return templates.TemplateResponse('after_search.html', context={'request': request, 'result': result})

# testcase search_duration
# {"min":1,
#  "max":4}

@app.post("/paying")
async def pay(request:Request,username : str = Form(None),money : str = Form(None)):
    if username == None or money == None:
        redirect_url = request.url_for('payment')
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    else:
        total_price = cart.get_total_price()
        if int(money) == int(total_price) and user_list.find_user(username) != 0:
            user = user_list.find_user(username)
            receipt = system.get_user_now().make_receipt(cart.get_buying_list(), cart.get_total_price())
            system.get_user_now().add_receipt_to_list(receipt)
            course_bought.add_course_to_list(cart.get_buying_list(),user.get_name())
            cart.reset_buying_list()
            return templates.TemplateResponse('payment_status.html', context={'request': request, "statuss":"Successful", "receipt": receipt})
        else:
            return templates.TemplateResponse('payment.html', context={'request': request, "statuss":"Please insert correct amount of money and username"})
        
# testcase payment
# {"money":2234,
#  "username":"Rimi"}
        
    
@app.post("/study")
def study(request:Request, ids : str = Form(None)):
    course = course_bought.find_course(system.get_user_now().get_name(),ids)
    video = course.get_video()
    statuss = course.get_status()
    length = len(video)
    progress = course.get_progress()
    return templates.TemplateResponse('study.html', context={'request': request,"video":video,"statuss":statuss,"ids" : ids,"length":length,"progress":progress})

@app.post("/show_vid")
def show_vid(request:Request, videos : str = Form(None)):
    data = videos.split(",")
    video = data[0] #0 = url/ 1 = position/ 2 = id
    course = course_bought.find_course(system.get_user_now().get_name(),data[2])
    course.set_status_from_position(int(data[1]),"Watched")
    course.update_progress()
    return templates.TemplateResponse('show_vid.html', context={'request': request,"videos":video})