# Write a pounds to kilogram converter program.
# A user will be prompted for their weight in pounds and the program 
# will output weight in kilograms.

# GET INPUT FROM THE USER!
# The weight needs to be converted from a string to a float.
# Validate that the weight inputed actually is a number.
# If the weight is not a number, reprompt the user until the input is correct.
def get_positive_float_input():
     while True:
          try:
               user_weight = float(input("Please enter your weight in pounds.\nIt will then be converted from pounds to kilograms: "))
               # Validate that user_weight is positive. If not positive, reprompt the user.
               # Bruh that continue shelled within in the if is not pythonic smh.
               if user_weight <= 0:
                    print("ERROR: Please enter a positive weight value.")
                    continue
               else:
                    break
          except:
               print("ERROR: Please enter a number for the conversion to take place.")
     
     return user_weight

def main():
     # Get the weight from the user. Call upon the get_positive_float_input function.
     user_weight = get_positive_float_input()

     # PROCESSING
     # Use a conversion input to convert pounds to kilos: 2.205lbs = 1kg

     LBS_TO_KGS_CONVERSION = 2.205
     user_weight_kgs = user_weight / LBS_TO_KGS_CONVERSION

     # OUTPUT
     # Print the output to the use in a nice format to 2 decimal places. 
     # The output will be sent to the console.

     print(f"You weigh {user_weight_kgs:.3f}kgs")

# Actually calls upon the defined main script (now a function) of our program.
main()     