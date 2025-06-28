"""
nguyễn thanh hậu
chương 2 bài 11
tính tổng phần trăm
"""
PHAN_TRAM = 100
soLuongNam = int(input("nhap so luong nam : "))
soLuongNu  = int(input("nhap vao so luong nu : "))

phanTramNam = soLuongNam / (soLuongNam + soLuongNu) * 100
phanTramNu  = soLuongNu  / (soLuongNam + soLuongNu) * 100

print(f"so phan trăm nữ : {phanTramNu:.2f} , nam : {phanTramNam:.2f}")
