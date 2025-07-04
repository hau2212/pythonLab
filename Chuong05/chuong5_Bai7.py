"""
nguyen thanh hau
24-0-00627
tinh gia ve cho ngoi san van dong
bai 7 chuong 5
"""
import ma_mau as m

VE_HANG_A = 20
VE_HANG_B = 15
VE_HANG_c = 10


# Hàm tính tiền của từng hạng vé và tổng cộng
# Input số lượng vé bán được
# Output tổng tiền của từng loại vé và tổng cộng
def tinhTien(veA,veB,veC):
    totalA =  veA * VE_HANG_A
    totalB =  veB * VE_HANG_B
    totalC = veC * VE_HANG_c
    total = totalA + totalB + totalC
    return totalA , totalB , totalC , total

# Hàm chịu trách nhiệm logic
# Input từ người dùng
# Output thông tin cuối cùng cho người dùng
def main():
    while True:
        try:
            inputVeA = int(input("nhap vao so luong ve A : "))
            inputVeB = int(input("nhap vao so luong ve B : "))
            inputVeC = int(input("nhap vao so luong ve C : "))

            tongGiaVeA , tongGiaVeB , tongGiaVeC , tongCong = tinhTien(veA=inputVeA,veB=inputVeB,veC=inputVeC)
            print(f"tong so luong gia ve A là : {tongGiaVeA}")
            print(f"tong so luong gia ve B là : {tongGiaVeB}")
            print(f"tong so luong gia ve C là : {tongGiaVeC}")
            print(f"tong so luong gia ve là : {tongCong}")
            tiepTuc = str(input("ban muon tiep tuc khong n/y : "))
            if tiepTuc == "n":
                return
            elif "n" != tiepTuc != "y":
                print(m.mauChu["do"][0] +"ban da nhap sai chuong trinh se tiep tuc "+ m.mauChu["do"][1])


        except ValueError as A:
            print(str(A))
main()
