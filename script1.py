def add(x,y):
    result=x+y
    print(f"The result is : ",result)
    return None
def sub(m,n):
    result=m-n
    print(f"The result is : ",result)
    return None
def main():
    a=10
    b=4
    add(a,b)
    sub(a,b)
    return None
#if _name_ == "_main_":
if __name__=='__main__':
    main()

