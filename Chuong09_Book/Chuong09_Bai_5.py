"""
File: chuong5_bai5_hyperboloid_3d.py
Mô tả: Vẽ hình hyperboloid từ phương trình -0.3x^2 -0.3y^2 + z^2 = 1
       sử dụng biểu đồ 3D và colormap 'jet'
Yêu cầu: matplotlib, numpy (pip install matplotlib numpy)
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ve_hyperboloid():
    """
    Vẽ hình hyperboloid 3D với phương trình:
        -0.3x^2 - 0.3y^2 + z^2 = 1
    Dùng colormap 'jet' và vmin/vmax cho dãy màu.
    """
    # Tạo lưới tọa độ x, y
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Tính giá trị Z theo công thức: z = ± sqrt(1 + 0.3*x^2 + 0.3*y^2)
    Z_top = np.sqrt(1 + 0.3 * X**2 + 0.3 * Y**2)
    Z_bottom = -Z_top

    # Tạo figure và trục 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ hai mặt hyperboloid trên/dưới
    surface1 = ax.plot_surface(X, Y, Z_top, cmap='jet', vmin=-5, vmax=5)
    surface2 = ax.plot_surface(X, Y, Z_bottom, cmap='jet', vmin=-5, vmax=5)

    # Thêm thanh màu
    fig.colorbar(surface1, ax=ax, shrink=0.5, aspect=5)

    # Gắn nhãn
    ax.set_title('Hyperboloid: $-0.3x^2 - 0.3y^2 + z^2 = 1$')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Gọi hàm vẽ
ve_hyperboloid()
