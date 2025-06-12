# This file will demonstrate how for loops work. 

def main():
     # Print integers between 0 and 10.
     print("Output numbers between 1 and 10.")
     for number in range(11):
          print(number)
     # Print integers from 5 and 10.
     print("\n\nOutput numbers between 5 and 10.")
     for number in range(5,11):
          print(number)
     # Print even numbers between 0 and 10.
     print("\n\nOutput even numbers between 0 and 10.")
     for number in range(0,11,2):
          print(number)
     # Print odd numbers between 0 and 10.
     print("\n\nOutput odd numbers between 0 and 10.")
     for value in range(1,11,2):
          print(value)
     # Prompt a user for the start and stop vaulues and
     # print the numbers between start and stop.
     # Get the start value from the user and convert to an integer
     start_value = int(input("Please provide the starting value: "))
     # and for times sake do not worry about edgecases.
     # Get the stop value from the user and convert to an integer.
     stop_value = int(input("Please provide the ending value: "))
     print(f"\n\nOutput numbers from {start_value} to {stop_value}")
     # Create a loop to run from start to stop.
     for value in range(start_value,stop_value + 1):
          print(value)
     # Use nested for loops to print multiplication tables from user input.
     start_value = int(input("Please provide the starting value: "))
     stop_value = int(input("Please provide the ending value: "))
     print(f"\n\nPrint multiplication tables from {start_value} to {stop_value}")
     for table in range(start_value, stop_value + 1):
          print(f"\nDisplaying the {table} multiplication tables\n")
          for multiple in range(1,13):
               product = table * multiple
               print(f"{table} x {multiple} = {product}")
main()