"""
nguyen thanh hau
bai 3 chuong 4
tinh thoi gian moi vong dua
"""

soVong = 0
soPhutMoiVong = 0
minuteByLab = []
tiepTuc = True



# hàm tính tổng và tìm vòng chạy nhanh nhất , chậm nhất , và số vòng chạy được
# input : không có
# output : không có
def tinhTong():
    try :
        for num in range(1,soVong+1):

            print("\n"*20)
            minuteByLab.append(float(input(f"nhap vao thoi gian  vong so {num} duoc")))
    #tim vong chay nhanh nhat
        nhanhNhat = max(minuteByLab)
        nhanhNhatLab = minuteByLab.index(nhanhNhat)
        print(f"vong chay nhanh nhat là {nhanhNhatLab} : {nhanhNhat}")

    #tim vong chay cham nhat
        chamNhat = min(minuteByLab)
        chamNhatLab = minuteByLab.index(chamNhat)
        print(f"vong chay cham nhat la {chamNhatLab} : {chamNhat}")
    except vars():
        print("yeu cau nhập số không nhập chữ trên số vòng chạy được và số phút mỗi vòng ")
        tinhTong()

# xác nhận tiếp tục hoặc không , check đầu vào .
# input : số vòng , check n\y , bắt lỗi
# output : không có 
while tiepTuc:
    try :
        soVong = int(input("nhap vao so vong ban chay duoc"))
        tinhTong()
        check_tiepTuc = input("Tiếp tục hay không? (y/n): ").strip().lower()

        if check_tiepTuc == "n":
            tiepTuc = False
            print("Kết thúc chương trình.")
        elif check_tiepTuc != "y" or check_tiepTuc != "n":
            print("❗ Vui lòng nhập đúng định dạng (y/n).")
            check_tiepTuc = input("Tiếp tục hay không? (y/n): ").strip().lower()

            if check_tiepTuc == "n":
                tiepTuc = False
                print("Kết thúc chương trình.")
    except ValueError:
        print(f"chu y ban dinh loi {ValueError.args} chuong trinh bi beark ")
