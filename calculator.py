# print("simple calculator")
 
# def add(a,b):
#     return a+b


# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# def get_remainder(a,b):
#     return a%b


# a=int(input("enter a number:"))
# b=int(input("enter another number"))
# print("enter operator :\n(+):for addition enter(1)\n(-):for subtraction enter(2) \n(*):for multiplication enter(3)\n(/):for division enter(4)\n(//) for get remainder(5)")
# op=int(input("enter operator:"))
# stop=int(input("enter 6 to exit"))



# def calculator():
#     if op==1:
        
#         result=add(a,b)
#         print(result)

#     elif op==2:
        
#         result=sub(a,b)
#         print(result)
#     elif op==3:
        
#         result=mul(a,b)
#         print(result)
#     elif op==4:
#         if b==0:
#             print("cannot divided by zero")
#         else:
#             result=div(a,b)
#             print(result)
#     elif op==5:
        
#         result=get_remainder(a,b)
#         print(result)
#     else:
#         print("invalid operator")    

# while True:
#     calculator()
#     if stop==6:
#         break



print("Simple Calculator 😎🔥")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def get_remainder(a, b):
    return a % b


def calculator(a, b, op):

    if op == 1:

        result = add(a, b)
        print(result)

    elif op == 2:

        result = sub(a, b)
        print(result)

    elif op == 3:

        result = mul(a, b)
        print(result)

    elif op == 4:

        if b == 0:
            print("Cannot divide by zero 😭🔥")

        else:
            result = div(a, b)
            print(result)

    elif op == 5:

        result = get_remainder(a, b)
        print(result)

    else:

        print("Invalid operator 😭🔥")


while True:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("""
1 -> Addition
2 -> Subtraction
3 -> Multiplication
4 -> Division
5 -> Remainder
""")

    op = int(input("Enter operator: "))

    calculator(a, b, op)

    stop = int(input("Enter 6 to exit or 0 to continue: "))

    if stop == 6:
        break