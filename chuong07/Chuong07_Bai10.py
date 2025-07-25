"""
nguyen thanh hau
24-0-00627
chuong 7 bai 10
"""

def kiemTra(tempt_DanhSach,tempt_name):
    count = 0
    tempt_chienThang = []

    for nam,doi in tempt_DanhSach.items():
        if tempt_name == doi:
            count += 1
            tempt_chienThang.append(f"nam {nam} doi : {doi} chien thang ")

    for line in tempt_chienThang:
        print(line)


    return
def main():
    try:
        danhSachDict = {}
        with open("Chương 07/WorldSeriesWinners.txt","r") as file:
            for i,line in enumerate(file,start=1903):
                danhSachDict[i] = line.strip()
            print(danhSachDict)
            kiemTra(danhSachDict,"New York Giant")

    except Exception as Ex:
        print(str(Ex))
main()