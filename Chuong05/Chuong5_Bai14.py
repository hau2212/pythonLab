"""
nguyen thanh hau
24-0-00627
bai 14 chuong 5
tinh dong nang
"""
import tiep_tuc as t
import ma_mau as m

flag = True

TY_LE = 1/2

def tinhKhoiLuong(M , V):
    dongNang = TY_LE * M * (V**2)
    return dongNang

def main():
    while flag:
        try:
            khoiLuong = float(input("nhap vao khoi luong : "))
            vanToc = float(input("nhap vao van toc : "))
            dongNang = tinhKhoiLuong(M=khoiLuong,V=vanToc)
            print( m.mauChu["do"][0]+f" dong nang la : {dongNang}"+m.mauChu["do"][1])
            t.tiepTuc()
        except ValueError as A:
            print(str(A))
if __name__ == '__main__':
    main()