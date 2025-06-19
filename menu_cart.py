"""
Function to load menu item and price into a dictionary
Input: (string)file_path
Output: (dictionary)menu 
"""
# LOOK BACK AT THIS CODE FOR FURTHER UNDERSTANDING!
def get_menu_dictionary(file_name:str) -> dict:
    #open file.txt: create a file handler in read mode
    data_file = open("file_demonstration.txt", "r")
    print(data_file)

    #create an empty dictionary to store item: price entries
    menu_items = {}

    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the data ant the comma
        item_name_and_price = line_of_data.split(",")
        
        #get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price
    
    data_file.close()
    return menu_items

def display_cart(cart:dict, menu_items:dict) -> None:
     #loop through the cart
     print("\nCart\n----")
     total = 0
     for item, quantity in cart.items():
          total += (quantity * menu_items[item])
          print(f"{quantity} {item} @{menu_items[item]:.2f}: {quantity * menu_items[item]:.2f}")
          print(f"\nTotal: {total:.2f}")
     return
"""
Function to write items from the cart to a receipt
Input: cart:dict
Output: None
"""
def print_receipt(cart:dict, menu_items:dict)->None:
     with open("receipt.txt", "w") as receipt_file:
          total = 0
          for item, quantity in cart.items():
               total += (quantity * menu_items[item])
               receipt_file.write(f"{quantity} {item} @{menu_items[item]:.2f}: {quantity * menu_items[item]:.2f}\n")
          receipt_file.write(f"\nTotal: {total:.2f}")
def main():
     menu_items = get_menu_dictionary("file_demonstration.txt")
     item_cart = {}
     total = 0
     while True:
          #prompt user for item
          item = input("\nItem: ")

          #determine if we need to end the program
          if item.lower() == "end":
               print_receipt(item_cart, menu_items)
               break
        
          #get the item price and add to total
          #Validate that item is in the menu item dict
          #use try except to catch an error if the item is not in the dictionary
          if item not in menu_items:
            print(f"\nERROR: {item} is not an item on the menu!" )
            continue
          # Add item to cart. If it is in cart already than add quantity
          # If it is not then add the item and quanitity
          try: 
               quantity = int(input("Quantity: "))
          except:
               print("\nERROR: Enter a number for quantity!")
               continue
          if item not in item_cart:
              item_cart[item] = quantity
          else:
              item_cart[item] += quantity
          #display total by calling the display cart function
          display_cart(item_cart, menu_items)
          """
          2 Taco @$3: $6.00
          3 Bowl @$8.5: $25.50
          Total: 31.50
          """


main()