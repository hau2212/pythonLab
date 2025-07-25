"""
nguyen thanh hau
24-0-00627
chuong 7 bai 12
"""

def main():
    try:
        conTent = {}
        tenTep = input("nhap vao ten mot tep : ")
        path ="Chương 07/"
        with open(path+tenTep,"r") as file:
            for num,line in enumerate(file):
                conTent[num] = line.strip("\n")

        print(conTent)
        while True:
            userInput = int(input("chon vao dong muon doc : "))
            if userInput <= len(conTent):
                tempt = conTent[userInput]
                print(tempt)
            else:
                print("khong hop le khong co dong do : ")
    except IOError as Io :
        print(str(Io))
    except ValueError as Va:
        print(str(Va))
    except IndexError as In:
        print(str(In))
    except Exception as Ex:
        print(str(Ex))


if __name__ == '__main__':
    main()