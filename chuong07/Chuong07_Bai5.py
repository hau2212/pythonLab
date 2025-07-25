"""
nguyễn thanh hậu
24-0-00627
chuong 7 bài 5 : doc so tai khoan trong file
"""


def kiemTra(tempt_taiKhoan , tempt_taiKhoanThanhToan):
    return tempt_taiKhoanThanhToan in tempt_taiKhoan


def main():
    try:
        taiKhoan = []
        tempt = ""
        with open("Chương 07\charge_accounts.txt","r") as file:
            for tempt in file:
                taiKhoan.append(tempt.strip("\n"))
            while True:
                taiKhoanThanhToan = str(input("nhap vao so tai khoan thanh toan cua ban : "))
                if kiemTra(tempt_taiKhoan=taiKhoan,tempt_taiKhoanThanhToan=taiKhoanThanhToan):
                    print("Da thanh toan thanh cong ")
                else:
                    print("so khong hop le vui long nhap lai")
                tiepTuc = input("ban muon tiep tuc khong y/n ; ").strip().lower()
                if tiepTuc == "n":
                    break
                else:
                    print("tiep tuc ")

            print(taiKhoan)
    except Exception as Ex:
        print(str(Ex))


if __name__ == '__main__':
    main()