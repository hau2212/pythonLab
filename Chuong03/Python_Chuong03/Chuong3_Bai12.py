"""
nguyễn thanh hậu
Bài 13 chương 3
Tính tiền mua phần mêm
"""

# Hằng số
GIA_SAN_PHAM = 99

# Nhập số lượng sản phẩm từ người dùng
soLuongSanPham = int(input("Nhập vào số lượng sản phẩm mua: "))

# Tính tổng giá gốc
giaGoc = soLuongSanPham * GIA_SAN_PHAM

# Xác định tỷ lệ giảm giá
if 10 <= soLuongSanPham <= 19:
    tyLeGiam = 0.10
elif 20 <= soLuongSanPham <= 49:
    tyLeGiam = 0.20
elif 50 <= soLuongSanPham <= 99:
    tyLeGiam = 0.30
elif soLuongSanPham >= 100:
    tyLeGiam = 0.40
else:
    tyLeGiam = 0.0

# Tính số tiền giảm và tổng tiền sau khi giảm
soTienGiam = giaGoc * tyLeGiam
tongThanhToan = giaGoc - soTienGiam

# Hiển thị kết quả
print(f"Số tiền giảm giá là: ${soTienGiam:,.2f}")
print(f"Tổng tiền phải thanh toán là: ${tongThanhToan:,.2f}")
