"""
nguyen thanh hau
24-0-00627
tinh tang dan so
"""

def tinhTangDanSo(soLuong, soNgay, mucTang):
    if soLuong <= 0 or soNgay <= 0 or mucTang < 0:
        print("Dữ liệu không hợp lệ.")
        return

    print(f"Ngày 1: {soLuong:.2f} sinh vật")
    for ngay in range(2, soNgay + 1):
        soLuong += soLuong * mucTang
        print(f"Ngày {ngay}: {soLuong:.2f} sinh vật")

# Gọi hàm
tinhTangDanSo(2, 10, 0.3)
