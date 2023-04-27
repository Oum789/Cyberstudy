import json
import numpy as np
from Course import CourseCatalog, Course, CourseBoughtCatalog
from User import User, UserList
from Teacher import Teacher
from typing import Optional
from fastapi import FastAPI, Request, Form, status, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import re
from IPython.display import display
from PIL import Image, ImageDraw
import base64

app = FastAPI()

templates = Jinja2Templates(directory='templates')



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
    Bank = User(0, "Bank","qwertyuiop@gmail.com","ASDFJKL")
    user_list.add_user_to_list(Bank)

    Fubuki = User(0, "Fubuki","a@gmail.com","amogus")
    user_list.add_user_to_list(Fubuki)

    Rimi = User(0, "Rimi","iLoveShrek@gmail.com","passworD")
    user_list.add_user_to_list(Rimi)

    #init teacher
    Guys = Teacher("Guys","like to eat an noodles",1,course1)
    Floyd = Teacher("Floyd","wanna eat rabbit",1,course2)

    #add to CourseBoughtCatalog
    user1_course_bought.add_course_to_list([course1,course2],Bank)
    
    #present user
    user_now = Bank
    login_status = True
    profile_picture = None 

    @app.get("/home", response_class=HTMLResponse)
    async def home_tem(request: Request):    
        return templates.TemplateResponse("home.html", {"request": request, "username": user_now.get_name(), "login_status": login_status, "catalog": catalog.course_list})
    
    @app.post("/home", response_class=HTMLResponse)
    async def home(request: Request, ids : str = Form(None)):    
        return templates.TemplateResponse("view_course.html", {"request": request, "ids": ids})
    
    @app.get("/logout", response_class=HTMLResponse)
    async def logout(request: Request): 
        login_status = False
        return templates.TemplateResponse("home.html", {"request": request, "username": user_now.get_name(), "login_status": login_status})

    
    @app.get("/view_profile", response_class=HTMLResponse)
    async def view_profile_tem(request: Request):
        profile = user_now.view_profile()
        return templates.TemplateResponse("view_profile.html", {"request": request, "picture": profile["picture"], "name": profile["name"], "email": profile["email"], "password": profile["password"]})
    
    @app.get("/view_course_bought", response_class=HTMLResponse)
    async def view_course_bought_tem(request: Request):
        my_course = user1_course_bought.view_bought_course()
        return templates.TemplateResponse("view_course_bought.html", {"request": request, "my_course": my_course})
    
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
            user_now.change_picture(changed_picture)    
            return templates.TemplateResponse("change_picture.html", {"request": request, "picture": changed_picture, "status": "Your picture has been changed"})

    @app.get("/change_username", response_class=HTMLResponse)
    async def change_username_tem(request: Request):
        return templates.TemplateResponse("change_username.html", {"request": request})
    
    @app.post("/change_username", response_class=HTMLResponse)
    async def change_username(request: Request, new_username: str = Form(None), password: str = Form(None)):
        if new_username == None or password == None:
            return templates.TemplateResponse("change_username.html", {"request": request, "status": "ERROR : Please Input Your Data"})
        else:
            user_change_status = user_now.change_username(new_username, user_list, password)
            return templates.TemplateResponse("change_username.html", {"request": request, "status": user_change_status["status"]})

    @app.get("/change_email", response_class=HTMLResponse)
    async def change_email_tem(request: Request):
        return templates.TemplateResponse("change_email.html", {"request": request})
    
    @app.post("/change_email", response_class=HTMLResponse)
    async def change_email(request: Request, new_email: str = Form(None), password: str = Form(None)):
        if new_email == None or password == None:
            return templates.TemplateResponse("change_email.html", {"request": request, "status": "ERROR : Please Input Your Data"})
        else:
            email_change_status = user_now.change_email(new_email, user_list, password)
            return templates.TemplateResponse("change_email.html", {"request": request, "status": email_change_status["status"]})
    
    @app.get("/change_password", response_class=HTMLResponse)
    async def change_password_tem(request: Request):
        return templates.TemplateResponse("change_password.html", {"request": request})
    
    @app.post("/change_password", response_class=HTMLResponse)
    async def change_password(request: Request, old_password: str = Form(None), new_password: str = Form(None)):
        if old_password == None or new_password == None:
            return templates.TemplateResponse("change_password.html", {"request": request, "status": "ERROR : Please Input Your Data"})
        else:
            password_change_status = user_now.change_password(new_password, old_password)
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
        return templates.TemplateResponse("view_course.html",context={"request": request, "cart_message":"", "diff":diff, "duration":duration, "genre":genre, "title":title, "price":price, "ids":id_dict})
                                                                        
                                                                        
                                                                       
                                                                        
                                                                        
                                                                        
            
    
    
    # @app.get("/view_profile")
    # async def get_profile() -> dict:
    #     user1_profile = user1.view_profile()
    #     return user1_profile

    # @app.get("/view_course_bought")
    # async def get_course_bought() -> dict:
    #     user1_course = user1_course_bought.view_bought_course()
    #     return user1_course 

    # @app.post("/change_password")
    # async def change_password(data: dict) -> dict:
    #     old_password = data["old password"]
    #     new_password = data["new password"]
    #     pass_change_status = user_now.change_password(new_password, old_password)
    #     return pass_change_status
    
    # @app.post("/change_username")
    # async def change_username(data: dict) -> dict:
    #     new_username = data["new username"]
    #     password = data["password"]
    #     user_change_status = user_now.change_username(new_username,user_list,password)
    #     return user_change_status
    
    # @app.post("/change_email")
    # async def change_email(data: dict) -> dict:
    #     new_email = data["new email"]
    #     password = data["password"]
    #     user_email_status = user_now.change_email(new_email,user_list,password)
    #     return user_email_status

main()