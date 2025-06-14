# OUTPUT 
# Gets input of what coin type is being inserted and then checks for edgecases
# Returns the denomination of coin to the amount remaining calculator
# Only takes integers of 1,5,10,25
def coin_input():
     while True:
          try:
               inputed_coin=int(input("INSERT COIN: "))
               if inputed_coin==1 or inputed_coin==5 or inputed_coin==10 or inputed_coin==25:
                    break
               else:
                    print("ERROR: Please input a valid coin denomination!\n(1, 5, 10, or 25): ")
                    continue
          except:
               print("ERROR: Please input an integer coin denomination and do not include any special characters!")
     return inputed_coin
# PROCESSING
# Starts the program with a needed input of 50 and reruns a subtraction operation with the variable returned by the coin input function.
# Returns the remaining balance to main.
def amount_remaining_calculator(total_that_is_remaining):
     inputed_coin=coin_input()
     amount_remaining=total_that_is_remaining-inputed_coin
     remaining_total=amount_remaining
     remaining_total=50
     return amount_remaining
# Gets the amount remaining from main
# If the amount remaining is a negative number or zero it takes the absloute value of the number and returns it to the main function
def change_owed_calculator(amount_remaining):
     return abs(amount_remaining)
# OUTPUT
def main():
     # Loops the main function until the change due calculator function runs and outputs the change due.
     #total_that_is_remaining=50
     amount_remaining = 50
     
     while True:
          if amount_remaining>0:
               amount_remaining = amount_remaining_calculator(amount_remaining)
               if amount_remaining > 0:
                    print(f"Amount Due: {amount_remaining}")
          else:
               change_owed=change_owed_calculator(amount_remaining)
               print(f"Change Owed: {change_owed}")
               break
# This code made me switch my theme because how bad my logical error was
# Really? Adjusting the theme, Really? That's been your problem the whole fucking time, the theme colour? So now you have it, right? Go! 
# Honestly not even sure how I got the desired result and this spaghetti is held together with duct-tape
main()