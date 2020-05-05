import re
'''
text="This is pythonnnn aaa language and python is simple aaa and python is easy xyzaaaaaaaaaa"
#my_pat=r"\bpython{4}\b"
#my_pat=r"\ba{3}\b"
my_pat=r"\bxyza{10}\b"
print(re.findall(my_pat,text))
'''

text="xaz asdfa sdf xaaz xaaaaaaaz xaaaaz  xz"
#my_pat=r"\bxa{2}z\b"
#my_pat=r"\bxa{1}z\b"
#my_pat=r"\bxa*z\b"
my_pat=r"\bxa?z\b"
print(re.findall(my_pat,text))

