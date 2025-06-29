"""
nguyen thanh hau
24-0-00627
bai 7
"""

def nhap_list():
    lst = []
    try:
        n = int(input("Nhập số phần tử trong list: "))
        for i in range(n):
            x = float(input(f"Phần tử thứ {i+1}: "))
            lst.append(x)
    except ValueError:
        print("⚠️ Vui lòng nhập số hợp lệ.")
    return lst

def loc_phan_tu_khong_lon_hon_A(lst, A):
    ket_qua = []
    for x in lst:
        if x <= A:
            ket_qua.append(x)
    return ket_qua

# === Chương trình chính ===
def main():
    lst = nhap_list()
    print("✅ Danh sách ban đầu:", lst)

    try:
        A = float(input("Nhập số thực A: "))
        lst_moi = loc_phan_tu_khong_lon_hon_A(lst, A)
        print(f"✅ Danh sách sau khi xoá phần tử > {A}:", lst_moi)
    except ValueError:
        print("⚠️ A phải là số thực.")

main()
