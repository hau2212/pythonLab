"""
nguyên thanh hậu
24-0-00627
tinh thue tren gia tri bat dong san
"""
PHAN_TRAM_DANH_GIA = 0.6
PHAN_TRAM_TINH_THUE = 100
TY_GIA_THUE_TAI_SAN = 0.72

# Hàm tính thuế
# input giátriji gốc bất động sản
# output giá trị đã tính thuế
def tinhThue(giaTriGoc):
    total = giaTriGoc * PHAN_TRAM_DANH_GIA
    total = total / PHAN_TRAM_TINH_THUE
    total = total * TY_GIA_THUE_TAI_SAN
    return total

# Hàm chịu trách nhiệm trính logic
def main():
    while True:
        try:
            giaTri = float(input("nhap vao gia tri thuc te bat dong san : "))
            print(f"{tinhThue(giaTri):.0f} USD")
            tiepTuc = str(input("ban muon tiep tuc khong n/y : "))
            if tiepTuc == "n":
                break
            elif "n" != tiepTuc != "y":
                print("ban nhap sai mac dinh tiep tuc ")


        except ValueError as A:
            print(str(A))

main()