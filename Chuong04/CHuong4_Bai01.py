"""
nguyen thanh hau
24-0-00627
tinh loi
"""

def tinhLoiMoiNgay(ngay):
    total = 0
    for num in range(1, ngay + 1):
        while True:
            try:
                loi = int(input(f"Nhập vào số lỗi ngày {num}: "))
                if loi < 0:
                    print("Số lỗi không thể là số âm. Nhập lại.")
                    continue
                total += loi
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên.")
    print(f"Tổng số lỗi của {ngay} ngày là: {total}\n")

# Vòng lặp chính
tiepTuc = True

while tiepTuc:
    try:
        soNgay = int(input("Nhập vào số ngày cần tính lỗi: "))
        if soNgay <= 0:
            print("Số ngày phải lớn hơn 0.")
            continue
        tinhLoiMoiNgay(soNgay)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        continue

    try:
        cont = input("Bạn có muốn tiếp tục không? (y/n): ").strip().lower()
    except ValueError:
        print("nhap vao dung dinh dang chi n/y :")
    if cont == "n":
        tiepTuc = False
        print("Kết thúc chương trình.")
