from functions import *
import math

#This function takes the operator the user wants to compute and takes in the numbers to compute on.
def Calculator():
    operators = ['+', '-', '/', '*']
    print("+, -, /, *")
    operator = input("Choose an operator: ")
    while operator not in operators:
        print("******Please select a valid operator************")
        operator = input("Choose an operator: ")  

    while True:    
        try:
            first_num = eval(input("Enter the first number: "))   
            break 
        except NameError:
    
           print("You have entered a non-number, please enter a number.")
    
    while True:   
        try:        
            second_num = eval(input("Enter a second number: "))
            break
        except NameError:
            print("You have entered a non-number, please enter a number.")    
           

    if operator == "+":
        print(f"results: {add(first_num, second_num)}")
    elif operator == "-":
        print(f"results: {subtract(first_num, second_num)}")
    elif operator == "/":
        if second_num == 0 and operator == "/":
            print("Undefined, You cannot divide with 0.")
        else:    
            print(f"results: {divide(first_num, second_num)}")          
    elif operator == "*":
        print(f"results: {multiply(first_num, second_num)}")
    else:
        print("Invalid operator, please enter one of the operators provided in the list above.")    
                    
still_on = True
while still_on:
    Calculator()             