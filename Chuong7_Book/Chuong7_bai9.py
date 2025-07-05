"""
nguyen thanh hau
24-0-00627
chuong 7 bai 9
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

# Hàm in ra thông báo thiết bị có tiết kiệm điện hay không
# Input: P - điện năng tiêu thụ mỗi ngày (kWh)
# Output: không có, chỉ in kết quả
def kiemTraTietKiem(P):
    sao = tinhSoSaoTietKiem(P)
    if sao >= 3:
        print(f"✅ Thiết bị tiết kiệm điện ({sao} sao).")
    else:
        print(f"❌ Thiết bị không tiết kiệm điện ({sao} sao).")

# Hàm nhập dữ liệu từ người dùng
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
    kiemTraTietKiem(p)

# Gọi chương trình
main()
