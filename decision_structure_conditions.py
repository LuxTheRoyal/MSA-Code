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
     test_score = 77

     if ((test_score <= 100) and (test_score >= 90)):
          print(f"{test_score} --> A")
     elif ((test_score <= 90) and (test_score >= 80)):
          print(f"{test_score} --> B")
     elif ((test_score <= 80) and (test_score >= 70)):
          print(f"{test_score} --> C")
     elif ((test_score <= 70) and (test_score >= 60)):
          print(f"{test_score} --> D")
     else:
          print(f"{test_score} --> F")
     
main()