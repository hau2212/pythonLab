"""
nguyen thanh hau
24-0-00627
bai 19 chuong 5
"""
import tiep_tuc as t

def tinh_thanh_toan_hang_thang(A, R, M):
    R = R / 100  # chuyển từ % sang thập phân
    P = (R * A) / (1 - (1 + R) ** -M)
    return P

def main():
    while True:
        try:
            # Nhập thông tin từ người dùng
            A = float(input("Nhập số tiền vay (VND): "))
            R = float(input("Nhập lãi suất hàng tháng (%): "))
            M = int(input("Nhập số tháng muốn trả góp: "))

            # Gọi hàm tính toán
            tien_thanh_toan = tinh_thanh_toan_hang_thang(A, R, M)

            # Hiển thị kết quả
            print(f"🌟 Mỗi tháng bạn cần thanh toán: {tien_thanh_toan:,.0f} VND")
            t.tiepTuc()
        except ValueError as A:
            print(str(A))
if __name__ == "__main__":
    main()
