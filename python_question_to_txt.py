def writelines():
    # Open the file for writing ('w' mode)
    outfile = open('myfile.txt', 'w')
    
    # Loop Statements
    while True:
        # Prompt the user to enter a line
        line = input('Enter line: ')
        # Prompt the user to enter a line
        line = input('Enter line: ')
        
        # Add a newline character to the input line
        line += '\n'
        
        # Write the line to the file
        outfile.write(line)
        
        # Prompt the user to determine if there are more lines to enter
        choice = input('Are there more lines y/n? ')
        
        # If the user chooses 'n', exit the loop
        if choice == 'n':
            break
    
    # Close the file
    outfile.close()

# Call the writelines function to execute the code
writelines()
