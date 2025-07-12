"""
nguyen thanh hau
24-0-00627
chuong 6 bai 2
chuong trinh nguoi dung nhap ten file va hien thi 5 dong
"""
import sys
sys.path.append("..")
from resource import res as ea
import os
ea.tiepTuc()

def hienThi(fileName):
    try:
        base_path = os.path.dirname(__file__)
        full_path = os.path.join(base_path, "Ch6", fileName)

        with open(full_path, "r") as file:
            for _ in range(5):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except Exception as e:
        print("Lỗi:", e)

hienThi("numbers.txt")