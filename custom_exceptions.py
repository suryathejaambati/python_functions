#raise Exception(" This is a exception")
#raise NameError(" Varibles are not defined")
'''
age=23
if age >30:
    print("Valida age")
else:
    raise valueError("Age is less than 30")
'''

age=20
try:
    assert age <30
    print("valid age")
except AssertionError:
    print("Raised with assert because age is less than 30")
except:
    print("Exception occured")
