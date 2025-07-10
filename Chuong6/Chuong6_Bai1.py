"""
Nguyễn thanh hậu
24-0-00627
chuong 6 bai 1
hien thi file numbers.txt
"""

# hàm dùng để hiện thị
# trả về nội dung file
def hienThi():
    try:
        with open("Ch6/numbers.txt", "r") as file:
            hau = file.read()
        return hau
    except Exception as a:
        print(str(a))
        return "Không thấy file"

# Hàm logic chính
# output terminal thông tin trong file
def main():
    try:
        print( hienThi() )
    except Exception as e:
        print(str(e))

main()
