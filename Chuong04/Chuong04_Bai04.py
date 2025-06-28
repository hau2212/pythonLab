"""
nguyễn thanh hậu
24-0-00627
bài tính khoảng cách theo giờ
"""
import sys

khoangCach = 0
tocDO = 0
thoiGian = 0

# hàm tính khoảng cách
# input : thời gian di chuyển , và tốc độ di chuyển
# output : hiển thị khoảng cách môi giờ di chuyển được nhiêu
def tinhKhoangCach(thoiGIanDiChuyen , tocDoDiChuyen):
    global khoangCach
    for gio in range(1,thoiGIanDiChuyen+1):
        khoangCach += tocDoDiChuyen * 1
        print(f"khoảng cách mỗi giờ di chuyển được là : {khoangCach}")


# hàm chính chịu trách nhiệm nhập liệu và xử lý code
# input : các thông số tốc ộ và thời gian
# output : trả về thông tin lỗi
def main():
    try:

        thoiGian = int(input("hay nhap vao thoi gian ban di chuyen duoc : "))
        tocDO = int(input("hay nhap vao toc độ bạn di chuyển : "))
        tinhKhoangCach(thoiGIanDiChuyen=thoiGian,tocDoDiChuyen=tocDO)
        tiepTuc = input("ban co muon ket thuc chuong trình không n/y :").strip().lower()
        if tiepTuc == "n":
            sys.exit()
        elif tiepTuc == "y":
            main()
        else:
            print("ban nhập sai định dạng yêu cầu nhập lại ")
            tiepTuc = input("ban co muon ket thuc chuong trình không n/y :").strip().lower()
    except ValueError:
        print("loi")

main()