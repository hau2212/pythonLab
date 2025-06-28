"""
nguyen thanh hau
24-0-00627
tinh giai thua cua mot so
"""
def tinh_giai_thua(n):
    if n < 0:
        return None  # Trả về None nếu số âm
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

# Chương trình chính
so = int(input("Nhập một số nguyên không âm: "))
ket_qua = tinh_giai_thua(so)

if ket_qua is None:
    print("Không thể tính giai thừa của số âm.")
else:
    print(f"{so}! = {ket_qua}")
