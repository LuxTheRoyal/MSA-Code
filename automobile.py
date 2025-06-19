import datetime
class Automobile():
     # For any class we want to define a constructer. 
     # The constructer defines what happens when we create an automobile.
     # Three principle of object oriented programming "PIE"
     # Polymorphism
     # Inheritence
     # Encapsulation
     def __init__(self, make, model, vin, engine_size, owner, year, colour):
          # Define class properties with the parameter values. 
          # Make class properties directly inaccessible 
          # Use a double underscore to make these values private outside of the class
          self.__make = make
          self.__model = model
          self.__vin = vin
          self.__engine_size = engine_size
          self.__owner = owner
          self.__year = year
          self.__colour = colour
     # Create getter and setter methods
     def get_make(self):
          return self.__make
     def get_model(self):
          return self.__model
     def get_vin(self):
          return self.__vin
     def get_engine_size(self):
          return self.__engine_size
     def set_engine_size(self, new_size:int):
          self.__engine_size = new_size
     def get_owner(self):
          return self.__owner
     def set_owner(self, new_owner:str):
          self.__owner = new_owner
     def get_year(self):
          return self.__owner
     def get_colour(self, new_colour:str):
          self.__colour = new_colour
     # Create a method to print Automobile data
     def print_data(self):

          print(f"{self.__year} {self.__make} {self.__model} {self.__year}")
          print(f"VIN: {self.__vin} {self.__engine_size}")
          print(f"OWNER: {self.__owner} COLOUR: {self.__colour}")
     # Create a method to get the automobile's age
     def get_age(self):
          # Get the current year
          the_date = datetime.datetime.now()
          this_year = the_date.year
          # Return the difference between the current year and the auto year as the age
          return this_year - self.__year

