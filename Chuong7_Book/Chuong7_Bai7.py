"""
nguyen thanh hau
24-0-00627
chuong 7 bai 7
"""
# Hàm kiểm tra thiết bị có tiết kiệm điện hay không
# Input: năng lượng tiêu thụ mỗi ngày (float)
# Output: không trả về, chỉ in thông báo
def kiemTraTietKiem(kwh):
    if kwh < 10:
        print(f"✅ Thiết bị tiết kiệm điện ({kwh} kWh/ngày).")
    else:
        print(f"⚠️ Thiết bị không tiết kiệm điện ({kwh} kWh/ngày).")

# Hàm nhận giá trị điện năng tiêu thụ từ người dùng
# Output: số kWh hợp lệ (float)
def getInput():
    try:
        value = float(input("Nhập điện năng tiêu thụ mỗi ngày (kWh): "))
        if value < 0:
            print("⚠️ Không được nhập số âm.")
            return getInput()
        return value
    except ValueError:
        print("⚠️ Vui lòng nhập số hợp lệ (dạng số thập phân).")
        return getInput()

# Hàm chính điều phối chương trình
def main():
    kwh = getInput()
    kiemTraTietKiem(kwh)

# Gọi hàm chính
main()
