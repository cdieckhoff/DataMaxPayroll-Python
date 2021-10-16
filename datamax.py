# File: datamax.py
# Author: Chris Dieckhoff
# Date: 10/10/2021
# Description: 
# This is a C++ project I did while in college and decided to port it in python
# The program asks user for employee(s) input (name, payrate, hours) and calculates
# the pay the employee receives, including overtime.

from employee import employee

numemps = 0
passing_type = False
employees = []
# We need 3 inputs for employee: name, rate, hours
# Clear the screen
print("\033[2J")

print("DataMax Payroll Calculator [Python Edition]\n\n")
while(passing_type == False):
    inp = input("How many employees are you entering data for?   ")
    #check for number
    if(inp.isnumeric()):
        numemps = int(inp)
        passing_type = True
    else:
        print("Invalid format!\nPlease enter a numeric value.")

# We have the number of employees to be entered
passing_type = False
for i in range(numemps):
    ename = ''
    erate = 0.0
    ehours = 0.0
    while(passing_type == False):
        ename = input("What is the employee's name?   ")
        if(isinstance(ename,str)):
            passing_type = True
            continue
    # Get the employees' name
    passing_type = False
    while(passing_type == False):
        erate = input("What is the hourly wage for "+ename+"?   ")
        if(erate.replace('.','',1).isdigit()):
            erate = float(erate)
            passing_type = True
            continue
        else:
            print("Exptected 00.00 input!\nPlease try again.\n")
    # Get the amount of hours worked
    passing_type = False
    while(passing_type == False):
        ehours = input("How many hour(s) did " + ename + " work?   ")
        if(ehours.replace('.','',1).isdigit() or ehours.isnumeric()):
            ehours = float(ehours)
            passing_type = True
            continue
        else:
            print("Exptected a numeric value!\nPlease try again.\n")
    passing_type = False
    employees.append(employee(ename,erate,ehours))

#output summary of employee(s)
print()
for i in range(len(employees)):
    print(employees[i].summary())

print("Thank your for using DataMax Payroll")

