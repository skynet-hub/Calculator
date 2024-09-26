from function import *

def Calculator():
    print("+, -, /, *")
    operator = input("Select an operator: ")
    try:
        first_num = eval(input("Enter the first number: "))
    except NameError:
        print("You have entered a non-number, please enter a number.")
    else:
        try:        
            second_num = eval(input("Enter a second number: "))
        except NameError:
            print("You have entered a non-number, please enter a number.")    
        else:    

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
                print("Invalid operator, please enter on of operators provided.")    
                    

Calculator()             