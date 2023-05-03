class Course:
    def __init__(self,ids,diff,duration,genre,title,price,detail,video,status_list):
        self.__id = ids
        self.__diff = diff
        self.__duration = duration
        self.__genre = genre
        self.__title = title
        self.__price = price
        self.__detail = detail
        self.__video = video
        self.__status_list = status_list
    
    def get_id(self):
        return self.__id

    def get_diff(self):
        return self.__diff
    
    def get_duration(self):
        return self.__duration
    
    def get_genre(self):
        return self.__genre
    
    def get_title(self):
        return self.__title
    
    def get_price(self):
        return self.__price
    
    def get_detail(self):
        return self.__detail
    
    def get_video(self):
        return self.__video
    
    def get_status(self):
        return self.__status_list
    
    def set_status_from_position(self,position,status):
        self.__status_list[position] = status

    def set_statuss(self,statuss):
        self.__status_list = statuss

    def set_video(self,video):
        self.__video = video
    
    def set_diff(self, diff):
        self.__diff = diff

    def set_duration(self, duration):
        self.__duration = duration
    
    def set_genre(self, genre):
        self.__genre = genre

    def set_title(self, title):
        self.__title = title

    def set_price(self, price):
        self.__price = price

    def set_detail(self,detail):
        self.__detail = detail

class CourseCatalog:
    def __init__(self):
        self.course_list = [] #list of course object

    def admin_add_course_to_list(self,ids,diff,duration,genre,title,price,detail,video,statuss):
        checking = self.find_course(ids)
        if checking == 0:
            newcourse = Course(int(ids),int(diff),int(duration),genre,title,int(price),detail,video,statuss)
            self.course_list.append(newcourse)
            return 1
        else:
            return 0
    
    def add_course_to_list(self,course):
        self.course_list.append(course)

    def remove_course_from_list(self,course):
        self.course_list.remove(course)

    def edit_course_from_list(self,ids,diff,duration,genre,title,price,detail,video,statuss):
        old_course_info = self.find_course(ids)
        if old_course_info == 0:
            return 0
        else:
            old_course_info.set_diff(diff)
            old_course_info.set_duration(duration)
            old_course_info.set_genre(genre)
            old_course_info.set_title(title)
            old_course_info.set_price(price)
            old_course_info.set_detail(detail)
            old_course_info.set_video(video)
            old_course_info.set_statuss(statuss)

            return 1

    def find_course(self,id):
        for i in self.course_list:
            if i.get_id() == id:
                return i
        return 0

    def search_by_diff(self,diff):
        counter = 0
        filtered_dict = {}
        for i in range (len(self.course_list)):
            if self.course_list[i].get_diff() == diff:
                course_dict = {}
                course_dict["title"] = self.course_list[i].get_title()
                course_dict["genre"] = self.course_list[i].get_genre()
                course_dict["difficulty"] = self.course_list[i].get_diff()
                course_dict["duration"] = self.course_list[i].get_duration()
                course_dict["price"] = self.course_list[i].get_price()
                course_dict["id"] = self.course_list[i].get_id()
                filtered_dict[counter] = course_dict
                counter+=1

        return filtered_dict

    def search_by_duration(self,min,max):
        counter = 0
        filtered_dict = {}
        for i in range (len(self.course_list)):
            if self.course_list[i].get_duration() >= min and self.course_list[i].get_duration() <= max:
                course_dict = {}
                course_dict["title"] = self.course_list[i].get_title()
                course_dict["genre"] = self.course_list[i].get_genre()
                course_dict["difficulty"] = self.course_list[i].get_diff()
                course_dict["duration"] = self.course_list[i].get_duration()
                course_dict["price"] = self.course_list[i].get_price()
                course_dict["id"] = self.course_list[i].get_id()
                filtered_dict[counter] = course_dict
                counter+=1

        return filtered_dict

    def search_by_genre(self,keyword):
        counter = 0
        filtered_dict = {}
        for i in range (len(self.course_list)):
            if self.course_list[i].get_genre() == keyword:
                course_dict = {}
                course_dict["title"] = self.course_list[i].get_title()
                course_dict["genre"] = self.course_list[i].get_genre()
                course_dict["difficulty"] = self.course_list[i].get_diff()
                course_dict["duration"] = self.course_list[i].get_duration()
                course_dict["price"] = self.course_list[i].get_price()
                course_dict["id"] = self.course_list[i].get_id()
                filtered_dict[counter] = course_dict
                counter+=1

        return filtered_dict
        
    def search_by_title(self,keyword):
        counter = 0
        filtered_dict = {}
        for i in range (len(self.course_list)):
            if self.course_list[i].get_title().find(keyword) > -1:
                course_dict = {}
                course_dict["title"] = self.course_list[i].get_title()
                course_dict["genre"] = self.course_list[i].get_genre()
                course_dict["difficulty"] = self.course_list[i].get_diff()
                course_dict["duration"] = self.course_list[i].get_duration()
                course_dict["price"] = self.course_list[i].get_price()
                course_dict["id"] = self.course_list[i].get_id()
                filtered_dict[counter] = course_dict
                counter+=1

        return filtered_dict
class CourseBought(Course):
    def __init__(self, expired_date, progress,course_owner,ids,diff,duration,genre,title,price,detail,video,status_list):
        Course.__init__(self,ids,diff,duration,genre,title,price,detail,video,status_list)
        self.__expired_date = expired_date
        self.__progress = progress
        self.__course_owner = course_owner
        self.__finished = False

    def get_expired_date(self):
        return self.__expired_date
    
    def get_progress(self):
        return self.__progress
    
    def get_finished(self):
        return self.__finished
    
    def set_course_owner(self, username):
        self.__course_owner = username
    
    def update_progress(self):
        watched = 0
        for i in self.get_status():
            if i == "Watched":
                watched +=1
        notwatched = len(self.get_video())
        if self.__finished != 100:
            self.__progress = watched/notwatched *100
        if self.__progress == 100 and self.__finished == False:
            self.__finished = True

    def get_course_owner(self):
        return self.__course_owner

class CourseBoughtCatalog:
    def __init__(self):
        self.__course_owned = [] #list of CourseBought Object

    def add_course_to_list(self,course,username):
        for i in range (len(course)):
            course[i] = CourseBought("expired_date",0,username,
                                     course[i].get_id(),course[i].get_diff(),course[i].get_duration(), course[i].get_genre(),
                                     course[i].get_title(),course[i].get_price(), course[i].get_detail(),course[i].get_video(),course[i].get_status())
            self.__course_owned.append(course[i])
        
    def find_course(self,username,ids):
        for i in self.__course_owned:
            if i.get_course_owner() == username:
                if i.get_id() == int(ids):
                    return i
        return 0
    
    def change_owner(self,username,new_username):
        for i in self.__course_owned:
            if i.get_course_owner() == username:
                i.set_course_owner(new_username)
    
    def check_course_bought(self,username,ids):
        for i in self.__course_owned:
            if i.get_course_owner() == username:
                if i.get_id() == int(ids):
                    return 0
        return 1

    def check_ids(self,id):
        for i in self.__course_owned:
            if i.get_id() == int(id):
                return 0
        return 1

    def get_list(self):
        return self.__course_owned
    
    def get_owned_list(self,username):
        result = []
        for i in self.__course_owned:
            if i.get_course_owner() == username:
                result.append(i)
        if result == []:
            return []
        return result
        

    def view_bought_course(self,user_now):
        my_course = {}
        i = 1   
        for j in self.__course_owned:
            if j.get_course_owner() == user_now:
                my_dict = {}
                my_dict["name"] = j.get_title()
                my_dict["exp"] = j.get_expired_date()
                my_dict["progress"] = j.get_progress()
                my_dict["owner"] = j.get_course_owner()
                my_dict["ids"] = j.get_id()      
                my_course[i] = my_dict
                i = i + 1
        return my_course