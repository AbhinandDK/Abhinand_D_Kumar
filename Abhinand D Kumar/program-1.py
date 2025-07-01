class calculator:
    
    def __init__(self,a:float,b:float,operator:str):
        self.a=a
        self.b=b
        self.operator=operator
        
    def calculate(self):
        
        if self.operator == 'add':
            
            return self.a + self.b
        
        elif self.operator == 'sub':
            
            return self.a - self.b
        
        elif self.operator =='mul':
            
            return self.a * self.b
        else:
            
            if self.b==0:
                raise ZeroDivisionError("Dinominator should not be zero")
            else:
                return self.a/self.b
            
operator=input("enter the operator addition: add, Subtraction : sub, Multiplication : mul, Division : div ? : ")
            
a=float(input("enter the first number"))
    
b=float(input("enter the second number"))
    
c= calculator(a, b, operator)
result=c.calculate()
    
print(result)
    
    
    
    