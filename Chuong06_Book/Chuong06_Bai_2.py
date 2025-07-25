"""
Nguyễn Thanh Hậu - Chương 6 - Bài 2

Chức năng:
- Trả về số sao tiết kiệm năng lượng dựa vào điện năng tiêu thụ mỗi ngày.

Quy định số sao:
+ P < 2        → 5 sao
+ 2 ≤ P < 4    → 4 sao
+ 4 ≤ P < 6    → 3 sao
+ 6 ≤ P < 10   → 2 sao
+ P ≥ 10       → 1 sao
"""

def tinh_so_sao(p):
    """
    Tính số sao tiết kiệm năng lượng cho thiết bị.

    Input:
        p (float): Điện năng tiêu thụ mỗi ngày (kWh)

    Output:
        int: Số sao tiết kiệm (1 đến 5)
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

# Ví dụ sử dụng
def main():
    dien_nang = float(input("Nhập điện năng tiêu thụ mỗi ngày (kWh): "))
    so_sao = tinh_so_sao(dien_nang)
    print("Số sao tiết kiệm năng lượng:", so_sao)

# Gọi hàm chính
main()
