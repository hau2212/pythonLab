"""
Nguyễn Thanh Hậu
Bài 7 Chương 3
Tính điểm
"""

DIEMLIET = 50
DIEMLIETCHINH = 25

def check():
    try:
        kiemTraPhu_A = int(input("Nhập vào điểm kiểm tra phụ A (0-25): "))
        kiemTraPhu_B = int(input("Nhập vào điểm kiểm tra phụ B (0-25): "))
        kiemTraChinh = int(input("Nhập vào điểm kiểm tra chính (0-50): "))

        # Kiểm tra điểm có hợp lệ không
        if not (0 <= kiemTraPhu_A <= 25 and 0 <= kiemTraPhu_B <= 25 and 0 <= kiemTraChinh <= 50):
            print("❌ Điểm không hợp lệ. Vui lòng nhập lại.")
            check()
        else:
            tinhDiem(numA=kiemTraPhu_A, numB=kiemTraPhu_B, primary=kiemTraChinh)

    except ValueError:
        print("❌ Yêu cầu nhập đúng định dạng số nguyên.")
        check()

def tinhDiem(numA, numB, primary):
    tong = numA + numB + primary
    print(f"Tổng điểm của bạn là: {tong}")

    if tong < DIEMLIET or primary < DIEMLIETCHINH:
        print("👉 Kết quả: **Không đạt** (rớt)")
    else:
        if tong >= 80:
            print("👉 Kết quả: **Xuất sắc**")
        elif 60 < tong < 80:
            print("👉 Kết quả: **Tốt**")
        else:
            print("👉 Kết quả: **Đạt**")

check()
