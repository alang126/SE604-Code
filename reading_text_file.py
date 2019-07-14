def p():
    print("\n -------PROGRAM CHANGE-------------\n")
'''reading an external file'''
employee_file = open("employees.txt", "r")
# parameters - filename, r-read, w-write, a-append, r+-read and write
print("The name of the file is :" + employee_file.name)
print("Is the file readable?", employee_file.readable())
print("The file mode is ", employee_file.mode)
p()
print(" Use 'readline ()' ---which will be line one the first time and second the next etc. \n")
print(employee_file.readline())
p()
print("'.readlines' takes info in the file and puts each line into an array-note the added line '\n'")
print(employee_file.readlines())
p()
employee_file.close()
employee_file = open("employees.txt", "r")
print(".readlines()[x]) lets you choose which line\n")
print("NOTE- if you have read the line before,\n you must close and reopen the file to return to the top of the file!!\n")
print(employee_file.readlines()[3])
p()
employee_file.close()
employee_file = open("employees.txt", "r")
print("----doing a for loop----\n")
for employee in employee_file.readlines():
    print(employee)
# always close the file after operation
employee_file.close()

'''Writing and Appending to files'''
p()
print(" Appending to the File")
def addEmployees():
    x= int(input("How many employees do you want to add? \n"))
    for inputs in range(x):
        employee_file=open("employees.txt","a")
        new_guy = input("Enter a new employee: name,job ")
        employee_file.write("\n"+ new_guy)
        employee_file.close()
        employee_file = open("employees.txt", "r")
        print(employee_file.read())
addEmployees()

p()
print("END")

