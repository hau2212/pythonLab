"""
nguyen thanh hau
chuong 5 bai 8
tinh gia nhan cong  son
"""

FEET_CHUAN = 112
PHI_CHUAN_LAO_DONG = 35.00
GIO_CHUAN = 8

def tinhTien(feetOrigin , giaGallon):
    totalFeet = feetOrigin / FEET_CHUAN
    totalGiaLaoDong = (totalFeet * GIO_CHUAN) * PHI_CHUAN_LAO_DONG
    totalGallon = totalFeet * giaGallon
    return totalFeet , totalGiaLaoDong , totalGallon


def main():
    while True:
        try:
            userInputFeet = float(input("nhap vao feet can tinh : "))
            userInputFee = float(input("nhap vao gia moi gallon : "))

            feetCanXuLy , giaThanhToan , gallonCan = tinhTien(feetOrigin=userInputFeet , giaGallon=userInputFee)
            print(f"feet can phai xu ly la : {feetCanXuLy:.5f}")
            print(f"gia can phai tra la : {giaThanhToan:.5f}")
            print(f"gia cho {feetCanXuLy:.5f} gallon can co  la : {gallonCan:.5f}")
            tiepTuc = str(input("nhap tiepTuc n/y : "))
            if tiepTuc == "n":
                return
            elif "n" != tiepTuc != "y":
                print("nhap tiepTuc n/y")
        except ValueError as A:
            print(str(A))
if __name__ == '__main__':
    main()
