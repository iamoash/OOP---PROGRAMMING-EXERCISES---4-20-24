# Open the File Of Student GWA
def main():
    try:
        with open("student_gwa.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return
    
# Create a file directory to store student names and GWAs
student_gwa = {}

# Analyze each line in the file
for line in lines:
        data = line.strip().split(",")
        name = data[0]
        gwa = float(data[1])
        student_gwa[name] = gwa
# Find the student with the highest GWA

# Output the student with the highest GWA

    