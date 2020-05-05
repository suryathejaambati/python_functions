import re
my_str="This is python language and it consists Python2 and python3 versions"
#my_pat=r'python'
my_pat=r"\bpython[23]?\b"
#print(re.split(my_pat,my_str,maxsplit=2,flags=re.I))
#print(re.sub(my_pat,"shell",my_str,count=2,flags=re.I))
print(re.subn(my_pat,"shell",my_str,flags=re.I))
