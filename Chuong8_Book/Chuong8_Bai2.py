def main():
    """
    Tác giả: Nguyễn Thanh Hậu
    Chương: 8 - Bài tập
    Mã số sinh viên: 24-0-00627
    Mô tả: Sinh 'a' số ngẫu nhiên trong khoảng [0, 100),
    lọc các số chia hết cho 'b' và in ra danh sách kết quả.
    """
    import numpy as np

    try:
        total_numbers = int(input("Nhập số lượng số cần tạo (a): "))
        divisor = int(input("Nhập số để kiểm tra chia hết (b): "))

        if divisor == 0:
            raise ValueError("Không thể chia cho 0. Vui lòng nhập số khác b ≠ 0.")

        result_list = []
        count = 0

        while count < total_numbers:
            random_number = np.random.randint(0, 100)
            if random_number % divisor == 0:
                result_list.append(random_number)
                count += 1

        print("Danh sách các số chia hết cho", divisor, "là:", result_list)

    except ValueError as ve:
        print("Lỗi giá trị:", ve)
    except Exception as e:
        print("Đã xảy ra lỗi không xác định:", e)

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()

