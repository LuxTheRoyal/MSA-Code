from Student import Student


def main():
    
     student_data_file = open("students.csv", "r")
     list_of_students = []
     for line in student_data_file:
          student_data = line.split(",")
          if len(student_data) != 6:
               continue

          try:
               student_credit_hours = int(student_data[3])
               student_gpa = float(student_data[4])      
          except:
               continue
          
          student_id_number = student_data[5]
          student_first_name = student_data[0]
          student_last_name = student_data[1]
          student_major = student_data[2]
          individual_student = Student(student_first_name,student_last_name,student_major,student_credit_hours,student_gpa,student_id_number)
          list_of_students.append(individual_student)

     

     student_data_file.close()

     for student in list_of_students:
         student.print_student_data()
main()