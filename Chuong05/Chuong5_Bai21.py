"""
nguyen thanh hau
24-0-00627
chuong 5 bai 21
keo bua bao
"""
import ma_mau as m
import tiep_tuc as t
import random
flag = True
dic = {1:"keo",2:"bua",3:"bao"}


def ketQua(user , pc):
    match user:
        case 1:
            match pc:
                case 1:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : hoa "
                case 2:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : may thang"
                case 3:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : ban thang"
        case 2:
            match pc:
                case 1:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : ban thang "
                case 2:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : hoa "
                case 3:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : may thang "
        case 3:
            match pc:
                case 1:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : may thang "
                case 2:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : ban thang "
                case 3:
                    return f"ban chon {dic[user]} may chon {dic[pc]} : hoa "
def main():
    while flag:
        try:
            may = lambda: random.randint(1, 3)
            print("**** chon keo , bua , bao tuong ung 1 , 2 , 3 ****")
            nguoiChon = int(input("chon 1 , 2, 3 : "))
            print(m.mauChu["vang"][0]+ketQua(user=nguoiChon,pc=may())+m.mauChu["vang"][1])
            t.tiepTuc()
        except ValueError as A:
            print(str(A))



if __name__ == '__main__':
    main()