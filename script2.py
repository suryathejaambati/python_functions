import script1
def multi(j,q):
    result=j*q
    print("The result is : ",result)
    return None
def main():
    a=10
    b=20
    multi(a,b)
    script1.add(a,b)
    script1.sub(a,b)
    return None
#if _name_ == '_main_':
if __name__=='__main__':
    main()
    

