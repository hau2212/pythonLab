"""
nguyen thanh hau
24-0-00627
chuong 7 bai 7
"""

# Hàm trả về số sao tiết kiệm năng lượng dựa vào điện năng tiêu thụ mỗi ngày
# Input: P - điện năng tiêu thụ mỗi ngày (kWh)
# Output: số sao tiết kiệm năng lượng (int)
def tinhSoSaoTietKiem(P):
    if P < 2:
        return 5
    elif P < 4:
        return 4
    elif P < 6:
        return 3
    elif P < 10:
        return 2
    else:
        return 1

# Hàm nhận giá trị điện năng từ người dùng
# Output: giá trị float hợp lệ
def getInput():
    try:
        value = float(input("Nhập điện năng tiêu thụ mỗi ngày (kWh): "))
        if value < 0:
            print("⚠️ Không được nhập số âm.")
            return getInput()
        return value
    except ValueError:
        print("⚠️ Vui lòng nhập số hợp lệ.")
        return getInput()

# Hàm chính điều phối chương trình
def main():
    p = getInput()
    so_sao = tinhSoSaoTietKiem(p)
    print(f"⭐ Thiết bị đạt {so_sao} sao tiết kiệm năng lượng.")

# Gọi chương trình
main()
