"""
Nguyen Thanh Hậu
Bài 1 - Chương 3
Kiểm tra số âm/dương, chẵn/lẻ
"""
tiepTuc = True

def kiemTraDuongAm(number):
    if number > 0:
        print( f"{number} la so dương")
    elif number < 0:
        print(f"{number} la so am")
    else:
        print( f"{number} la so khong")
    # kiemTraChanLe(number=number, result=a)


def kiemTraChanLe(number):
    if number % 2 == 0:
        print(f"Số {number} là số chẵn ")
    else:
        print(f"Số {number} là số lẻ ")

while tiepTuc:
    try:
        inputNumber = float(input("Nhập vào số muốn kiểm tra: "))
        kiemTraDuongAm(number=inputNumber)
        kiemTraChanLe(number=inputNumber)

    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")
        thoat = input("Bạn có muốn thoát không? (y/n): ")
        if thoat.lower() == 'y':
            print("Đã thoát chương trình.")
            break