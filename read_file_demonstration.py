def main():
     # Open file_demonstration.txt: create a file handler in read mode
     data_file = open("file_demonstration.txt", "r")
     # Create a dictionary out of it
     menu_items_and_prices = {

     }
     # Use a loop to read the contents of the file line by line
     for line_of_data in data_file:
          # Split the data at the comma
          item_name_and_price = line_of_data.split(",")
          # Get the menu item (key) and price (value) from the file
          item_name = item_name_and_price[0]
          item_price = float(item_name_and_price[1])
          # Create an entry in the dictionary for the item and price
          menu_items_and_prices[item_name] = item_price
main()