"""
Nguyễn Thanh Hậu - Chương 6 - Bài 3

Chức năng:
Kiểm tra một thiết bị có tiết kiệm điện hay không,
dựa vào số sao tiết kiệm năng lượng tính từ hàm bài 2.

Quy định:
- Gọi lại hàm tính số sao từ bài 2.
- Nếu số sao < 3 → không tiết kiệm điện.
- Ngược lại → tiết kiệm điện.

Input:
    p (float): điện năng tiêu thụ mỗi ngày (kWh)

Output:
    In ra thông báo tương ứng.
"""

def tinh_so_sao(p):
    """
    Tính số sao tiết kiệm năng lượng.

    Input:
        p (float): điện năng tiêu thụ mỗi ngày (kWh)

    Output:
        (int): số sao tiết kiệm (1 đến 5)
    """
    if p < 2:
        return 5
    elif p < 4:
        return 4
    elif p < 6:
        return 3
    elif p < 10:
        return 2
    else:
        return 1

def kiem_tra_tiet_kiem(p):
    """
    Kiểm tra thiết bị có tiết kiệm điện không,
    dựa vào số sao trả về từ hàm tinh_so_sao().

    Input:
        p (float): điện năng tiêu thụ mỗi ngày (kWh)

    Output:
        In ra thông báo tiết kiệm hoặc không tiết kiệm.
    """
    so_sao = tinh_so_sao(p)
    if so_sao < 3:
        print("Thiết bị KHÔNG tiết kiệm điện.")
    else:
        print("Thiết bị tiết kiệm điện.")

def main():
    """
    Hàm chính: nhập vào điện năng tiêu thụ,
    kiểm tra và in kết quả ra màn hình.
    """
    try:
        p = float(input("Nhập điện năng tiêu thụ mỗi ngày (kWh): "))
        kiem_tra_tiet_kiem(p)
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

# Gọi hàm main
main()
