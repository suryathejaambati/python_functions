def get_add(x,y):
    result=x+y
    print(f"the value of {x} and {y} is: {result}")
    return None
def get_sub(m,n):
    result=m-n
    print(f"the value of {m} and {n} is: {result}")
    return None
def main():
    a=eval(input("Enter a value is : "))
    b=eval(input("Enter b value is : "))
    get_add(a,b)
    get_sub(a,b)
    return None

main()











