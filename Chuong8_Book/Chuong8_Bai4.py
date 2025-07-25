def is_prime(n):
    """
    Kiểm tra xem số n có phải là số nguyên tố không.
    Trả về True nếu là số nguyên tố, ngược lại False.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Kiểm tra đến căn bậc 2 của n
        if n % i == 0:
            return False
    return True

def check_list_for_primes(lst):
    """
    Trả về danh sách True/False tương ứng với việc phần tử
    trong lst có phải số nguyên tố hay không.
    """
    result = []
    for number in lst:
        result.append(is_prime(number))
    return result

# Dữ liệu đầu vào
list1 = [2, 1, 4, 7, 8, 19, 13]

# Đặt breakpoint tại đây nếu dùng debugger
# import pdb; pdb.set_trace()

# Kiểm tra số nguyên tố
list2 = check_list_for_primes(list1)

# In kết quả
print(list2)
