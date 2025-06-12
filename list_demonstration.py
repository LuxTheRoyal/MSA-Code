# This file will demonstrate lists in Python.
def main():
     # We do not what to do this!
     # name_1 = "John"
     # name_2 "Mary"
     # Instead create a list ov names.
     names = ["John","Mary","Alice","Bob"]
     list_of_integers = [10,16,24,42,14,9]
     random_datatype_list = ["String",15,22.3,True]
     print(names)
     # Add an item to the names list.
     inputed_name = input("Please type a name to be added to the list: ")
     names.append(f"{inputed_name}")
     print(names)
     # Get the number of items in a list.
     print("\nNumber of items in the name list.")
     number_of_items = len(names)
     print(f"Number of items in the names list: {number_of_items}")
     # Get the values from our list.
     # Get the first value from our list_of_integers.
     print(f"\nFirst item in integer list: {list_of_integers[0]}")
     # Print all items from my list_of_integers.
     print("\nInteger list itmes")
     for item in list_of_integers:
          print(item)
     print("\nInteger list items using the itme indexes.")
     number_of_integer_items = len(list_of_integers)
     for index in range(number_of_integer_items):
          print(f"Item {index}: {list_of_integers[index]}")
main()