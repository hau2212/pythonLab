"""
nguyen thanh hau
24-0-00627
ghi du lieu va ve matpliot
"""

import matplotlib.pyplot as plt
def veBieuDo():
    tempt_dict = {}
    with open("chiPhi.txt", "r") as fileVal:
        for line in fileVal:
            key,val = line.strip().split()
            tempt_dict[key] = val
    plt.title("bieu do hinh tron \n thong ke chi phi ca nhan ")
    plt.pie(tempt_dict.values(),labels=tempt_dict.keys(),startangle=180)

    plt.show()


veBieuDo()
def main():
    content = {"tienAn" : 100 ,  "tienNha":200 , "tienXe" : 500 , "tienChoiGai" : 1000}
    with open("chiPhi.txt","w") as file:
        for key,val in content.items():
            file.writelines(f"{key} {val} \n")
