"""
nguyễn thanh hậu
chương 2 bai 14
tinh lai kep
"""
# Nhập thông tin từ người dùng
P = float(input("Nhập số tiền gốc ban đầu (VND): "))
r = float(input("Nhập lãi suất hàng năm (%, ví dụ: 5): ")) / 100
n = int(input("Nhập số lần lãi được gộp mỗi năm (ví dụ: 12 cho hàng tháng): "))
t = float(input("Nhập số năm gửi tiền: "))

# Tính lãi kép
A = P * (1 + r / n) ** (n * t)

# In kết quả
print(f"Số tiền sau {t} năm là: {A:,.2f} VND")
