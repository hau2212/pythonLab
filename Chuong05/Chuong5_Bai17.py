"""
nguyen thanh hau
24-0-00627
bai 17 chuong 5
tinh so nguyen to
"""
def is_prime(num):
    if num < 2:
        return False  # 0 và 1 không phải số nguyên tố
    for so in range(2, int(num**0.5) + 1):
        if num % so == 0:
            return False
    return True  # chỉ return True sau khi đã kiểm tra hết
print(int(10**0.5))
def main():
    so = int(input("nhap vao so can kiem tra : "))
    if is_prime(so):
        print("la so nguyen to")
    else:
        print("khong phai la so nguyen to")

if __name__ == '__main__':
    main()