"""
nguyen thanh hau
bai 3 chuong 3
tinh quy reong nam 
"""
thang = int(input("nhap vao so thang : "))

def tinhQuy(number):
    try:
        if 1 <= thang <= 3:
            print("quy 1")
        elif 4 <= thang <= 6:
            print("quy 2")
        elif 7 <= thang <= 9:
            print("quy 3")
        else:
            print("quy 4")
    except ValueError:
        print("nhap vao hop le")

tinhQuy(number=thang)