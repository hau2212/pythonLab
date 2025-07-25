"""
Nguyễn Thanh Hậu - Chương 6 - Bài 5

Chức năng:
Giải phương trình bậc hai dạng: ax^2 + bx + c = 0

Input:
    a, b, c (float): các hệ số của phương trình

Output:
    list nghiệm (rỗng nếu vô nghiệm)
"""

import math

def giai_pt_bac_hai(a, b, c):
    """
    Giải phương trình bậc hai ax^2 + bx + c = 0

    Input:
        a (float): hệ số bậc hai
        b (float): hệ số bậc nhất
        c (float): hệ số tự do

    Output:
        list chứa nghiệm (float) hoặc rỗng nếu vô nghiệm
    """
    if a == 0:
        if b == 0:
            return []  # Phương trình vô nghiệm
        else:
            return [-c / b]  # Phương trình bậc 1
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return []  # Vô nghiệm
    elif delta == 0:
        return [-b / (2 * a)]  # Nghiệm kép
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [x1, x2]

def main():
    """
    Hàm chính để nhập hệ số và hiển thị nghiệm
    """
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    nghiem = giai_pt_bac_hai(a, b, c)

    if not nghiem:
        print("Phương trình vô nghiệm.")
    elif len(nghiem) == 1:
        print("Phương trình có nghiệm kép:", nghiem[0])
    else:
        print("Phương trình có hai nghiệm:")
        print("x1 =", nghiem[0])
        print("x2 =", nghiem[1])

# Gọi hàm main
main()
