"""
nguyen thanh hau
24-0-00627
chuong 6 bai 6
tinh trung binh
"""
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(cur_dir,"CH6")

def tinhTrungBinh(fileName):
    total =0
    with open(os.path.join(full_path,fileName)) as file:
        for line in file:
            total += int(line)
        print(f" trung binh la  : {total/3}")

tinhTrungBinh("numbers.txt")