"""
nguễn thanh hậu
Chuong 3 bài 4
chuyển đổi số la mã

"""

def chuyenDoi(number):
    dict_laMa = {
        1:"I",
        2:"II",
        3:"III",
        4:"IV",
        5:"V",
        6:"VI",
        7:"VII",
        8:"VIII",
        9:"IX",
        10:"X"
    }
    if (dict_laMa.get(number)):
        print(dict_laMa.get(number))
    else:
        print("nhap 1 toi 10")


soCHuyenDoi = int(input("so chuyen doi dau vao "))
chuyenDoi(soCHuyenDoi)

