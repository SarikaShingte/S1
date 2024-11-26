# Initialize a variable to store the sum
total_sum = 0

# Loop to get 10 digits from the user and add them
for i in range(10):
    digit = int(input(f"Enter digit {i+1}: "))  # Take input and convert to integer
    total_sum += digit  # Add the digit to the total sum

# Print the final result
print(f"The sum of the 10 digits is: {total_sum}")
  
