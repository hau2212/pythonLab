"""
nguyen thanh hau
24-0-00627
chuong 7 bai 1
"""

import sys

sys.path.append("..")
from resource import res as M

import sys

# Hàm chịu trách nhiệm tính trung vị của 3 số
# Input : ba số a, b, c (kiểu float hoặc int)
# Output : giá trị trung vị
def tinhTrungVi(a, b, c):
    danh_sach = [a, b, c]
    danh_sach.sort()
    trung_vi = danh_sach[1]  # phần tử ở giữa
    print(f"Giá trị trung vị là: {trung_vi}")
    return trung_vi

# Hàm chịu trách nhiệm nhận một số từ người dùng
# Input : tên biến cần nhập (dạng chuỗi)
# Output : giá trị số hợp lệ mà người dùng nhập vào
def getInput(ten):
    try:
        userInput = float(input(f"Nhập giá trị cho {ten}: "))
        return userInput
    except ValueError:
        print("⚠️ Sai định dạng, vui lòng nhập một số.")
        return getInput(ten)

# Hàm chịu trách nhiệm chính cho logic, gọi các hàm con
# Input : không có
# Output : không có
def main():
    while True:
        print("\n👉 Nhập 3 số để tính trung vị:")
        a = getInput("a")
        b = getInput("b")
        c = getInput("c")
        tinhTrungVi(a, b, c)

        # Hỏi người dùng có muốn tiếp tục không
        M.tiepTuc()

# Gọi hàm chính
main()
