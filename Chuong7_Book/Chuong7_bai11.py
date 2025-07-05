import math

# Hàm giải phương trình bậc hai ax^2 + bx + c = 0
# Input: a, b, c - hệ số của phương trình
# Output: list nghiệm (rỗng nếu vô nghiệm)
def giaiPTBacHai(a, b, c):
    if a == 0:
        # Trường hợp phương trình bậc nhất: bx + c = 0
        if b == 0:
            return []  # vô nghiệm
        return [-c / b]  # nghiệm duy nhất

    delta = b**2 - 4*a*c

    if delta < 0:
        return []  # vô nghiệm
    elif delta == 0:
        x = -b / (2 * a)
        return [x]
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return [x1, x2]

# Hàm kiểm thử
def main():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))

    nghiem = giaiPTBacHai(a, b, c)

    if not nghiem:
        print("❌ Phương trình vô nghiệm.")
    elif len(nghiem) == 1:
        print(f"✅ Phương trình có nghiệm kép: x = {nghiem[0]:.4f}")
    else:
        print(f"✅ Phương trình có 2 nghiệm: x1 = {nghiem[0]:.4f}, x2 = {nghiem[1]:.4f}")

# Gọi hàm chính
main()
