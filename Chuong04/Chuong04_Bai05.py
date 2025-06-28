"""
nguyen thanh hậu
24-0-00627
lượng mưa trung bình
"""
import sys

soNam = 0
soThang = 0
luongMuaHangThanh = 0

def tinhLuongMua(nam):
    luongMua = 0
    trungBinh =0
    for year in range(1,nam+1):
        for month in range(1,12+1):
            luongMua += float(input(f"nhap vao luong mua tháng {month} : "))

        trungBinh = luongMua  / 12
        print(f"lượng mưa trunh bình của năm {year} là : {trungBinh}")

def main():
    try:
        soNam = int(input("nhap vao so nam muon tinh:"))

        tinhLuongMua(nam=soNam)
        tiepTuc = input("ban co muon tiep tuc khong y/n : ")
        if tiepTuc == "n":
            sys.exit()
        elif tiepTuc == "y":
            main()
        else:
            print("ban nhap sai định dạng nhập lai ")
            tiepTuc = input("ban co muon tiep tuc khong y/n : ")

    except ValueError:
        print("chu y nhap vao dung dinh dang")
        main()

main()