# Hàm viết hoa chữ cái đầu của mỗi từ trong chuỗi
# Input: một chuỗi bất kỳ (str)
# Output: chuỗi đã được chuẩn hóa viết hoa đầu từ
def chuanHoaVietHoaChuDau(text):
    words = text.split()
    result = [word.capitalize() for word in words]
    return " ".join(result)

# Hàm kiểm thử
def main():
    s = input("Nhập chuỗi cần chuẩn hóa: ")
    ket_qua = chuanHoaVietHoaChuDau(s)
    print(f"✅ Chuỗi sau chuẩn hóa: {ket_qua}")

# Gọi hàm main
main()
