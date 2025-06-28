"""
Nguyễn thanh hậu
chương 2 bài 6
tính tiền trả góp
"""
LAI_XUAT = 0.05
soTienTraGop = float(input("nhap vao so tien tra gop : \n"))
soThangThanhToan = int(input("nhap vao so thang mong muon : \n"))
soTienThanhToanHangThang = 0
# Cộng thêm lãi suất vào tổng tiền phải trả
tongTienPhaiTra = soTienTraGop + (soTienTraGop * LAI_XUAT)

# Tính tiền phải trả hàng tháng
soTienThanhToanHangThang = tongTienPhaiTra / soThangThanhToan

print(f"Số tiền phải trả mỗi tháng là: {soTienThanhToanHangThang:.0f}")

