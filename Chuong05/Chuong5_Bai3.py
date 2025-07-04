"""
nguyen thanh hau
24-0-00627
bai 3 chuong 5
tinh tien bao hiem
"""

CONT = True
PHAN_TRAM_BAO_HIEM = 0.8

# Hàm tính bảo hiểm
# Input là chi phí người dùng nhập vào
# Output là tiền bảo hiểm trả về
def tinhBaoHiem(chiPhi):
    total = chiPhi * PHAN_TRAM_BAO_HIEM
    return total

def main():
    while CONT:
        try:
            userInput = float(input("nhap vao so tien muon tinh Bao hiem : "))
            print(f"{tinhBaoHiem(userInput):.2f} USD" )
            tiepTuc = str(input("ban muon tiep tuc n/y : ")).lower()
            if tiepTuc == "n":
                return
            elif tiepTuc == "y":
                continue
        except ValueError as A:
            print("ban bi loi "+ str(A))


if __name__ == '__main__':
    main()