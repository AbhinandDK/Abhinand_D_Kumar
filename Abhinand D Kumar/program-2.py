a=int(input("enter a number:"))

x=a+(a-1)

for i in range(0,x):
    for j in range(i,i+1):
        if j%2!=0:
            print(j,end=',')
print(j+1)
