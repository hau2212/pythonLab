"""
nguyễn thanh hậu
Chương 2 bài 8
Tip, Tax , Total
"""
TAX = 0.07
TIP = 0.18
soTienTongCong = float(input("nhap vao so tien tong cong :"))
sohang = 0
total = 0

goods = {}
sohang = int(input("nhap vao so luong hang"))

for number in range(sohang):
    tenHang = input(f"nhap vao ten hang hoa thu {number+1} : ")
    soLuong = int(input("nhap vao so luong : "))
    donGia  = float(input("nhap vao don gia :"))

    goods[tenHang] = (soLuong,donGia)


for value,(donGia,soLuong) in goods.items():
    total += donGia * soLuong

sauThue = total * TAX
sauTip  = total * TIP
print("\n"*20)
print(f"gia tri thanh tien hang hoa la : {total}")
print(f"so tien thue 7% là             : {sauThue:.2f}")
print(f"so tien sau TIp 18% là         : {sauTip:.2f}")
print(f"can phai thanh toan la         : {total + sauTip + sauThue}")