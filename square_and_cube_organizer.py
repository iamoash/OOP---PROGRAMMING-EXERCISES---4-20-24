def process_integers(source_file):
    # Open the file to read
    with open(source_file, 'r') as infile:
        # Read all integers from the file
        integers = [int(line.strip()) for line in infile.readlines()]

    # Open output files for writing
    with open('double.txt', 'w') as double_file, open('triple.txt', 'w') as triple_file:
        # Iterate through the integer
        for num in integers:
            # Check if the number is even
            if num % 2 == 0:
                # Calculate the square of even numbers and write to double.txt
                double_file.write(str(num ** 2) + '\n')
            else:
            
                # Calculate the cube of odd numbers and write to triple.txt
                triple_file.write(str(num ** 3) + '\n')

# Call the method with the source file name
process_integers('integers.txt')