def main():
    # Open the File Of Student GWA
    try:
        with open("student_gwa.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    # Create a dictionary to store student names and GWAs
    student_gwa = {}

    # Analyze each line of the file
    for line in lines:
        data = line.strip().split(",")
        name = data[0]
        gwa = float(data[1])
        student_gwa[name] = gwa

    # Find the student with the highest GWA
    highest_gwa_student = max(student_gwa, key=student_gwa.get)
    highest_gwa = student_gwa[highest_gwa_student]

    # Output the student with the highest GWA
    print("Student with the highest GWA:")
    print(f"Name: {highest_gwa_student}")
    print(f"GWA: {highest_gwa}")

if __name__ == "__main__":
    main()
    