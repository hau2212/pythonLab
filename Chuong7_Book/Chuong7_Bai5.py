"""
nguyen thanh hau
24-0-00627
chuong 7 bai 5
"""
import sys

# Hàm kiểm tra mật khẩu có mạnh hay không
# Input: mật khẩu dạng chuỗi
# Output: True nếu mạnh, False nếu không
def kiemTraMatKhau(password):
    if len(password) < 8:
        return False

    co_thuong = False
    co_hoa = False
    co_so = False

    for char in password:
        if char.islower():
            co_thuong = True
        elif char.isupper():
            co_hoa = True
        elif char.isdigit():
            co_so = True

    return co_thuong and co_hoa and co_so

# Hàm chính: nhận mật khẩu từ người dùng và báo kết quả
def main():
    while True:
        password = input("Nhập mật khẩu để kiểm tra: ")

        if kiemTraMatKhau(password):
            print("✅ Mật khẩu có tính bảo mật cao.")
        else:
            print("❌ Mật khẩu chưa đủ mạnh. Yêu cầu: ≥8 ký tự, 1 thường, 1 hoa, 1 số.")

        # Hỏi người dùng có muốn kiểm tra tiếp
        while True:
            cont = input("Bạn có muốn kiểm tra mật khẩu khác? (y/n): ").lower()
            if cont == "n":
                print("Tạm biệt.")
                sys.exit(0)
            elif cont == "y":
                break
            else:
                print("⚠️ Chỉ nhập 'y' hoặc 'n'.")

# Gọi hàm chính
main()
