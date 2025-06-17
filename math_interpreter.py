# INPUT
# Checks for edge cases
# Gets user input
# Edgecases checked for:
# Returns an expression
# x and z are not integers or y is not an operator 
# not seperated by spaces
# Splits expression into x y z
# YEAH... this code does not check for the edgecase that the y variable is correct but x and z are gibberish
# It just fucking crashes
# Will have to examine it later
def expression_input():
     while True:
          inputed_expression = (input("Please input an expression with one number, an operator, and another number: "))
          number_of_terms = len(inputed_expression.split(" "))
          if number_of_terms != 3: 
               print("ERROR: Please include spaces on either side of the operator!\n(OPERATOR OPTIONS: +, -, *, or /)")
               continue
          y = inputed_expression.split(" ")[1]
          x = ((inputed_expression.split(" ")[0]))
          z  = ((inputed_expression.split(" ")[2]))
          if (y != "*" and y != "-" and y != "+" and y != "/"):
               print("ERROR: Please enter a valid operator!\n(OPERATOR OPTIONS: +, -, *, or /)")
               continue
          if ((type(int(x)) != int) or (type(int(z)) != int)):
               print("ERROR: Please a valid expression in which both numbers are integers!")
               continue
          break
               
     return inputed_expression 
# PROCESSING
# Gets x y z from main
# Returns the calculated value
def expression_calculator(x,y,z):
     if y == "*":
          calculated_value = x * z
     elif y == "-":
          calculated_value = x - z
     elif y == "/":
          calculated_value = x / z
     else:
          calculated_value = x + z
     return calculated_value
# Sends x y z to calculator and then prints the calculated value
def main():
     expression = expression_input()
     y = expression.split(" ")[1]
     x = int((expression.split(" ")[0]))
     z = int(expression.split(" ")[2])
     final_calculated_value = expression_calculator(x,y,z)
     print(f"The expression inputed equals {final_calculated_value:.1f}")
main()