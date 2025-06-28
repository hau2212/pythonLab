"""
Nguyen Thanh Hau
Bai 14 Chuong 3
Tinh can nang va chieu cao BMI
"""

BMI = 0
CONG_THUC = 703
canNang = 0
chieuCao = 0

# Nhập dữ liệu
canNang = float(input("Nhập vào cân nặng (pound): "))
chieuCao = float(input("Nhập vào chiều cao (inch): "))

# Tính BMI
BMI = canNang * CONG_THUC / (chieuCao ** 2)

# Kiểm tra kết quả BMI
if 18.5 <= BMI <= 25:
    print("Cân nặng của bạn tối ưu.")
elif BMI < 18.5:
    print("Bạn bị thiếu cân.")
else:
    print("Bạn bị thừa cân.")

print(f"Chỉ số BMI của bạn là: {BMI:.2f}")
