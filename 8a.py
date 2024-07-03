import random

# Generate 20 random numbers between 0 and 10000
random_numbers = [random.randint(0, 10000) for _ in range(20)]
print("Random numbers:", random_numbers)

# Filter odd numbers with length 2 and 4
odd_numbers = [num for num in random_numbers if num % 2 != 0 and (len(str(num)) == 2 or len(str(num)) == 4)]
print("Odd numbers with length 2 and 4:", odd_numbers)
