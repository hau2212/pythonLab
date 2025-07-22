"""
Nguyễn Thanh Hậu
24-0-00627
Kiểm tra định kỳ - Câu 4: đọc file và vẽ biểu đồ giá xăng
"""

import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV.
# Input: filename (str): tên tệp CSV
# Output: list: 2 danh sách (ngay, gia)
def doc_du_lieu(filename):
    ngay = []
    gia = []
    with open(filename, "r") as file:
        for dong in file:
            dong = dong.strip()
            if dong == "":
                continue  # Bỏ dòng trống
            data = dong.split(",")
            if len(data) != 2:
                continue  # Bỏ dòng sai định dạng
            ngay.append(data[0])
            gia.append(float(data[1]))
    return ngay, gia

#Vẽ biểu đồ đường giá xăng theo ngày.
#Input:
#        ngay (list): danh sách ngày (chuỗi)
#        gia (list): danh sách giá (float)
def ve_bieu_do(ngay, gia):
    plt.figure(figsize=(10, 5))
    plt.plot(ngay, gia, marker='o', linestyle='-', color='blue')
    plt.title("Biểu đồ giá xăng theo ngày")
    plt.xlabel("Ngày")
    plt.ylabel("Giá xăng (VNĐ hoặc USD)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()  # Tránh bị che chữ
    plt.show()

# Hàm main chịu trách nhiệm xử lý chính
def main():
    ten_file = "gas_price.csv"
    ngay, gia = doc_du_lieu(ten_file)
    ve_bieu_do(ngay, gia)

# Gọi chương trình chính
main()
