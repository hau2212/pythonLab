"""
nguyen thanh hau
24-0-00627
tính lương để trả
"""

SALARY = 1

def tinhLuong(day):
    total = 0
    for ngay in range(1,day+1):
        total += ngay * SALARY