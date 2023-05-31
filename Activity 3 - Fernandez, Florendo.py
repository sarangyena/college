# Math Tutor v 1.0 Name/s: John Marvin Fernandez & Edrian Florendo
import random

def add (x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def dividedby(x, y):
    return x / y

while True: 
    print ("Enter your choice 1- Add, 2- Subtract, 3- Multiply, 4- Division: ")
    choice = input("")
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            qty = int(input("How many question?: "))
            a = int(1)
            b = int(0)
            while a <= qty:  
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    a = a + 1
                    b = b + 1
                else:
                    print("Wrong, the correct answer is: ",num3)
                    a = a + 1                   
            print ("DONE")
            a = 1
            print("Score: " + str(b) + "/" + str(qty) )
            b = 0            
        elif choice == '2':
            qty = int(input("How many question?: "))
            a = int(1)
            b = int(0)
            while a <= qty:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtract(num1, num2)
                print("What is the dif of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    a = a + 1
                    b = b + 1
                else:
                    print("Wrong, the correct answer is: ",num3)
                    a = a + 1
            print ("DONE")
            a = 1
            print("Score: " + str(b) + "/" + str(qty) )
            b = 0     
        elif choice == '3':
            qty = int(input("How many question?: "))
            a = int(1)
            b = int(0)
            while a <= qty:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("What is the mul of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    a = a + 1
                    b = b + 1
                else:
                    print("Wrong, the correct answer is: ",num3)
                    a = a + 1
            print ("DONE")
            a = 1
            print("Score: " + str(b) + "/" + str(qty) )
            b = 0     
        elif choice == '4':
            qty = int(input("How many question?: "))
            a = int(1)
            b = int(0)
            while a <= qty:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = dividedby(num1, num2)
                print("What is the div of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    a = a + 1
                    b = b + 1
                else:
                    print("Wrong, the correct answer is: ",num3)
                    a = a + 1
            print ("DONE")
            a = 1
            print("Score: " + str(b) + "/" + str(qty))
            b = 0
    try_again = input("Want to try again (y/n)")
    if try_again == "n" or try_again == "N":
        print ("STOP")
        break
    elif try_again == "y" or try_again == "Y":      
        print ("")
else:
    print("Invalid Input")