"""
Nguyễn thanh hậu
24-0-00627
chương 7 bài 1
"""
import sys
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.abspath(os.path.join(current_folder, ".."))
res1_path = os.path.join(parent_folder, "Res1")

if res1_path not in sys.path:
    sys.path.append(res1_path)

import res as Res

# Hàm chịu trách nhiệm tính trung vị của 3 số
# Input : ba số a, b, c (kiểu float hoặc int)
# Output : giá trị trung vị
def tinhTrungVi(a, b, c):
    danh_sach = [a, b, c]
    danh_sach.sort()
    trung_vi = danh_sach[1]  # phần tử ở giữa
    return trung_vi

# Hàm chịu trách nhiệm nhận một số từ người dùng
# Input : tên biến cần nhập (dạng chuỗi)
# Output : giá trị số hợp lệ mà người dùng nhập vào
def layDuLieu(ten):
    try:
        duLieu = float(input(f"Nhập giá trị cho {ten}: "))
        return duLieu
    except ValueError:
        print("⚠️ Sai định dạng, vui lòng nhập một số.")
        return layDuLieu(ten)

# Hàm chịu trách nhiệm chính cho logic, gọi các hàm con
# Input : không có
# Output : không có
def main():
    tiepTuc = True
    while tiepTuc:
        print("\n👉 Nhập 3 số để tính trung vị:")
        a = layDuLieu("a")
        b = layDuLieu("b")
        c = layDuLieu("c")
        print(f"Giá trị trung vị là: {tinhTrungVi(a, b, c)}")

        # Hỏi người dùng có muốn tiếp tục không
        Res.tiepTuc()

# Gọi hàm chính
main()
