"""
nguyen thanh hau
24-0-00627
bảng chuyển đổi dặm sang km bước nhảy 10
"""
MOT_KM = 1.60934


# hàm tính chuyển đổi dặm sang km làm tròn đến 2 số thập phân
def tinhChuyenDoi():
    print("**************************\n Bảng chuyển đổi ")
    for dam in range(10,80+10,10):
        print(f"{dam} chuyển đổi thành {dam * MOT_KM:.2f}")


tinhChuyenDoi()