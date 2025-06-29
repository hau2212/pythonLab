"""
nguyen thanh hau
24-0-00627
bai 4
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
            print("⚠️ Vui lòng nhập số nguyên hợp lệ.")

def tong_chu_so(n):
    tong = 0
    while n > 0:
        chu_so = n % 10
        tong += chu_so
        n = n // 10
    return tong

# === Chạy chương trình ===
def main():
    n = nhap_so_nguyen_duong()
    tong = tong_chu_so(n)
    print(f"✅ Tổng các chữ số của {n} là: {tong}")

main()
