"""
Nguyen Thanh Hau
Chuong 5 - Bai 4
Tính chi phí phát sinh thêm
"""

def tinhChiPhi(tongChiPhi):
    totalMonth = tongChiPhi
    totalYear = tongChiPhi * 12
    return totalMonth, totalYear

def main():
    while True:
        try:
            chiPhi = []
            count = 1
            print("Nhập vào các chi phí hàng tháng (nhập 0 để kết thúc):")

            while True:
                gia = int(input(f"Chi phí {count}: "))
                if gia == 0:
                    break
                chiPhi.append(gia)
                count += 1

            if not chiPhi:
                print("Bạn chưa nhập chi phí nào.")
                continue

            tongThang = sum(chiPhi)
            chiPhiThang, chiPhiNam = tinhChiPhi(tongThang)

            print(f"\n👉 Chi phí một tháng: {chiPhiThang:,} VND")
            print(f"👉 Chi phí một năm  : {chiPhiNam:,} VND\n")

            dungLai = input("Bạn có muốn tiếp tục? (y/n): ").strip().lower()
            if dungLai == "n":
                print("Kết thúc chương trình.")
                break
            elif dungLai != "y":
                print("Bạn chọn sai, mặc định sẽ tiếp tục.\n")

        except ValueError as e:
            print("Lỗi: Bạn phải nhập một số nguyên.\n")

if __name__ == '__main__':
    main()
