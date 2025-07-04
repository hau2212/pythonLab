"""
nguyen thanh hau
24-0-00627
tinh khoang cach bi té xuống
"""
import tiep_tuc as t
import ma_mau as m

flag = True
G = 9.8
TY_LE = 1/2

# Hàm tính toán khoảng cách rơi
# Input thời gian tính theo giây
# output về khoảng cách
def tinhToan(t):
    d = TY_LE * G * (t**2)
    return d

# Hàm xử lý chính
# Output thông tin sau khi đã tính toán
def main():
    while flag:
        try:
            thoiGian = float(input("nhap vao thoi gian : "))
            met = tinhToan(t=thoiGian)
            print(m.mauChu["trang"][0]+f"{thoiGian} tương ứng với {met} M"+m.mauChu["trang"][1])
            t.tiepTuc()
        except ValueError as A:
            print(str(A))

if __name__ == "__main__":
    main()