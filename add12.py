class Numbers:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def __add__(self1,self2):
        return self1.__class__(self1.x+self2.x, self1.y+self2.y)
    
    def __sub__(self1,self2):
        return self1.__class__(self1.x-self2.x, self1.y-self2.y)
    
    def __mul__(s1,s2):
        return s1.__class__(s1.x*s2.x, s1.y*s2.y)
    
    def __truediv__(s1,s2):
        return s1.__class__(s1.x/s2.x, s1.y/s2.y)
    
s1 = Numbers(56,25)
s2 = Numbers(300,70)
s3= Numbers(56,82)
s4 = Numbers(85,72)
add = s1+s2+s3+s4
print(add)
print(add.x)

sub1 = s1-s2-s3-s4
print(sub1)
print(sub1.x)

mul1 = s1*s2*s3*s4
print(mul1)
print(mul1.x)

div1 = s1/s2/s3/s4
print(div1)
print(div1.x)