

def my_function1():
    x=456 #This is define as local variable and it can be applicable for this funtion only
    print("Welcome to functions")
    print("x value of fun1 is : ",x)
    #my_function2()
    return None

def my_function2(x):  # parameter
    print(" Thank you...! ")
    print("x values of fun2 is : ",x)
    return None

def main():
    #global x  # This is define as global variable and it can be applicable for all functions
    x=5
    my_function1()
    my_function2(x) #Argument
    return None
main()











