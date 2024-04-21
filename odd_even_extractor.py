def main():
    try:
        # Read the numbers from the input file
        with open("numbers.txt", "r") as file:
            numbers = [int(line.strip()) for line in file]

        # Separate even and odd numbers
        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]

        # Write even numbers to even.txt
        with open("even.txt", "w") as even_file:
            for num in even_numbers:
                even_file.write(f"{num}\n")

        # Write odd numbers to odd.txt
        with open("odd.txt", "w") as odd_file:
            for num in odd_numbers:
                odd_file.write(f"{num}\n")

        print("Even and odd numbers extracted successfully!")

    except FileNotFoundError:
        print("Error: The 'numbers.txt' file was not found.")

if __name__ == "__main__":
    main()
