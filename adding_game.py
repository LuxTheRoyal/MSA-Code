import random
# INPUT
"""
Create a while loop that breaks internally when a valid input is provided by the user. This will be contained within a function that gets the chosen difficulty 
Create a while loop that breaks internally when a valid input is provided by the user. This will be contained within a function that gets number of questions.
"""
def user_chosen_difficulty():
     difficulty_levels = [1,2,3]
     while True:
          try:
               selected_difficulty = int(input("Please input a difficulty level.\n(OPTIONS: 1 - Easy, 2 - Normal, 3 - Hard)\nSelect Diffculty: "))
               if selected_difficulty not in difficulty_levels:
                    print("\nERROR: The single interger value inputed must correspond to a difficulty level!")
                    continue
               break
          except:
               print("\nERROR: Enter a single interger value with no other characters!")
               continue
     return selected_difficulty
def user_chosen_question_quantity():
     possible_question_quantities = [3,4,5,6,7,8,9,10]
     while True:
          try:
               selected_question_quantity = int(input("Please input a difficulty level.\n(OPTIONS: 3-10)\nSelect Question Quantity: "))
               if selected_question_quantity not in possible_question_quantities:
                    print("\nERROR: The interger value inputed must be between 3-10!")
                    continue
               break
          except:
               print("\nERROR: Enter an interger value with no other characters!")
               continue
     return selected_question_quantity
# PROCESSING
"""
A function is needed to calculate the correct answer to the question and compare it to the inputed answer to see if the inputed answer is true or false.
Another function is needed to randomly generate the math problems. 
There needs to be a processing funtion that takes the number of questions that were corrrect and divides it by the number of questions asked (rounds to two decimals)
"""
def answer_calculator_and_comparer(x:int,z:int):
     correct_answer = x + z
     return correct_answer
def random_question_generator(selected_difficulty:int):
     random_number = random.Random()
     if selected_difficulty == 1:
               x = random_number.randint(0,9) 
               z = random_number.randint(0,9)
     elif selected_difficulty == 2:
               x = random_number.randint(10,99) 
               z = random_number.randint(10,99)
     else:
               x = random_number.randint(100,999) 
               z = random_number.randint(100,999)
     return x,z
def user_success_rate_calculator(number_of_final_correct_answers:int, selected_question_quantity:int):
     success_rate = (number_of_final_correct_answers / selected_question_quantity) * 100
     return success_rate
# OUTPUT
"""
The most important function is the main function which will handle logic for (playing again OPTIONAL) and calling upon every other function in the code.
Create a decision structure that runs as long as the number of times the wrong answer text is less than three. Afterward, this second function will print the next question until the number of questions prompted is equal to the number of problems requested.
Another function will be needed. It will be a loop that runs for the number of questions the user wants. 
Afterward, this second function will print the next question until the number of questions prompted is equal to the number of problems requested. Part of the input will be in main
"""
def main():
     while True:
          selected_difficulty = user_chosen_difficulty()
          selected_question_quantity = user_chosen_question_quantity()
          number_of_final_correct_answers = 0
          for _ in range(selected_question_quantity):
               x, z = random_question_generator(selected_difficulty)
               correct_answer = answer_calculator_and_comparer(x,z)
               number_of_incorrect_answers = 1
               while True:
                    try: 
                         inputed_answer_pre_conversion = (input((f"\n{x} + {z} = ")))
                         inputed_answer = int(inputed_answer_pre_conversion)
                         if number_of_incorrect_answers == 3:
                              print(f"\n{x} + {z} = {correct_answer}")
                              break
                         elif inputed_answer == correct_answer:
                              print("\nCORRECT!!!")
                              number_of_final_correct_answers += 1
                              break
                         else:
                              print("\nWRONG!!!")
                              number_of_incorrect_answers += 1
                              continue
                    except:
                         if number_of_incorrect_answers == 3:
                              print(f"\n{x} + {z} = {correct_answer}")
                              break
                         else:
                              print("\nWRONG!!!")
                              number_of_incorrect_answers += 1
                              continue
          success_rate = user_success_rate_calculator(number_of_final_correct_answers, selected_question_quantity)
          print(f"You got {number_of_final_correct_answers} out of {selected_question_quantity} correct.\nSuccess Rate: {success_rate:.2f}%")
          run_again_input_pre = input(('\nWould you like to run again?\nType a non-cap-sensitive "y" to run again: '))
          run_again_input = run_again_input_pre.lower()
          if run_again_input == "y":
               continue
          break
main()