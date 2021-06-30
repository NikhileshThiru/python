# Read the file.
employee_file = open("Employees.txt", "r")
print(employee_file.readable())
print(employee_file.read())
print(employee_file.readline())

employee_file.close()

# Write more info.
# open("Employees.txt", "2")
# Append to the end of the file.
employee_file = open("Employees.txt", "a")

employee_file.write("Toby - Human Resources")

employee_file.close()

# Read and write.
# open("Employees.txt", "r")
