# INPUT
# Checks for edge cases
# Gets user input
# Edgecases checked for:
# Returns an expression
# x and z are not integers or y is not an operator 
# not seperated by spaces
# THIS IS NOT FINISHED
def expression_input():
     while True:
          try:
               inputed_expression = (input("Please input an expression: "))
               inputed_expression.split(" ")
               number_of_terms = len(inputed_expression)
               y = inputed_expression[2]
               if (number_of_terms == 3 and (y == "*" or y == "-" or y == "+" or y == "/")):
                    break
               else:
                    print("ERROR: Please include spaces on either side of the operator!\n(OPERATOR OPTIONS: +, -, *, or /)")
                    continue
          except:
               print("ERROR: Please input a valid expression with two integer numbers seperated by an operator!\n(OPERATOR OPTIONS: +, -, *, or /)")
               continue
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
# Splits expression into x y x 
# Sends x y z to calculator and then prints the calculated value
def main():
     expression = expression_input()
     x = expression[0]
     y = expression[1]
     z = expression[2]
     final_calculated_value = expression_calculator(x,y,z)
     print(f"The expression inputed equals {final_calculated_value:.1f}")
main()