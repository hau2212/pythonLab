"""
Nguyễn Thanh Hậu
24-0-00627
matplotlib chuong 9  bài 3
"""

import matplotlib.pyplot as plt

def veBieuDo():
    x_cord = [1,3,6,9,12]
    y_cord = [4,2,9,7,3]

    plt.bar(x_cord,y_cord)
    plt.grid(True)
    plt.xlabel("sales")
    plt.ylabel("doanh thu")
    plt.show()
veBieuDo()