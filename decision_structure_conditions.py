# This file demonstrates decision structures and their conditions.
def main():
     a = 7
     b = 7
     # Exploring conditions!
     print(f"A is greater than B: {a > b}")
     print(f"B is greater than A: {b > a}")
     # Comparison operators:
     # Less than: <, Greater than: >, Less than or equal to: <=, Greater than or equal to >=, Equal to: ==
     # One equal sign is an assignment statement and two equal signs is a comparison operator.
     # Create a decision to determine if a and b are equal.
     if a > b:
          print(f"{a} is greater than {b}.")
     elif b > a:
          print(f"{b} is greater than {a}.")
     else:
          print(f"{a} is equal to {b}.")
     # Create a decision strucutre to print a letter grade based on a test score.
     print("Grade Decision: 1")
     test_score = 137

     if ((test_score <= 100) and (test_score >= 90)):
          print(f"{test_score} --> A")
     elif (test_score >= 80):
          print(f"{test_score} --> B")
     elif (test_score >= 70):
          print(f"{test_score} --> C")
     elif (test_score >= 60):
          print(f"{test_score} --> D")
     elif ((test_score > 100) or (test_score >= 0)):
          print(f"ERROR: {test_score} is an invalid score!")
     else:
          print(f"{test_score} --> F")
     
     # Create a decision structure to determine the season: winter, summer, spring, autumn.
     # Ask the user to enter the number of the month and based on the number, determine the season.
     # Output the season: It is {season}.
     user_month = int(input("Please input a month to find the season: " ))
     if (((user_month == 12) or (user_month <= 2)) and (user_month <0)):
          print("The curent season is Winter.")
     elif (user_month <= 5):
          print("The curent season is Spring.")
     elif (user_month <= 8):
          print("The curent season is Summer.")
     elif (user_month <= 11):
          print("The current season is Autumn.")
     else:
          print("Please input a valid month of the year.")

main()