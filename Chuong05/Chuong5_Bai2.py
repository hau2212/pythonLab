"""
nguyen thanh hau
"""
SO_LAN_LAP = 3

# Hàm dùng để lặp chuỗi
def lapChuoi(chuoi):
    total = ""
    for chu in range(SO_LAN_LAP):
        total += chuoi
    return total

# Hàm main xử lý logic dữ liệu đầu vào
def main():
    try:
        while True:
            user_input = input("nhap vao nhung gi ban muon lap lai")
            print(lapChuoi(user_input))

            tiepTuc = input("ban co muon tiep tuc khong n/y :").lower()
            if tiepTuc == "n":
                return
            elif tiepTuc == "y":
                continue

    except ValueError as A:
        print("ban bi loi " + str(A))
main()