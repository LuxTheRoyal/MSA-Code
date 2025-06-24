from Student import Student
from datetime import datetime 
"""
Function to write an error message to a log file.
Input: Error message (string)
Output: None
"""
def write_to_error_log(message:str, line_number:int)->None:
     # Open to long file
     # Write error message to the file in the format
          # Date: message -> 6/24/2025: Error in datafile on line 5
     # Close file
     with open("error_log", "a") as error_log:
          the_date = datetime.now()
          date_of_error = the_date.date()
          error_log.write(f"Date: {message} -> {date_of_error}: Error in datafile on line {line_number}\n")
# This code hurt me bruh
"""
Function to treurn a list of student objects
Input: None
Output: List of student objects
"""
def load_students()->list[Student]:
     line_number = 0
     student_data_file = open("students.csv", "r")
     list_of_students = []
     for line in student_data_file:
          line_number += 1
          student_data = line.split(",")
          if len(student_data) != 6:
               # Write an error message to an error log
               error_message_1 = "ERROR: Missing or overflowing student data!"
               write_to_error_log(error_message_1, line_number)
               continue

          try:
               student_credit_hours = int(student_data[3])
               student_gpa = float(student_data[4])      
          except:
               # Write an error message to an error log
               error_message_2 = "ERROR: Credit Hours or Student GPA conversion failure!"
               write_to_error_log(error_message_2, line_number)
               continue
          
          student_id_number = student_data[5]
          student_first_name = student_data[0]
          student_last_name = student_data[1]
          student_major = student_data[2]
          individual_student = Student(student_first_name,student_last_name,student_major,student_credit_hours,student_gpa,student_id_number)
          list_of_students.append(individual_student)
     student_data_file.close()

     return list_of_students
"""
Function to convert student objects to student dictionaries
Input: List of student objects
Output: List of student dictionaries
"""
def student_to_dictionary(list_of_students:list[Student])->list[dict]:
     # Create a list to store the dictionaries in.
     individual_student_dictionary_list = []
     # Loop through the student list and write each student's data to a dictionary 
     for i in list_of_students:
          # Create an empty dictionary
          # Set the keys and values for the dictionary
          individual_student_dictionary={}
          individual_student_dictionary["first_name"] = i.get_first_name()
          individual_student_dictionary["last_name"] = i.get_last_name()
          individual_student_dictionary["gpa"] = i.get_gpa()
          individual_student_dictionary["major"] = i.get_major()
          individual_student_dictionary["class"] = i.get_class_level()
          individual_student_dictionary["id"] = i.get_id_number()
          # Apend the dictionary to the list of dictionaries
          individual_student_dictionary_list.append(individual_student_dictionary)
     return individual_student_dictionary_list
     # Return the list of dictionaries
"""
Function to get a list of student dictionaries
Input: None
Output: List of student dictionaries
"""
def get_student_dictionaries():
     # Get a list of students
     student_list = load_students()
     # Get a list of student dictionaries
     student_dictionaries = student_to_dictionary(student_list)
     print(student_dictionaries)
     return student_dictionaries
     

get_student_dictionaries()