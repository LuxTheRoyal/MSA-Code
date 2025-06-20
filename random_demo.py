import random
def main():
     # Create a random number generator.
     random_generator = random.Random()
     for _ in range(20):
          print(random_generator.randint(0,100))
main()