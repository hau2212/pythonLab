"""
nguyen thanh hau
24-0-00627
bai 5 chuong 6
tinh tong cac so , va doc nó
"""
import os.path

Cur_dir = current_dir = os.path.dirname(os.path.abspath(__file__))
h = os.path.join(Cur_dir,"Ch6")

def tinhSoNguyen(fileName):
    total = 0
    with open(os.path.join(h,fileName)) as file:
        for line in file:
            print(line)
            total += int(line)
        print(f"tong cong : {total}")

tinhSoNguyen("numbers.txt")