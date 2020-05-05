'''
a=eval(input("enter a value is : "))
b=eval(input("enter b value is : "))
result=a*b
print(f"The value of {a} and {b} is : {result}")
'''

def multi(x,y):
    #result=x*y
    #print(f"The value of {x} and {y} is : {result}")
    #return result
    return x*y
def main():
    a=eval(input("enter a value is : "))
    b=eval(input("enter b value is : "))
    #multi(a,b)
    result=multi(a,b)
    print(f"The result  is : {result}")
    return None
main()






