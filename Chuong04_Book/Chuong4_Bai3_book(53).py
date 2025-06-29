"""
nguyen thanh hau
24-0-00627
tinh so nguyen
"""

def nhap_so_nguyen():
    while True:
        try:
            n = int(input("Nhập một số nguyên N: "))
            return n
        except ValueError:
            print("⚠️ Vui lòng nhập một số nguyên hợp lệ.")

def in_uoc_so(n):
    print(f"✅ Các ước số của {n} là:")
    i = 1
    while i <= abs(n):   # Dùng abs để hỗ trợ số âm
        if n % i == 0:
            print(i, end=' ')
        i += 1
    print()

# ======= Chạy chương trình ========
def main():
    n = nhap_so_nguyen()
    in_uoc_so(n)

main()
