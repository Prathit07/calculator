from Calculator import Calculator

calculator_is_on = True
while calculator_is_on:
    operation = input('''\n---WELCOME TO PS CALCULATOR---
Please select one of the following:
=======================================
+ for addition
- for subtraction
* for multiplication
/ for division
rect to find the area of a rectangle
sq to find area of square
inch to convert cm to inch
cm to convert inch to cm
0 to exit
========================================
Please enter your chosen operator: ''')
    if operation == str(0):
        print("\n---THANK YOU FOR USING PS CALCULATOR---")
        calculator_is_on = False
    elif operation in ("+","-","*","/"):
        number_1 = int(input("\nPlease enter number 1: "))
        number_2 = int(input("\nPlease enter number 2: "))
        calculator = Calculator(number_1,number_2)
        if operation == "+":
            calculator.add()
        elif operation == "-":
            calculator.substract()
        elif operation == "*":
            calculator.multiply()
        elif operation == "/":
            calculator.divide()
    elif operation == "rect":
        number_1 = int(input("\nPlease enter length: "))
        number_2 = int(input("\nPlease enter width: "))
        calculator = Calculator(number_1,number_2)
        calculator.area_rect()
    elif operation == "sq":
        number_1 = int(input("\nPlease enter length/side: "))
        number_2 = None
        calculator = Calculator(number_1,number_2)
        calculator.area_sq()
    elif operation == "inch":
        number_1 = int(input("\nPlease enter cm: "))
        number_2 = None 
        calculator = Calculator(number_1, number_2)
        calculator.cm_to_inch()
    elif operation == "cm":
        number_1 = int(input("\nPlease enter inch: "))
        number_2 = None 
        calculator = Calculator(number_1, number_2)
        calculator.inch_to_cm()
    else:
        print("---PLEASE ENTER A CORRECT OPERATION---")