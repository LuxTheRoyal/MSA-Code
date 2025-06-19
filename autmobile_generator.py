from automobile import Automobile
# Three principle of object oriented programming "PIE"
# Polymorphism
# Inheritence
# Encapsulation
def main():
     # create instances of Automobile
     auto1 = Automobile("Honda", "Accord", "23456", 2.2, "Alice", 2017, "Black")
     auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")
     # Change auto2 year
     auto2.__year = 2000
     auto1.owner = "Walker"
     auto_list = []
     auto_list.append(auto1)
     auto_list.append(auto2)
     for auto in auto_list:
          auto.print_data()
     print(f"auto 1 is {auto1.get_age()} years old.")
main()