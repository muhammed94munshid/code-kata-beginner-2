h1=int(input())
m1=int(input())
h2=int(input())
m2=int(input())
t1=(h1*60)+m1
t2=(h2*60)+m2
t=t1-t2
th=t//60
tm=t%60
print("diffrence in time",th ,":",tm)
