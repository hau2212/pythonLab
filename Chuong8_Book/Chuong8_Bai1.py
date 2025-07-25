"""
nguyen thanh hau
chuong 8 bai
24-0-00627
"""

def filter_divisible_in_range(numbers, divisor, min_value, max_value):
    """
    Trả về danh sách các số trong 'numbers' thỏa mãn:
    - Chia hết cho 'divisor'
    - Nằm trong đoạn từ 'min_value' đến 'max_value' (bao gồm cả hai đầu)
    """
    filtered_numbers = []
    for num in numbers:
        if num % divisor == 0 and min_value <= num <= max_value:
            filtered_numbers.append(num)
    return filtered_numbers

# Danh sách đầu vào
number_list = [2, 1, 4, -4, 6, 10, 5, 8]

# Lọc các số chia hết cho 2 và nằm trong đoạn [5, 10]
result = filter_divisible_in_range(number_list, 2, 5, 10)

# In kết quả
print(result)
