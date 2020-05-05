import re
'''
text="This is a string this is function this"
my_pat=r"this"
print(re.findall(my_pat,text,re.I))
'''

text='''This is as string
    this is first line
    this is Secondline
    sdfdfs end'''
#my_pat=r"this"
my_pat=r"end$"
print(re.findall(my_pat,text,re.M|re.I))

