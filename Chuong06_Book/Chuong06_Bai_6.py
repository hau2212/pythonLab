"""
Nguyễn Thanh Hậu - Chương 6 - Bài 6

Chức năng:
Tính giá trị gần đúng của cos(x) bằng chuỗi Taylor.

Input:
    x (float): góc (tính theo radian)
    epsilon (float): sai số cho phép (ngưng khi giá trị tuyệt đối của hạng tử nhỏ hơn epsilon)

Output:
    cos_x (float): giá trị gần đúng của cos(x)
"""


def tinh_cos_bang_taylor(x, epsilon=1e-10):
    """
    Tính gần đúng cos(x) bằng khai triển Taylor

    cos(x) = Σ [(-1)^n * x^(2n)] / (2n)! với n từ 0 đến ∞

    Input:
        x (float): giá trị góc theo radian
        epsilon (float): sai số dừng

    Output:
        float: giá trị gần đúng của cos(x)
    """
    term = 1.0  # Hạng tử đầu tiên
    cos_x = term
    n = 1
    while abs(term) > epsilon:
        term *= (-1) * x ** 2 / ((2 * n - 1) * (2 * n))  # Tính hạng tử tiếp theo
        cos_x += term
        n += 1
    return cos_x


def main():
    """
    Hàm chính để nhập giá trị và tính cos(x)
    """
    import math
    x = float(input("Nhập x (radian): "))
    ket_qua = tinh_cos_bang_taylor(x)
    print(f"cos({x}) xấp xỉ = {ket_qua}")
    print(f"cos({x}) theo math.cos = {math.cos(x)}")


# Gọi hàm main
main()
