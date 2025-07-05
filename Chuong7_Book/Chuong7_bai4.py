"""
nguyen thanh hau
24-0-00627
chuong 7 bai 4
"""
import sys
import math

# Hàm kiểm tra một số có phải là số nguyên tố
# Input: n - số nguyên cần kiểm tra
# Output: True nếu là số nguyên tố, False nếu không
def laSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm tìm số nguyên tố đầu tiên lớn hơn n
# Input: n - số nguyên đầu vào
# Output: số nguyên tố đầu tiên lớn hơn n
def nextPrime(n):
    candidate = n + 1
    while True:
        if laSoNguyenTo(candidate):
            return candidate
        candidate += 1

# Hàm nhận số nguyên từ người dùng, đảm bảo hợp lệ
# Output: số nguyên dương được nhập
def getInput():
    try:
        userInput = int(input("Nhập một số nguyên bất kỳ: "))
        return userInput
    except ValueError:
        print("⚠️ Vui lòng nhập số nguyên.")
        return getInput()

# Hàm chính điều phối logic chương trình
def main():
    while True:
        n = getInput()
        ket_qua = nextPrime(n)
        print(f"Số nguyên tố đầu tiên lớn hơn {n} là: {ket_qua}")

        # Hỏi người dùng có muốn chạy tiếp không
        while True:
            cont = input("Bạn có muốn tiếp tục? (y/n): ").lower()
            if cont == "n":
                print("Tạm biệt.")
                sys.exit(0)
            elif cont == "y":
                break
            else:
                print("⚠️ Chỉ nhập 'y' hoặc 'n'.")

# Gọi hàm main
main()
