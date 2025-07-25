"""
nguyễn thanh hậu
24-0-00627
tinh tổng lượng mưa
"""
from numpy.ma.extras import average


def tinhLuongMua(danhSach):
    try:
        total = []
        avg = []
        tempt_avg = 0
        for year in danhSach:
            tempt_total = 0

            print(f"nam {year}")
            for month in danhSach[year]:
                print(f"thang {month} cua nam {year} : {danhSach[year][month]}")
                tempt_total += danhSach[year][month]
            tempt_avg = tempt_total / 12
            total.append(tempt_total)
            avg.append(tempt_avg)



    except KeyError as a :
        print(str(a))
    except ValueError as e:
        print(str(e))
    finally:
        print("xong")
    return print(total , avg)

def main():
    try:
        yearList = {}
        months = {}
        years = 0
        while True:
            years = int(input("ban muon tinh may nam : "))
            if years <= 0:
                print(" yeu cau nhap vao tren 1 nam 0")
                continue
            else:
                for year in range(1,years+1):
                    for month in range(1,12+1):
                        months[month] = float(input(f"nhap vao luong mua cho nam thu {year} thang {month} : "))
                    yearList[year] = months.copy()
                break
        tinhLuongMua(danhSach=yearList)

        print(months)
        print(months.values())
        print(yearList)
    except ValueError as a:
        print(str(a))
main()