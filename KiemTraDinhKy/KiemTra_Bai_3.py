"""
Nguyễn Thanh Hậu
24-0-00627
Kiểm tra định kỳ - Câu 3: mã hóa và giải mã ceaser
"""

# Bảng chữ cái thường và hoa
chu_cai_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_cai_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Mã hóa chuỗi bằng dịch chuyển chữ cái k bước (không dùng ord).
# text: chuỗi đầu vào (str)
# k: số bước dịch (int)
# return: chuỗi đã mã hóa (str)
def ma_hoa(text, k):
    ket_qua = ""
    for ky_tu in text:
        if ky_tu in chu_cai_thuong:
            vi_tri = chu_cai_thuong.index(ky_tu)
            moi = (vi_tri + k) % 26
            ket_qua += chu_cai_thuong[moi]
        elif ky_tu in chu_cai_hoa:
            vi_tri = chu_cai_hoa.index(ky_tu)
            moi = (vi_tri + k) % 26
            ket_qua += chu_cai_hoa[moi]
        else:
            ket_qua += ky_tu  # Ký tự khác giữ nguyên
    return ket_qua

# Giải mã chuỗi đã mã hóa bằng cách dịch ngược lại k bước.
# Return: chuỗi gốc
def giai_ma(text, k):

    return ma_hoa(text, -k)

# Hàm main chịu trách nhiệm xử lý chính
# Lựa chọn giải mã và mã hóa
# Input : chuỗi Text để xử lý
# Output : kết quả tương ứng
def main():
    text = input("Nhập chuỗi cần xử lý: ")
    try:
        k = int(input("Nhập khóa k (số nguyên): "))
    except:
        print("Vui lòng nhập số nguyên!")
        return

    print("1. Mã hóa")
    print("2. Giải mã")
    chon = input("Chọn chức năng (1 hoặc 2): ")

    if chon == "1":
        print("Kết quả mã hóa:", ma_hoa(text, k))
    elif chon == "2":
        print("Kết quả giải mã:", giai_ma(text, k))
    else:
        print("Bạn đã chọn sai!")

# Gọi hàm chính
main()
