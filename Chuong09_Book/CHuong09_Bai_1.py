import matplotlib.pyplot as plt
import numpy as np
"""
X_CORD = [1,3,6,9]
Y_CORD = [2,4,6,8]

plt.pie(X_CORD,colors=('r','k'))
#plt.xlim(xmin=1,xmax=50)
#plt.ylim(ymin=1,ymax=50)
#plt.xticks([1,2,3,4],['1cm','2cm','3cm','4cm'])
#plt.yticks([0,1,2,3,4,5,6,7,8,9],['hello','5','gt','fd','fd','56','yt','98','hs','qưqwe'])
plt.title("hello ửold")
#plt.xlabel("nôn")
#plt.grid(True)
plt.show()"""

import numpy as np
import matplotlib.pyplot as plt
def veSoDo():
    # Định nghĩa hàm
    def f(x):
        return 3*x**5 + 20*x**4 - 10*x**3 - 240*x**2 - 250*x + 200

    # Tạo dãy giá trị x
    x = np.linspace(-10, 5, 1000)
    y = f(x)

    # Vẽ đồ thị
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue', linestyle='-', linewidth=2, label='y = 3x⁵ + 20x⁴ – 10x³ – 240x² – 250x + 200')

    # Định dạng đồ thị
    plt.title('Đồ thị hàm bậc 5', fontsize=16)
    plt.xlabel('Giá trị x', fontsize=12)
    plt.ylabel('Giá trị y', fontsize=12)
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)  # trục Ox
    plt.axvline(0, color='black', linewidth=1)  # trục Oy

    # Giới hạn trục
    plt.xlim(-10, 5)
    plt.ylim(-4000, 2000)

    # Hiển thị chú thích
    plt.legend()

    # Hiển thị đồ thị
    plt.show()
veSoDo()