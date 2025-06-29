"""
nguyen thanh hau
24-0-00627
bai 2 sach
"""


def nhap_so_nguyen_duong():
    while True:
        try:
            n = int(input("Nhập số nguyên dương N: "))
            if n > 0:
                return n
            else:
                print("⚠️ N phải lớn hơn 0.")
        except ValueError:
            print("⚠️ Vui lòng nhập một số nguyên hợp lệ.")


def tim_so_le_lon_nhat(danh_sach):
    so_le = [x for x in danh_sach if x % 2 == 1]
    if so_le:
        return max(so_le)
    else:
        return None


def main():
    tiep_tuc = 'c'
    while tiep_tuc.lower() == 'c':
        N = nhap_so_nguyen_duong()

        ds_so = []
        print(f"Nhập {N} số nguyên:")
        i = 0
        while i < N:
            try:
                so = int(input(f"Số thứ {i + 1}: "))
                ds_so.append(so)
                i += 1
            except ValueError:
                print("⚠️ Vui lòng nhập số nguyên.")

        so_le_max = tim_so_le_lon_nhat(ds_so)
        if so_le_max is not None:
            print(f"✅ Số lẻ lớn nhất là: {so_le_max}")
        else:
            print("❌ Không có số lẻ nào trong danh sách.")

        tiep_tuc = input("Nhấn 'c' để tiếp tục, phím khác để thoát: ")


main()
