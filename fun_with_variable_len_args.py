'''
def display(b):
    print(type(b))
    return None
#display(4)
display(4,5)
'''


def display(*arg):
    #print(type(arg))
    for each in arg:
        print(type(arg))
    return None
display("hi")
display(4,5,6,"hi")

