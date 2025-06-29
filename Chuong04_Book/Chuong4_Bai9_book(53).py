"""
nguyen thanh hau
24-0-00627
bai 9
"""

def nhap_so_nguyen_duong():
    while True:
        try:
            n = int(input("Nhập số lượng số nguyên tố cần tìm (N): "))
            if n > 0:
                return n
            else:
                print("⚠️ N phải lớn hơn 0.")
        except ValueError:
            print("⚠️ Vui lòng nhập số nguyên hợp lệ.")

def la_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def tim_n_so_nguyen_to(n):
    lst = []
    dem = 0
    so = 2
    while dem < n:
        if la_nguyen_to(so):
            lst.append(so)
            dem += 1
        so += 1
    return lst

# === Chương trình chính ===
def main():
    N = nhap_so_nguyen_duong()
    danh_sach_nt = tim_n_so_nguyen_to(N)
    print(f"✅ {N} số nguyên tố đầu tiên là:")
    print(danh_sach_nt)

main()
