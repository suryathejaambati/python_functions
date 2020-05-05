
#print(a) # Name Error
#print(4+ "hi") #Type Error
#print("surya.txt") #File not found Error
#print(4/0) # Zero division error

'''
try:
    print("Exceptions Handling")
    #print(a)
    #print(4+ "hi")
    #print("surya.txt")
    #print(4/0)
    import fabric
except NameError:
    print(" Variables is not define")
except TypeError:
    print("Adding Num and strings is not possible")
except FileNotFoundError:
    print("File is not available")
except ZeroDivisionError:
    print("Division with zero is not possible")
except ModuleNotFoundError:
    print("please install fabric package")
except Exception as e:
    print(e)
finally:
    print("Finally this will execute the statement")

'''

try:
    print("Exceptions Handling")
    a=10
    print(a)
    #print(4+ "hi")
    #print("surya.txt")
    #print(4/0)
    #import fabric
except NameError:
    print(" Variables is not define")
except TypeError:
    print("Adding Num and strings is not possible")
except FileNotFoundError:
    print("File is not available")
except ZeroDivisionError:
    print("Division with zero is not possible")
except ModuleNotFoundError:
    print("please install fabric package")
except Exception as e:
    print(e)
else:
    print("This will excute if no exception")

