'''
a=eval(input("Enter a value : "))
b=eval(input("Enter b value: ")
result=a/b
print(f"the value of {a} and {b} is : {result}")
'''
'''
try:
    #print(f"the value of 4 and 2 is : {4/2}")
    print(4/0)
except:
    print(f"Zero division error")

# This is called Zero division  error
'''

'''
fo=open("surya.txt","r")
print(fo.read())
'''
'''
try:
    fo=open("random.txt","r")
    print(fo.read())
    fo.close()
except:
    print(" File not found exception")

# This is call File not found error 
'''
'''
try:
    fo=open("surya.txt","r")
    print(fo.read())
    fo.close()
except Exception as e: # This way define the exceptions in realtime 
    print(e)
'''
'''
my_list=[3,4,5]
#print(my_list[1])
#print(my_list[4])

try:
    print(my_list[4])
except Exception as e:
    print(e)

#This is called index error
'''
'''

Error Types:
Index Error
Zero Divison Error
Import error
Value Error
Type Error
Name Error
File not found error
IO Error
'''




try:
    import fabric
except Exception as e:
    print(e)

