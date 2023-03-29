NiemYet=input('Nhap Gia niem yet: ')

ChietKhau=input('Nhap Chiet khau: ')

VAT=(float(NiemYet)-float(ChietKhau))*0.01
GiaBan= float(NiemYet)-float(ChietKhau)+float(VAT)
print('Gia ban:', GiaBan) 