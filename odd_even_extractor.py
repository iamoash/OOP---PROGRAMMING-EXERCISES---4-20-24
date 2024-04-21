def main():
# Read the numbers from the input file
with open("numbers.txt", "r") as file:
    numbers = [int(num) for num in file.read().split()]
# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Write even numbers to even.txt

# Write odd numbers to odd.txt