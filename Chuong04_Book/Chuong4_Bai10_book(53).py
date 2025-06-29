"""
nguyen thanh hau
24-0-00627
bai 10
"""

def tinh_can_bac_hai(x):
    guess = x / 2.0
    epsilon = 1e-12
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess

def main():
    try:
        x = float(input("Nhập số thực x ≥ 0 để tính căn bậc hai: "))
        if x < 0:
            print("⚠️ Không thể tính căn bậc hai của số âm.")
        elif x == 0:
            print("✅ Căn bậc hai của 0 là 0")
        else:
            can_x = tinh_can_bac_hai(x)
            print(f"✅ Căn bậc hai gần đúng của {x} là: {can_x:.12f}")
    except ValueError:
        print("⚠️ Vui lòng nhập một số hợp lệ.")

main()
