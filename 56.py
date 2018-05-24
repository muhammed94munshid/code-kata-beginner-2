str=input()
try:
    str==str.alpha()+str.numeric()
except AttributeError:
    print("yes")
else:
    print("no")
