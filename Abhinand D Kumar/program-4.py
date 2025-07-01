a=[]
x=[1,2,3,4,5,6,7,8,9]
result={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
count=0
n=int(input('enter the range : '))
for i in range(n):
    a.append(int(input("enter the number : ")))
    
print(a)
for i in x:
    for j in a:
        if j%i==0:
            
            count+=1
        result[i]=count
    count=0
        
        
print(result)

