class Course:
    def __init__(self,ids,diff,duration,genre,title,price,detail):
        self.__id = ids
        self.__diff = diff
        self.__duration = duration
        self.__genre = genre
        self.__title = title
        self.__price = price
        self.__detail = detail
    
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

    def admin_add_course_to_list(self,ids,diff,duration,genre,title,price):
        checking = self.find_course(ids)
        if checking == 0:
            newcourse = Course(int(ids),int(diff),int(duration),genre,title,int(price))
            self.course_list.append(newcourse)
            return 1
        else:
            return 0
    
    def add_course_to_list(self,course):
        self.course_list.append(course)

    def remove_course_from_list(self,course):
        self.course_list.remove(course)

    def edit_course_from_list(self,ids,diff,duration,genre,title,price):
        old_course_info = self.find_course(ids)
        if old_course_info == 0:
            return 0
        else:
            old_course_info.set_diff(diff)
            old_course_info.set_duration(duration)
            old_course_info.set_genre(genre)
            old_course_info.set_title(title)
            old_course_info.set_price(price)
            return 1

    def find_course(self,id):
        for i in self.course_list:
            if i.get_id() == id:
                return i
        return 0

    def search_by_diff(self,keyword):
        counter = 0
        filtered_dict = {}
        for i in range (len(self.course_list)):
            if self.course_list[i].get_diff() == keyword:
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
    
    def edit_course(self,edit_type,data,Course):
        match edit_type:
            case "diff" :
                Course.set_diff(data)
            case "duration" :
                Course.set_duration(data)
            case "genre" :
                Course.set_genre(data)
            case "title" :
                Course.set_title(data)
            case "price" :
                Course.set_price(data)
            case _:
                print("No type matched - pls try again")
    
class CourseBought(Course):
    def __init__(self, expired_date, progress,course_owner,ids,diff,duration,genre,title,price,detail):
        Course.__init__(self,ids,diff,duration,genre,title,price,detail)
        self.__expired_date = expired_date
        self.__progress = progress
        self.__course_owner = course_owner


    def get_expired_date(self):
        return self.__expired_date
    
    def get_progress(self):
        return self.__progress
    
    def get_course_owner(self):
        return self.__course_owner

class CourseBoughtCatalog:
    def __init__(self):
        self.__course_owned = [] #list of CourseBought Object

    def add_course_to_list(self,course,username):
        for i in range (len(course)):
            course[i] = CourseBought("expired_date",0,username,course[i].get_id(),course[i].get_diff(), course[i].get_duration(), course[i].get_genre(), course[i].get_title(), course[i].get_price(), course[i].get_detail())
            self.__course_owned.append(course[i])
            print("added")
        
    def check_ids(self,id):
        for i in self.__course_owned:
            if i.get_id() == int(id):
                return 0
        return 1

    def get_list(self):
        return self.__course_owned

    def download_material():
        pass

    def activate_course():
        pass
        
    def view_bought_course(self):
        my_course = {}
        i = 1   
        for j in self.__course_owned:
            my_dict = {}
            my_dict["name"] = j.get_title()
            my_dict["exp"] = j.get_expired_date()
            my_dict["progress"] = j.get_progress()
            my_dict["owner"] = j.get_course_owner()
            my_course[i] = my_dict
            i = i + 1
        return my_course