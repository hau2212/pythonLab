"""
nguyen thanh hau
24-0-00627

"""
import os.path
import sys
curent_folder = os.path.dirname(os.path.abspath(__file__))
full_path= os.path.join(curent_folder, "Ch6")
def tinh_trung_binh_buoc_moi_thang(filename):
    try:
        with open(os.path.join(full_path ,filename), "r") as f:
            data = [int(line.strip()) for line in f.readlines()]

        if len(data) != 365:
            print("⚠️ File không chứa đúng 365 dòng.")
            return

        so_ngay_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ten_thang = ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6",
                     "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "Tháng 11", "Tháng 12"]

        index = 0
        for i in range(12):
            ngay = so_ngay_thang[i]
            buoc_thang = data[index:index + ngay]
            trung_binh = sum(buoc_thang) / ngay
            print(f"{ten_thang[i]}: Trung bình {trung_binh:,.2f} bước/ngày")
            index += ngay

    except FileNotFoundError:
        print("❌ Không tìm thấy file:", filename)
    except Exception as e:
        print("❌ Lỗi:", str(e))

# Gọi hàm
tinh_trung_binh_buoc_moi_thang("steps.txt")
