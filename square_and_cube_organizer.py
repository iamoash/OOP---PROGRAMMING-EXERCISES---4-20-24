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
            
                # Calculate the square of even numbers and write to double.txt
                
            
                # Calculate the cube of odd numbers and write to triple.txt
                

# Call the method with the source file name
