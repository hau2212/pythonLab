"""
nguyen thanh hau
24-0-00627
doc file dan so va loc du lieu ra
bai 9 chuong 7
"""

def tinhToan(tempt_danSoDict):
    tempt_highest = {}
    tempt_lowest = {}
    year_highest = max(tempt_danSoDict,key=tempt_danSoDict.get)
    year_lowest = min(tempt_danSoDict,key=tempt_danSoDict.get)
    print(f"{year_highest} la nam co dan so cao nhat : {tempt_danSoDict[year_highest]}")
    print(f"{year_lowest} la nam co dan so thap nhat :  {tempt_danSoDict[year_lowest]}")



def main():
    try:
        danSoDict = {}

        with open("Chương 07/USPopulation.txt","r") as file:
            for i , content in enumerate(file,start=1950):
                danSoDict[i] = content.strip("\n")

        print(danSoDict)
        tinhToan(danSoDict)
    except Exception as Ex:
        print(str(Ex))

main()

