"""
nguyen thanh hau
chuong 3 bai 13
tinh phi van chuyen

"""
# Định nghĩa mức giá theo trọng lượng
GIA_TIEN_TYPE_1 = 1.50
GIA_TIEN_TYPE_2 = 3.00
GIA_TIEN_TYPE_3 = 4.00
GIA_TIEN_TYPE_4 = 4.75

# Giới hạn trọng lượng
POUND1 = 2
POUND6 = 6
POUND10 = 10

# Nhập trọng lượng từ người dùng
try:
    trongLuongGoiHang = float(input("Nhập trọng lượng gói hàng (pound): "))

    # Xác định giá dựa trên trọng lượng
    if trongLuongGoiHang <= POUND1:
        gia = GIA_TIEN_TYPE_1
    elif trongLuongGoiHang <= POUND6:
        gia = GIA_TIEN_TYPE_2
    elif trongLuongGoiHang <= POUND10:
        gia = GIA_TIEN_TYPE_3
    else:
        gia = GIA_TIEN_TYPE_4

    # Tính phí vận chuyển
    phiVanChuyen = gia * trongLuongGoiHang

    # Hiển thị kết quả
    print(f"Phí vận chuyển là: ${phiVanChuyen:.2f}")

except ValueError:
    print("Vui lòng nhập một số hợp lệ cho trọng lượng.")
