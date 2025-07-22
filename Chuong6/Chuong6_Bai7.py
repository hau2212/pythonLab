"""
nguyen thanh hau
24-0-00627
chuong 6 bai 7
nhap tu vao mot tep
"""
import os.path

Cur_Dir = os.path.dirname(os.path.abspath(__file__))
Full_path = os.path.join(Cur_Dir,"Ch6")

def nhapTu(fileName):
    with open(fileName,"w") as file:
        text = input("ghi vao")
        file.write(text)

def main():
    tenFile = input("nhap vao ten file : ")
    nhapTu(tenFile)
main()