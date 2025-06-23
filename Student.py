class Student():
     def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
          self.__first_name = first_name
          self.__last_name = last_name
          self.__major = major
          self.__credit_hours = credit_hours
          self.__gpa = gpa
          self.__id_number = id_number
     
     def get_first_name(self):
          return self.__first_name
     def get_last_name(self):
          return self.__last_name
     def get_major(self):
          return self.__major
     def get_credit_hours(self):
          return self.__credit_hours
     def get_gpa(self):
          return self.__gpa
     def get_id_number(self):
          return self.__id_number
     def set_first_name(self, new_first_name:str):
          self.__first_name = new_first_name
     def set_last_name(self, new_last_name:str):
          self.__last_name = new_last_name
     def set_major(self, new_major:str):
          self.__major = new_major
     def set_credit_hours(self, new_credit_hours:int):
          self.__credit_hours = new_credit_hours
     def get_gpa(self, new_gpa:float):
          self.__gpa = new_gpa
     
     def get_class_level(self):

          if self.__credit_hours <= 30 and self.__credit_hours >= 0:
               return "Freshman"
          elif self.__credit_hours <= 60:
               return "Sophomore"
          elif self.__credit_hours <= 90:
               return "Junior"
          elif self.__credit_hours > 90:
               return "Senior"
     
     def update_credit_hours(self, additional_credit_hours:int):
          new_credit_hours += additional_credit_hours
     
     def print_student_data(self):
          print(f"{self.__first_name} {self.__last_name}\nClass Level: {self.get_class_level()} Major: {self.__major}\nGPA: {self.__gpa} Student ID: {self.__id_number}")
     
