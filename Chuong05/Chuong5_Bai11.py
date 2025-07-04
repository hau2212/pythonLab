"""
nguyễn thanh hậu
24-0-00627
random cau hỏi số
"""
import random
import ma_mau as m
import tiep_tuc as t

SO_CAU_HOI = 5
KHOANG_CANH = 10

def xuLy():
    while True:
        for num in range(1,SO_CAU_HOI+1):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)

            total = int(input(f"{num1} + {num2} : "))
            if total == (num1+num2):
                print(m.mauChu["xanh_duong"][0]+" Đúng rồi "+m.mauChu["xanh_duong"][1])
            else:
                print(m.mauChu["do"][0] + " Sai rồi " + m.mauChu["do"][1])
        t.tiepTuc()

xuLy()
