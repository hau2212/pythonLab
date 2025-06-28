"""
Nguyen thanh hau
bai 2 chuong 3
tinh dien tich hai hinh chu nhat va so sanh 
"""

tiepTuc = True

dienTichHinhA = 0
dienTichHinhB = 0 

def calculateSquare(numberOne , numberTwo):
    total = numberOne * numberTwo
    return total


#hien thi 
print("\n"*20)
while tiepTuc:
    try:
# lay gia tri nguoi dung cho dien tich A
        chieuDaiA = float(input("nhập vào chieu dai A : "))
        chieuRongA = float(input("nhập vào chieu rong A : "))

    # lay gia tri nguoi dung cho dien tich B
        chieuDaiB = float(input("nhập vào chieu dai B : "))
        chieuRongB = float(input("nhập vào chieu rong B : "))
        
        dienTichHinhA = calculateSquare(numberOne=chieuDaiA,numberTwo=chieuRongA)
        dienTichHinhB = calculateSquare(numberOne=chieuDaiB,numberTwo=chieuRongB)
    except ValueError:
        print("nhap so hop le ")
        thoat = input("Bạn có muốn thoát không? (y/n): ")
        if thoat.lower() == 'y':
            print("Đã thoát chương trình.")
            break
if dienTichHinhA > dienTichHinhB:
    print("dien tich hinh A lon hon")
elif dienTichHinhB > dienTichHinhA:
    print("dien tich hinh B lon hon")
else:
    print("ca hai hinh A , B co dien tich bang nhau ")