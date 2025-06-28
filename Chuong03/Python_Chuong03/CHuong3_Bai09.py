"""
nguyen thanh hau
bai 9 chuong 3
routele
"""



def ranDom(value):
    ketQua = "khong hop le"
    match value :
        case _ if 1 <= value <= 10:
            if value % 2 == 0:
                ketQua = "mau den"
            else:
                ketQua = "mau do"
        case _ if 11 <= value <= 18:
            if value % 2 == 0:
                ketQua = "mau do"
            else:
                ketQua = "mau den"
        case _ if 19 <= value <= 28:
            if value % 2 == 0:
                ketQua = "mau den"
            else:
                ketQua = "mau do"
        case _ if 29 <= value <= 36:
            if value % 2 == 0:
                ketQua = "mau den"
            else:
                ketQua = "mau do"
    return print(f"so ban chon la {ketQua}")

number = int(input("nhap so ban chon vao : "))
ranDom(value=number)