"""
nguyen thanh hau
24-0-00627
bai 3 chuong 6
hien thi so dong voi noi dung
"""
import sys
import os
import pathlib as PaCk

d = os.path.join(os.path.dirname(os.path.abspath(__file__)),"Ch6")

def hienThi(fileName):
    filePath = os.path.join(d,fileName)
    with open(filePath, "r") as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}: {line.strip()}")


hienThi("numbers.txt")

