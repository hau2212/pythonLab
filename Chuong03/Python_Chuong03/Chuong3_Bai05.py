"""
nguyen thanh hau
chuong 3 bai 6
tinh khoi luong
"""

NEWTON = 9.8
trongLuong = 0

khoiLuong = float(input("nhap vao khoi luong KG : "))
trongLuong = khoiLuong * NEWTON

if trongLuong >= 500:
    print(f"vat co trong luong {trongLuong:.2f} qua nang")
elif trongLuong <= 100:
    print(f"vat co trong luong {trongLuong:.2f} qua nhe")
else:
    print(f"vat co trong luong {trongLuong:.2f} binh thuong ")