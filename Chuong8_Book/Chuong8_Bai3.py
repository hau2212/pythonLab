def main():
    """
    Tác giả: Nguyễn Thanh Hậu
    Ví dụ: Sử dụng hàm isinstance() để kiểm tra kiểu dữ liệu đầu vào.
    Mã số sinh viên: 24-0-00627
    """

    try:
        # Nhập giá trị từ người dùng
        user_input = input("Nhập một giá trị bất kỳ: ")

        # Kiểm tra nếu là chuỗi
        if isinstance(user_input, str):
            print("Giá trị bạn vừa nhập là kiểu chuỗi (str).")

        # Thử ép kiểu sang số nguyên
        converted_int = int(user_input)

        # Kiểm tra kiểu sau khi ép kiểu
        if isinstance(converted_int, int):
            print("Giá trị sau khi chuyển đổi là kiểu số nguyên (int).")

    except ValueError:
        print("Không thể chuyển đổi sang kiểu số nguyên.")

    except Exception as e:
        print("Lỗi không xác định:", e)

# Gọi hàm main
if __name__ == "__main__":
    main()
