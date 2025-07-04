"""
nguyen thanh hâu
24-0-00627
chuong 5 bài 13
số lớn số bé
"""
import tiep_tuc as m
flag = True

def timSoLonHon(num1 , num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return "so bang nhau"
    else:
        return num2

def main():
    while flag:
        try:
            number1 = float(input("nhap vao so thu 1 : "))
            number2 = float(input("nhap vao so thu 2 : "))
            result = timSoLonHon(num1=number1,num2=number2)
            print(result)
            m.tiepTuc()
        except ValueError as A:
            print(str(A))

if __name__ == '__main__':
    main()