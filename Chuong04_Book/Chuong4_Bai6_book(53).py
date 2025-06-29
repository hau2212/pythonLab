"""
nguyen thanh hau
24-0-00627
bai 6
"""


def nhap_list():
    lst = []
    try:
        n = int(input("Nhập số lượng phần tử trong list: "))
        for i in range(n):
            x = int(input(f"Phần tử thứ {i + 1}: "))
            lst.append(x)
    except ValueError:
        print("⚠️ Vui lòng nhập số nguyên.")
    return lst


def tim_chia_het_5_max(lst):
    max_chia_5 = None
    for x in lst:
        if x % 5 == 0:
            if (max_chia_5 is None) or (x > max_chia_5):
                max_chia_5 = x
    return max_chia_5


# === Chương trình chính ===
def main():
    lst = nhap_list()
    print("✅ Danh sách bạn đã nhập:", lst)

    kq = tim_chia_het_5_max(lst)
    if kq is not None:
        print(f"✅ Phần tử chia hết cho 5 lớn nhất là: {kq}")
    else:
        print("❌ Không có phần tử nào chia hết cho 5 trong list.")


main()
