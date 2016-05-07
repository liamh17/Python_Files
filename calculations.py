
def add():
    print('Enter first value: ')
    a = int(input())
    print('Enter second value: ')
    b = int(input())

    sum = a + b
    sum = str(sum)
    print('The sum is: ' + sum) 

def subtract():
    print('Enter first value: ')
    a = int(input())
    print('Enter second value: ')
    b = int(input())

    difference = a - b
    difference = str(difference)
    print('The difference is: ' + difference)  
    
def multiply():
    print('Enter first value: ')
    a = int(input())
    print('Enter second value: ')
    b = int(input())
        
    product = a * b
    product = str(product)
    print('The product is: ' + product) 

def divide():
    print('Enter first value: ')
    a = int(input())
    print('Enter second value: ')
    b = int(input())

    quotient = a / b
    quotient = str(quotient)
    print('The quotient is: ' + quotient) 

choiceNumber = 0
while choiceNumber < 5:
    print('Choices: add, subtract, multiply, divide')
    print('Type "exit" to exit the outupt terminal.') 
    print('Enter an operation: ')
    choice = input()
    choiceNumber = choiceNumber + 1

    if choice == 'add':
        print('You chose, ' + choice)
        add()
    elif choice == 'subtract':
        print('You chose, ' + choice)
        subtract()
    elif choice == "multiply":
        print('You chose, ' + choice)
        multiply()
    elif choice == 'divide':
        print('You chose, ' + choice)
        divide()
    elif choice == 'exit':
        print('Sad to see you go, goodbye!') 
        exit() 
