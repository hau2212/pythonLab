"""
Nguyễn thanh hậu
chương 2 bài 13
tính hàng cây
"""
# Nhập dữ liệu từ người dùng
r = float(input("Nhập chiều dài của hàng (feet): "))
e = float(input("Nhập không gian mỗi trụ cuối (feet): "))
s = float(input("Nhập khoảng cách giữa các dây nho (feet): "))

# Tính số lượng cây nho phù hợp
v = (r - 2 * e) / s

# Hiển thị kết quả
print(f"Số lượng cây nho có thể trồng trong mỗi hàng là: {int(v)} cây")
