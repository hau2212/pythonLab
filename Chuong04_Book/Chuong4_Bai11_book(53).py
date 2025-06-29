"""
nguyen thanh hau
24-0-00627
bai 11
"""


def la_chuoi_nhi_phan(s):
    for ch in s:
        if ch not in ('0', '1'):
            return False
    return True


def chuyen_nhi_phan_sang_thap_phan(binary_str):
    decimal = 0
    do_dai = len(binary_str)
    for i in range(do_dai):
        bit = int(binary_str[i])
        mu = do_dai - 1 - i
        decimal += bit * (2 ** mu)
    return decimal


def main():
    binary = input("Nhập chuỗi nhị phân (chỉ gồm 0 và 1): ").strip()

    if not la_chuoi_nhi_phan(binary):
        print("⚠️ Chuỗi không hợp lệ! Chỉ được chứa ký tự 0 hoặc 1.")
        return

    decimal = chuyen_nhi_phan_sang_thap_phan(binary)
    print(f"✅ Giá trị thập phân tương ứng là: {decimal}")


main()
