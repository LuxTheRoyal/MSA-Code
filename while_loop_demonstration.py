# Create a while loop that prints integers between 0 and 10.

output_value = 0
stop_value = 10

# Run the loop while output_value is less than or equal to stop_value.

while output_value <= stop_value:
     print(output_value)
     # Increment output_value by 1.
     output_value = output_value + 1

print("\n\n")
output_value = 0
while True:
     print(output_value)
     # Increment output value by 1.
     output_value += 1

     # If the condition of output_value is greater than stop_value. Break the loop.
     if output_value > stop_value:
          break