"""
nguyen thanh hau
24-0-00627
Calo từ chất béo và chất bột đường
"""
def main():
    while True:
        try:
            inputFat = float(input("nhap vao so gram chat beo : "))
            inputHyd = float(input("nhap vao so gram carbohydrate : "))

            totalFat = lambda inputUser : inputUser * 9
            totalHyd = lambda inputUser : inputUser * 4
            print("\n"*10)
            print(f"tong so cal beo la : {totalFat(inputUser=inputFat)}")
            print(f"tong so cal hyd la : {totalHyd(inputUser=inputHyd)}")
            tiepTuc = str(input("Ban co muon tiep tuc hay khong n/y : "))
            if tiepTuc == "n":
                return
            elif "n" != tiepTuc != "y":
                print("\n"*20)
                print("ban nhap sai nen chuong trinh se tiep tuc ")
        except ValueError as A:
            print(str(A))
if __name__ == '__main__':
    main()