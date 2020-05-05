'''
num=eval(input("Enter your Number: "))
result=num+10
print(f"your result is : {result}")
'''
def get_result(value): # parameter/positional arguments
    result=value+10
    print(f"your result is : {result}")    
    return None
def main():
    num=eval(input("Enter your Number: "))
    get_result(num) # Arguments

main()
