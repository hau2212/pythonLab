"""
Nguyễn Thanh Hậu
24-0-00627
matplotlib chuong 9  bài 3
"""
import numpy as np
import matplotlib.pyplot as plt
def veSoDo():
    # Tạo tập giá trị x
    x = np.linspace(-10, 10, 1000)

    # Các hàm số
    y1 = x**2
    y2 = np.sin(x)
    y3 = np.cos(x)

    # Tạo hình vẽ
    plt.figure(figsize=(8, 8))  # Hình vuông để tỷ lệ 1:1

    # Vẽ từng đồ thị
    plt.plot(x, y1, label='y = x²', color='red', linestyle='--', linewidth=2)
    plt.plot(x, y2, label='y = sin(x)', color='blue', linestyle='-', linewidth=2)
    plt.plot(x, y3, label='y = cos(x)', color='green', linestyle='-.', linewidth=2)

    # Cấu hình trục và tỷ lệ
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.title('Các đồ thị hàm số', fontsize=16)
    plt.axis('equal')  # Đơn vị trên trục Ox và Oy bằng nhau

    # Hiển thị trục Ox và Oy rõ ràng
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Hiển thị đồ thị
    plt.show()
veSoDo()