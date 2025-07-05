# Hàm tìm các tốc độ quay nhỏ hơn min và trả về cùng chỉ số
# Input:
#   - list_speed: danh sách tốc độ quay (list số nguyên)
#   - min_speed: giá trị tối thiểu cần kiểm tra
# Output:
#   - tuple gồm (list_toc_do_nho, list_chi_so)
def locTocDoThap(list_speed, min_speed):
    toc_do_nho = []
    chi_so = []

    for i in range(len(list_speed)):
        if list_speed[i] < min_speed:
            toc_do_nho.append(list_speed[i])
            chi_so.append(i)

    return toc_do_nho, chi_so


# Hàm main kiểm tra ví dụ
def main():
    speeds = [1200, 800, 950, 1500, 700, 1100]
    min_val = 1000

    ket_qua, vi_tri = locTocDoThap(speeds, min_val)

    print(f"Các tốc độ nhỏ hơn {min_val}: {ket_qua}")
    print(f"Vị trí trong danh sách: {vi_tri}")


# Gọi main
main()
