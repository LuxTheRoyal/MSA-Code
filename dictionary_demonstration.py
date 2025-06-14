def main():
     # The need for dictionaries
     scores=[55,75,87,82,91]
     students=["Alice","Bob","Jerry","Jane","Bill"]
     # I want to print the names and scores together
     for index in range(len(scores)):
          print(f"{students[index]}: {scores[index]}")
     # Create a dictionary of names and scores
     student_scores={
     "Alice":55,"Bob":75,"Jerry":87,"Jane":82,"Bill":91
     }
     # Print all student data in the student scores dictionary
     for student in student_scores:
          print(f"{student}: {student_scores[student]}")
     # Create a car dictionary to store the make, model, year, value, and engine size of a car
     car_1 = {
          "Make":"Ferrari", "Model":"F-50","Year":2021,"Value":500000,"Engine Type":4.8
     }
     print("\nGet the car's information")
     for key, value in car_1.items():
          print(f"{key}: {value}")
     car_2 ={
          "Make":"Honda","Model":"Accord","Year":2015,"Value":1500
     }
     # Create a list of dictionaries
     car_dictionary_list=[car_1,car_2]
     print("\nDisplay all cars' information")
     for car in car_dictionary_list:
          print("\nCar Information:")
          for feature, value in car.items():
               print(f"{feature}: {value}")
     # Create a dictionary of dictionaries
     car_super_dictionary={
          "Ferrari":car_1,"Honda":car_2
     }
     # Write a for loop to display the car informations
     # Ferrari
     # Print all the ferrari information
     # Honda
     # Print all the honda information
     for make, car in car_super_dictionary.items():
          print(f"{make}:")
          for feature, value in car.items():
               print(f"{feature}: {value}")
main()
