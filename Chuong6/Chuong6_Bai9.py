
"""
nguyen thanh hau
24-0-00627
chuong 6 bai 6
tinh trung binh
"""

import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(cur_dir, "CH6")

def tinhTrungBinh(fileName):
    try:
        total = 0
        count = 0

        with open(os.path.join(full_path, fileName)) as file:
            for line in file:
                try:
                    number = int(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    print(f"Bỏ qua dòng không hợp lệ: {line.strip()}")

        if count > 0:
            print(f"Trung bình là: {total / count}")
        else:
            print("Không có dữ liệu hợp lệ để tính trung bình.")

    except IOError as e:
        print(f"Lỗi khi đọc file: {e}")

tinhTrungBinh("numbers.txt")
