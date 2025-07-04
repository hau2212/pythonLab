"""
nguyen thanh hau
bai 20 chuong 5
doan so
"""
import random
import tiep_tuc as t
import ma_mau as m
flag = True

def soNgauNhien():
    number = random.randint(1,100)
    return number

def main():
    soRandom = soNgauNhien()

    while flag:

        print(soRandom)
        soDoan = int(input(m.mauChu["vang"][0]+"nhap vao so doan 1 --- 100 : "+m.mauChu["vang"][1]))
        if soDoan < soRandom:
            print(m.mauChu["xanh_duong"][0]+"nho hon"+m.mauChu["xanh_duong"][1])
            continue
        elif soDoan > soRandom:
            print(m.mauChu["xanh_la"][0]+"lon hon "+m.mauChu["xanh_la"][1])
            continue
        else:
            print("chuc mung")
            soRandom = soNgauNhien()

        t.tiepTuc()

if __name__ == '__main__':
    main()