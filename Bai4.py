a=input('a=')
b=input('b=')
c=input('c=')

s=((float(a)+float(b)+float(c))/2)

import math
Dientich=math.sqrt(s*(s-float(a))*(s-float(b))*(s-float(c)))
print('Dien tich=',Dientich,sep="")