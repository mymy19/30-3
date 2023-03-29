a=input('Nhap hai canh ke cua tam giac vuong:')
ke1=input('')
ke2=input('')

import math
huyen=math.sqrt(float(ke1)**2 + float(ke2)**2)

print('Canh ke thu nhat la: ' + str(ke1) + ', canh ke thu hai: ' + str(ke2) + ', co canh huyen =', round(huyen,2))