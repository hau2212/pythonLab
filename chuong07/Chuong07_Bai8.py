"""
nguyen thanh hau
24-0-00627
chuong 7 bai 8 doc tep va tim xem co trung khong
"""

def timKiem(tempt_fileBoy,tempt_fileGirl,tempt_name):

    if tempt_name in tempt_fileBoy:
        print("ten pho bien Nam")
    elif tempt_name in tempt_fileGirl:
        print("ten pho bien Nu")
    else:
        print("khong co")

    return
def main():
    boyList = []
    girlList =[]
    with open("Chương 07/GirlNames.txt","r") as fileGirl:
        girlList = [line.strip() for line in fileGirl]
        print(girlList)
    with open("Chương 07/BoyNames.txt","r") as fileBoy:
        boyList = [line.strip() for line in fileBoy]
        while True:
            ten = str(input("nhap vao ten : "))
            timKiem(boyList,girlList,ten)
            tiepTuc = input("tiep tuc hay khong y/n :")
            if tiepTuc == "n":
                break
            elif tiepTuc == "y":
                print("ok tiep tuc nhe ")
                continue
            else:
                print("nhap sai tiep tuc nhe ")
if __name__ == '__main__':
    main()