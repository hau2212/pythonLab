"""
nguyễn thanh hậu
24-0-00627
bài 2 chương 7
"""
import random


def soNgauNhien():
    so_xo = []
    for _ in range(7):
        so_xo.append(random.randint(0,9))
    return so_xo

def main():
    soXo = []
    soXo = soNgauNhien()
    print(soXo)
main()