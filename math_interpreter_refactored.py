# INPUT
"""
Function: To get an expression from user
Input: What the user types when prompted
Output: The expression inputted by the user
"""
def expression_input():
     while True:
          inputed_expression = (input("Please input an expression with one number, an operator, and another number: "))
          number_of_terms = len(inputed_expression.split(" "))
          if number_of_terms != 3: 
               print("ERROR: Please include spaces on either side of the operator!\n(OPERATOR OPTIONS: +, -, *, or /)")
               continue
          try:
               y = inputed_expression.split(" ")[1]
               x = int(((inputed_expression.split(" ")[0])))
               z = int(((inputed_expression.split(" ")[2])))
          except:
               print("ERROR: Please a valid expression in which both numbers are integers!")
               continue
          valid_operators = ["*", "+", "-", "/"]
          if y not in valid_operators:
               print("ERROR: Please enter a valid operator!\n(OPERATOR OPTIONS: +, -, *, or /)")
               continue
          if z == 0:
               print("ERROR: Can not divide by 0!")
          break
               
     return inputed_expression 
# PROCESSING
"""
Function: Evaluates an expression.
Inputs: (int)X, (string)Y, and (int)Z
Output: The final answer
"""
def expression_calculator(x: int,y: str,z: int):
     if y == "*":
          calculated_value = x * z
     elif y == "-":
          calculated_value = x - z
     elif y == "/":
          calculated_value = x / z
     else:
          calculated_value = x + z
     return calculated_value
# OUTPUT
"""
Function to get valid expression inputs from the user.
Input: NONE
Outputs: (Int)X, (string)Y, and (int)Z
"""
def main():
     while True:
          expression = expression_input()
          y = expression.split(" ")[1]
          x = int((expression.split(" ")[0]))
          z = int(expression.split(" ")[2])
          final_calculated_value = expression_calculator(x,y,z)
          print(f"The expression inputed equals {final_calculated_value:.1f}")
          rerun_prompt = input(f"The expression inputed equals {final_calculated_value:.1f}.\nWould you like to run again?\nPress y to continue: ")
          if (rerun_prompt=="y" or rerun_prompt=="Y"):
               continue
          else:
               break
main()