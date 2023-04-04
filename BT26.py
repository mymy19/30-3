Ten=input('Ho ten: ')
SoNgay=input('So ngay cong: ')
DonGia=input('Don gia ngay cong: ')
PhuCap=input('He so phu cap: ')
TamUng=input('Tam ung: ')

Luong=float(DonGia)*float(SoNgay)*float(PhuCap)
ThucLinh=Luong - float(TamUng)

print('Nhan vien '+ str(Ten)+', Co tien Luong='+ str(round(Luong,1))+', Tam ung='+str(TamUng)+' va Thuc linh='+str(round(ThucLinh,1)))
