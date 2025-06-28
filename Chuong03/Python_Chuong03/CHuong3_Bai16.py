"""
Nguyen Thanh Hau
Bai 16 Chuong 3
Kiem tra so ngay cua thang Hai
"""

# Nhập năm từ người dùng
nam = int(input("Nhập một năm: "))

# Kiểm tra năm nhuận theo quy tắc
if nam % 100 == 0:
    if nam % 400 == 0:
        soNgay = 29
    else:
        soNgay = 28
elif nam % 4 == 0:
    soNgay = 29
else:
    soNgay = 28

# In kết quả
print(f"Năm {nam} tháng 2 có {soNgay} ngày.")
