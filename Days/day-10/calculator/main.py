from logo import logo

#functions

def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2


#dictionary with keys operation

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":division
}

def calculator():
    print(logo)
    num1 = float(input(f"Cual es el primer numero?: "))
    for sign in operations:
        print(sign)
    should_continue = True
    
    while should_continue:
        op = input("Cual es la operacion que deseas hacer?: ")
        num2 = float(input(f"Cual es el proximo numero?: "))
        calculo = operations[op]
        answer = calculo(num1,num2)
        state = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if state == "y":
            num1=answer
        else:
            should_continue = False
            print(f"{num1} {op} {num2} = {answer}")
            calculator() #recursive function, be careful and set a condition, if not, will be a infinite loop
calculator()
