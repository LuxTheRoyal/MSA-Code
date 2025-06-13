# INPUT
# 
def get_month():
     # Validate that the number is 1-12
     # Reprompt user if input is not valid
     while True:
          try:
               user_month=int(input("Please input a month number: "))
               if user_month<=0 or user_month>12:
                    print("ERROR: Please input a valid month number!")
                    continue
               else:
                    break
          except:
               print("ERROR: Please input an integer number and do not include any special characters!")
     return user_month
# PROCESSING
# You can use a colon in the parameters followed by the type to remind future programmers
def get_season(user_month:int):
     if ((user_month==12) or (user_month<=2)):
          return "winter"
     elif (user_month<=5):
          return "Spring"
     elif (user_month<=8):
          return "Summer"
     elif (user_month<=11):
          return "Fall"
     else:
          print("Please input a valid month of the year.")
# Different processing fuction that I did not code myself
def get_season_alternate(user_month:int):
     if (user_month in [12,1,2]):
          return "winter"
     elif (user_month in [3,4,5]):
          return "Spring"
     elif (user_month in [6,7,8]):
          return "Summer"
     elif (user_month in [9,10,11]):
          return "Fall"
     else:
          print("Please input a valid month of the year.")
# OUTPUT 
# Must be the integer
def main():
     while True:
          user_month=get_month()
          season = get_season(user_month)
          rerun_prompt = input(f"With the provided month number the season would be {season}.\nWould you like to run again?\nPress y to continue: ")
          if (rerun_prompt=="y" or rerun_prompt=="Y"):
               continue
          else:
               break
     # Prompt and get a month number from the user by calling the get_month()
     # Call get_season() to get the name of the season
     # Print the output
     # Ask the user if they want to run the program again
     # f y or Y rerun the program otherwise end it
main()