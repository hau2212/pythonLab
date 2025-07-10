"""
nguyen thanh hau
24-0-00627
chuong 6 bai 1
hien thi file numbers.txt
"""
import sys
sys.path.append("..")
from resource import res as e
flag = True



def hienThi():
    global file
    try:

        file = open("Ch6/numbers.txt","r")
        hau = file.read()
    except Exception as a:
        print(str(a))
    finally:
        return hau
        file.close()

# ham chinh goi main

def main():
    try:
        print(hienThi())
    except Exception as e:
        print(str(e))
main()