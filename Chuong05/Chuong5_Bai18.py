"""
nguyen thanh hau
bai 18 chuong 5

"""
import Chuong5_Bai17 as C
import ma_mau as m

def main():
    for num in range(1,100+1):
        if C.is_prime(num):
            print(m.mauChu["tim"][0]+f"{num} la so nguyen to "+m.mauChu["tim"][1])
        else:
            print(m.mauChu["do"][0]+f"{num} khong phai so nguyen to"+m.mauChu["do"][1])

if __name__ == '__main__':
    main()