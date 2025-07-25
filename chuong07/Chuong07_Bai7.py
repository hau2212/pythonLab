"""
nguyen thanh hau
24-0-00627
chuong 7 bai 6
"""
def soSanh(tempt_dap_an,tempt_cauTraLoi):
    for num,key in tempt_dap_an:
        if tempt_dap_an[key] == tempt_cauTraLoi[num]:
            print("dung")
    return

def main():
    try:
        totalRight = ""
        totalWrong = ""
        flagWrong =0
        flagRight =0
        dap_an = {1: "A", 2: "C", 3: "A", 4: "A", 5: "D", 6: "B", 7: "C", 8: "A", 9: "C", 10: "B",
              11: "A", 12: "D", 13: "C", 14: "A", 15: "D", 16: "C", 17: "B", 18: "B", 19: "D", 20: "A"}

        for num in range(1,20+1):
            traLoi = str(input("nhap vao cau tra loi : "))
            if dap_an[num] != traLoi:
                totalWrong += f"Sai roi , cau {num} dap an {dap_an[num]} ban chon la : {traLoi} \n"
                flagWrong += 1
            else:
                totalRight += f"Dung roi , cau {num} dap an {dap_an[num]} ban chon la : {traLoi} \n "
                flagRight += 1
        print(totalRight)
        print(totalWrong)
    except Exception as Ex:
        print(str(Ex))
main()