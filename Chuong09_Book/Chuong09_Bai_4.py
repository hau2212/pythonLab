"""
File: chuong9_bai4_histogram.py
Mô tả: Minh họa cách sử dụng hàm plt.hist() để vẽ histogram.
       Dữ liệu mẫu là danh sách điểm số của sinh viên.
Yêu cầu: Cài đặt thư viện matplotlib (pip install matplotlib nếu chưa có).
"""

import matplotlib.pyplot as plt


def ve_histogram_diem(danh_sach_diem):
    """
    Vẽ biểu đồ histogram thể hiện phân bố điểm số.

    Input:
        danh_sach_diem (list of float): Danh sách điểm số.

    Output:
        Hiển thị biểu đồ histogram bằng matplotlib.
    """
    plt.hist(danh_sach_diem, bins=5, color='skyblue', edgecolor='black')
    plt.title('Biểu đồ phân bố điểm số sinh viên')
    plt.xlabel('Điểm số')
    plt.ylabel('Số lượng sinh viên')
    plt.grid(True)
    plt.show()


# Dữ liệu mẫu: điểm của 30 sinh viên
diem = [6.5, 7.0, 8.5, 5.5, 6.0, 9.0, 7.5, 8.0, 4.5, 6.0,
        7.0, 5.0, 6.5, 8.0, 9.0, 7.0, 6.5, 5.5, 4.0, 7.5,
        6.0, 5.0, 7.5, 8.0, 8.5, 6.0, 6.5, 7.0, 5.5, 4.5]

# Gọi hàm vẽ histogram
ve_histogram_diem(diem)
