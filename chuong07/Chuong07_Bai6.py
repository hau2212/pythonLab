"""
nguyễn thanh hâu
24-0-00627
chuong 7 bài 6 so lan tung suc xac
"""
import random


def tungSucXac(tempt_soLanTung):
    tempt_ketQua = [random.randint(1,6) for _ in range(tempt_soLanTung)]
    return tempt_ketQua

def main():
    try:
        soLanTung  = int(input("so lan tung xuc sac : "))
        print(tungSucXac(soLanTung))
    except Exception as Ex:
        print(str(Ex))

main()