"""
nguyen thanh hau
24-0-00627
bai 16 chuong 5
dem so chan le
"""
import random
tongCong = []
listChan = []
listLe = []

def tinhSoChanLe():
    for num in range(100):
        number = random.randint(1,100)
        tongCong.append(number)
        if number % 2 == 0:
            listChan.append(number)
        else:
            listLe.append(number)
    print(f" day la list chan : {listChan}")
    print(len(listChan))
    print(f"day la list le :{listLe}")
    print(len(listLe))
    print(f"day la tat ca :{tongCong}")

tinhSoChanLe()

