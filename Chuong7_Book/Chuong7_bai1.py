"""
nguyen thanh hau
24-0-00627
chuong 7 bai 1
"""
import sys
sys.path.append("..")
from resource import res as a

MET_CHUAN = 140
PHI_CO_SO = 4
PHI_DI_CHUYEN = 0.25
QUI_DOI_KM = 1000

# ham chiu trach nhiem tinh tien
# input so km nguoi dung di duoc
# output thong tin sau khi da tinh toan tra ve
def tinhTien(soKm):
    doiKm = soKm * QUI_DOI_KM
    totalDiChuyen = (doiKm / MET_CHUAN) * PHI_DI_CHUYEN
    total = totalDiChuyen + PHI_CO_SO
    return totalDiChuyen ,total

def main():
    while True:
        try:
            userInputKm = float(input("nhap vao so km di duoc : "))
            tienDiChuyen , tongCong = tinhTien(userInputKm)
            print(f"tien di chuyen la : {round(tienDiChuyen)}")
            print(f"tien phai thanh toan la : {round(tongCong)}")
            a.tiepTuc()
        except ValueError as A:
            print(str(A))
main()