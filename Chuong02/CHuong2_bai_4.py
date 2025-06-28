# Thuế bán hàng
import sys

TAX_RATE = 0.07
firstTime = True
goods = {"a":0,"b":0,"c":0,"d":0,"e":0}


def calculator():
    global firstTime
    goods_total = 0
    for key in goods:
        goods[key] = float(input("nhap vao gia tri "))

    for value in goods.values():
        goods_total += value

    goods_total += goods_total * TAX_RATE

    print("gia tri sau khi tinh bao gồm 7% TAX la :")
    print(goods_total)
    if (input("ban co mon tiep tuc khong Y/N")) != "Y":
        firstTime = False


while firstTime == True:
    calculator()
else:
    sys.exit()