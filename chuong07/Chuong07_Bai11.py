"""
nguyen thanh hau
24-0-00627
chuong 7 bai 11
"""

"""
Nguyen Thanh Hau
24-0-00627
Chuong 7 - Bai 11: Kiem tra Lo Shu Magic Square
"""

def is_lo_shu_magic_square(square):
    # Kiểm tra có đủ các số từ 1 đến 9 không
    numbers = [num for row in square for num in row]
    if sorted(numbers) != list(range(1, 10)):
        return False

    # Tính tổng chuẩn của một hàng/cột/đường chéo (phải bằng 15)
    target_sum = 15

    # Kiểm tra tổng các hàng
    for row in square:
        print(row)
        if sum(row) != target_sum:
            return False

    # Kiểm tra tổng các cột
    for col in range(3):
        col_sum = square[0][col] + square[1][col] + square[2][col]
        if col_sum != target_sum:
            return False

    # Kiểm tra 2 đường chéo
    diag1 = square[0][0] + square[1][1] + square[2][2]
    diag2 = square[0][2] + square[1][1] + square[2][0]

    if diag1 != target_sum or diag2 != target_sum:
        return False

    return True

def main():
    lo_shu_square = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]

    if is_lo_shu_magic_square(lo_shu_square):
        print("✅ Đây là quảng trường ma thuật Lo Shu.")
    else:
        print("❌ Đây KHÔNG phải là quảng trường ma thuật Lo Shu.")

main()
