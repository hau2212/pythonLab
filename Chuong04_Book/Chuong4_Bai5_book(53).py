"""
nguyen thanh hau
24-0-00627
bai 5
"""

def nhap_so_nguyen_duong():
    while True:
        try:
            n = int(input("Nhập số nguyên dương n: "))
            if n > 0:
                return n
            else:
                print("⚠️ Vui lòng nhập số > 0.")
        except ValueError:
            print("⚠️ Giá trị không hợp lệ, vui lòng nhập số nguyên.")

def tinh_S1(n):
    tong = 0
    for i in range(1, n + 1):
        tong += 1 / (i * (i + 1))
    return tong

def tinh_S2(n):
    tong = 0
    for i in range(n):
        tu = 2 * i + 1
        mau = 2 * i + 2
        tong += tu / mau
    return tong

# === Chương trình chính ===
def main():
    n = nhap_so_nguyen_duong()
    s1 = tinh_S1(n)
    s2 = tinh_S2(n)
    print(f"✅ S1(n) = {round(s1, 5)}")
    print(f"✅ S2(n) = {round(s2, 5)}")

main()

