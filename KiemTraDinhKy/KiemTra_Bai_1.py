"""
Nguyễn Thanh Hậu
MSSV: 24-0-00627
Kiểm tra định kỳ - Câu 1: Mô phỏng việc tung 2 xúc xắc 6 mặt
"""
import random

tiepTuc = True

# Mô phỏng việc tung 2 viên xúc xắc, mỗi viên có giá trị từ 1 đến 6.
# Input: Không có.
# Output: tuple (int, int): kết quả của 2 viên xúc xắc (x1, x2)
def tung_xuc_xac():
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)
    return x1, x2

# Hàm điều khiển chính. Cho phép người dùng chọn tiếp tục tung hoặc dừng lại.
# Input: không có
# Output: in ra kết quả tung và điều khiển vòng lặp người dùng
def main():
    while tiepTuc:
        ket_qua = tung_xuc_xac()
        print(f"Kết quả tung: Xúc xắc 1 = {ket_qua[0]}, Xúc xắc 2 = {ket_qua[1]}")
        tiep = input("Bạn có muốn tiếp tục tung? (y/n): ").strip().lower()
        if tiep == 'n':
            print("Kết thúc chương trình.")
            break
        elif tiep == 'y':
            continue
        else:
            print("bạn ghi sai mc định là tiếp tục ")

main()
