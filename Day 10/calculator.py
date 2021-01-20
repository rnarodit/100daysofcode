from art import logo
def add (n1, n2):
    return n1 + n2

def subtract (n1 , n2):
    return n1 - n2

def multiply (n1 , n2):
    return n1 * n2


def divide (n1 , n2):
    if(n2 ==0 ):
        return "Can't multiply by zero"
    
    else:
        return n1 / n2

# storing funciton names in a dictionary 
operations = { 
    "+" : add ,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():# putting everything in a function to use recursion to restart the calculator if the user wants to do a fresh calculation
    print (logo)
    num1 = float(input ("What is the first number ?"))
    for operation in operations :
        print (operation)
    cont_calc = 'y'
    while cont_calc =='y':
        operation = input("which operation ? ")
        num2 = float(input ("What is the next number ?"))
        function = operations [operation]
        result= function (num1, num2)
        print (f"{num1} {operation} {num2} = {result}")
        cont_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ")
        if (cont_calc == 'y'):
            num1 = result
        else:
            calculator()
calculator()
        