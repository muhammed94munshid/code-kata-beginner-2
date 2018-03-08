#program for simple intrest
# i=intrest
# p=investment
# r=rate of intrest
# t=time duration
p=float(input("investment:"))
r=float(input("rate of intrest:"))
t=float(input("time duration :"))
r=(r/100)
i=p*r*t
i=i+p
print("simpe intrest for",p,"investmentin intrest rate of",r,"in years",t,"is",i)
