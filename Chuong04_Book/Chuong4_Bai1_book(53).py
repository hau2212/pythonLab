"""
nguyen thanh hau
24-0-00627
tinh bai tap toan
"""

def tinh_S1(n):
    i = 1
    tong = 0
    tich = 0
    while i <= n:
        tich += i
        tong += 1 / tich
        i += 1
    return tong

def tinh_S2(n):
    i = 1
    tong = 0
    while i <= n:
        tong += 1 / (i * (i + 1))
        i += 1
    return tong

def tinh_S3(n):
    i = 1
    tong = 0
    while i <= n:
        tong += i / (i + 1)
        i += 1
    return tong

def tinh_S4(n):
    i = 0
    tong = 0
    while i < n:
        tu = 2 * i + 1
        mau = 2 * i + 2
        tong += tu / mau
        i += 1
    return tong

# ====== Chương trình chính ======
def main():
    n = int(input("Nhập n (số nguyên dương): "))
    while n <= 0:
        n = int(input("Vui lòng nhập lại n (> 0): "))

    print("S1 =", round(tinh_S1(n), 5))
    print("S2 =", round(tinh_S2(n), 5))
    print("S3 =", round(tinh_S3(n), 5))
    print("S4 =", round(tinh_S4(n), 5))

main()
