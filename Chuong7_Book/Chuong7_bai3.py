"""
nguyen thanh hau
24-0-00627
chuong 7 bai 1
"""

import sys
import math
sys.path.append("..")
from resource import res as M


# Hàm chịu trách nhiệm kiểm tra số nguyên tố
# Input: một số nguyên dương n
# Output: True nếu là số nguyên tố, False nếu không
def laSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm chịu trách nhiệm nhận một số nguyên từ người dùng
# Input: không có
# Output: số nguyên hợp lệ
def getInput():
    try:
        userInput = int(input("Nhập một số nguyên để kiểm tra: "))
        if userInput < 0:
            print("⚠️ Vui lòng nhập số nguyên dương.")
            return getInput()
        return userInput
    except ValueError:
        print("⚠️ Vui lòng chỉ nhập số nguyên.")
        return getInput()

# Hàm chịu trách nhiệm chính cho logic, gọi các hàm con
def main():
    while True:
        n = getInput()
        if laSoNguyenTo(n):
            print(f"✅ {n} là số nguyên tố.")
        else:
            print(f"❌ {n} không phải là số nguyên tố.")

        # Hỏi người dùng có muốn tiếp tục không
        M.tiepTuc()
# Gọi hàm chính
main()
