def main():
     my_name = "alexander"
     # Capitalize a string
     print(my_name.capitalize()) 
     print(my_name.upper())
     my_last_name = "BATES"
     print(f"{my_name.capitalize()} {my_last_name.lower().capitalize()}")
     # Determine if a string starts with a set of characters
     print("\nUsing startswith() method")
     print(my_name.startswith("A") or my_name.startswith("a"))
     if(not my_name.startswith("alex") and not my_name.startswith("Alex")):
          print(f"You spelled {my_name} wrong!")
     else:
          print(f"You spelled {my_name} correctly. :)")
     print(f"Using endswith() method")
     print(f'{my_name} ends with "ander": {my_name.endswith("andr")}')
     # ^^^Yo printing with single quotes is fire^^^
     print("\nUsing the find() method")
     # Find the d if Alexander
     search_letter = "d"
     if(my_name.find(search_letter) == -1):
          print(f'There is not a {search_letter} is {my_name}')
     else:
          print(f'The {search_letter} is at index {my_name.find(search_letter)} in {my_name}')
     # Loop through a string.
     print("\nLoop through a string")
     for xyztest in my_name:
          print(xyztest)
     print(f"{my_name} has {len(my_name)} letters")
     # Print the letters in a string along with the index position.
     for letter_index in range(len(my_name)):
          print(f"Letter {letter_index+1}: {my_name[letter_index]}")
     print("\n\n")
     sentence = "I have a dog. My dog is cute. Do you want a dog?"
     # Write a code that counts the number of occurences of the word dog in the sentence.
     # Expected output
     # maybe something like this for (sentence.find("dog") in sentence): number_of_incurences=0+1 print(number_of_incurences)
     # Wait no
     # Use a while loop 
     dog_start_index = 0
     number_of_dogs = 0
     search_word = "dog"
     # Start at the beginning of the string
     # Search for the first occurence of the word dog
     # Update the start_index to dog index + 1
     while True:
          # If we find a dog add 1 to some varaible of dogs we found
          # Continue searching the string from the next index ater the dog we found
          # Do this until we do not find any more dogs
          dog_index = sentence.find(search_word, dog_start_index)
          if dog_index == -1:
               break
          else:
               number_of_dogs+=1
               dog_start_index = dog_index + 1
     print(f"There are {number_of_dogs} dogs.")
     # How to use the split() method
     print("\nUsing the split() method")
     car_info = "Ferrari,F-50,2021,500000,4.8\n"
     car_data = car_info.split(",")
     print(car_data)
     # Get individual pieces of data
     make = car_data[0]
     model = car_data[1]
     year = int(car_data[2])
     price = float(car_data[3])
     engine_size = float(car_data[4])
     print(f"{year} {make} {model}")
     print(f"Price: ${price} & Engine: {engine_size}L")

main()