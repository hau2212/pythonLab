"""
Nguyễn Thanh Hậu - Chương 6 - Bài 1

Chức năng:
- Kiểm tra một thiết bị có tiết kiệm điện hay không dựa trên điện năng tiêu thụ mỗi ngày.

Điều kiện:
- Thiết bị tiêu thụ < 10 kWh/ngày → được gọi là "tiết kiệm điện".
"""

def kiem_tra_tiet_kiem(p):
    """
    Hàm kiểm tra thiết bị có tiết kiệm điện hay không.

    Input:
        p (float): Điện năng tiêu thụ mỗi ngày (kWh)

    Output:
        None: In ra thông báo kết luận
    """
    if p < 10:
        print("Thiết bị tiết kiệm điện.")
    else:
        print("Thiết bị không tiết kiệm điện.")

# Ví dụ sử dụng
def main():
    dien_nang = float(input("Nhập điện năng tiêu thụ mỗi ngày (kWh): "))
    kiem_tra_tiet_kiem(dien_nang)

# Gọi hàm chính
main()
