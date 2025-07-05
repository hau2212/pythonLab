import math

# Hàm tính cos(x) bằng chuỗi Taylor
# Input: x (góc tính bằng radian), epsilon là sai số dừng
# Output: giá trị gần đúng của cos(x)
def tinh_cos_taylor(x, epsilon=1e-10):
    term = 1.0          # hạng tử đầu tiên (n = 0)
    cos_x = term        # tổng ban đầu
    n = 1               # bắt đầu từ n = 1

    while abs(term) > epsilon:
        term *= (-1) * x * x / ((2 * n - 1) * (2 * n))  # công thức đệ quy
        cos_x += term
        n += 1

    return cos_x

# Hàm kiểm thử
def main():
    do = float(input("Nhập góc (độ): "))
    rad = math.radians(do)
    approx = tinh_cos_taylor(rad)
    actual = math.cos(rad)

    print(f"✅ cos({do}°) ≈ {approx:.10f} (theo Taylor)")
    print(f"🔍 So sánh với math.cos: {actual:.10f}")
    print(f"📉 Sai số tuyệt đối: {abs(actual - approx):.10f}")

# Gọi hàm chính
main()
