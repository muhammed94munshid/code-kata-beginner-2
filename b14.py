x=int(input("Enter the lower limit for the range:"))
y=int(input("Enter the upper limit for the range:"))
for i in range(x,y+1):
    if(i%2!=0):
        print(i)
