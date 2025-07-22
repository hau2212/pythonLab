"""
Nguyễn Thanh Hậu
MSSV: 24-0-00627
Kiểm tra định kỳ - Câu 2: Kiểm tra mật khẩu bảo mật cao
"""
import random
tiepTuc1 = True

# Hàm sinh mật khẩu ngẫu nhiên đủ mạnh với độ dài tối thiểu.
# Input length (int): độ dài mật khẩu cần tạo (nên >= 8)
# Output str: mật khẩu được tạo ra
def sinh_mat_khau(length):
    if length < 8:
        length = 8  # bắt buộc phải >= 8

    # Các nhóm ký tự
    chu_thuong = "abcdefghijklmnopqrstuvwxyz"
    chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    so = "0123456789"
    dac_biet = "!@#$%^&*"

    # Đảm bảo có ít nhất 1 ký tự của mỗi loại
    mat_khau = random.choice(chu_thuong)
    mat_khau += random.choice(chu_hoa)
    mat_khau += random.choice(so)
    mat_khau += random.choice(dac_biet)

    # Các ký tự còn lại chọn ngẫu nhiên trong tất cả nhóm
    tat_ca = chu_thuong + chu_hoa + so + dac_biet
    for _ in range(length - 4):
        mat_khau += random.choice(tat_ca)

    # Trộn ngẫu nhiên thứ tự các ký tự
    mat_khau = list(mat_khau)
    random.shuffle(mat_khau)

    return ''.join(mat_khau)

# Kiểm tra mật khẩu có đủ mạnh không.
# Input: mat_khau (str): chuỗi mật khẩu cần kiểm tra
# Output: True nếu mật khẩu mạnh, False nếu không"""
def kiem_tra_mat_khau(mat_khau):

    if len(mat_khau) < 8:
        return False

    co_thuong = False
    co_hoa = False
    co_so = False
    co_ky_tu_dac_biet = False

    for ky_tu in mat_khau:
        if ky_tu.islower():
            co_thuong = True
        elif ky_tu.isupper():
            co_hoa = True
        elif ky_tu.isdigit():
            co_so = True
        elif not ky_tu.isalnum():
            co_ky_tu_dac_biet = True

    return co_thuong and co_hoa and co_so and co_ky_tu_dac_biet

# Hàm nhập mật khẩu từ người dùng và kiểm tra bảo mật.
# Input: không có
# Output: không trả về, chỉ in ra kết quả
def nhap_mat_khau():
    mk = input("Nhập mật khẩu cần kiểm tra: ")
    if kiem_tra_mat_khau(mk):
        print(" Mật khẩu mạnh (bảo mật cao).")
    else:
        print(" Mật khẩu yếu. Vui lòng thử lại.")

def main():
    while tiepTuc1:
        nhap_mat_khau()
        taoMatKhau = input("bạn có muốn tạo mật khẩu không (n/y) : ")
        if taoMatKhau == "y":
            doDai = int(input("nhập vào độ dài mật khẩu (số nguyên) : "))
            matKhau = sinh_mat_khau(doDai)
            print(f"mật khẩu của bạn là {matKhau}.")
        tiepTuc = input("bạn có muốn tiếp tc không y/n : ")
        if tiepTuc.lower() == "n":
            print("bye bye")
            break
        elif tiepTuc.lower() == "y":
            continue
        else:
            print("bạn nhập sai mặc định là tiếp tục : ")

main()
