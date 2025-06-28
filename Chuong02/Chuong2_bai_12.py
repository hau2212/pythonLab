"""
Nguyễn thanh hậu
chương 2 bài 12
tính lời lỗ chứng khoán
"""
stock = 2000
giaMua = 40.00
phanTramMoiGioi = 0.03
giaBan = 42.75

giaTriMua = stock * giaMua
traMoiGioiKhiMua = giaTriMua * phanTramMoiGioi
print(f"tien joe chi mua vao la                  : {giaTriMua}")
print(f"số tiền phải trả môi giới khi mua vào là : {traMoiGioiKhiMua}")

giaTriBan = stock * giaBan
traMoiGioiKhiBan = giaTriBan * phanTramMoiGioi
print(f"so tien joe ban duoc la                   : {giaTriBan}")
print(f"so tien phải trả môi giới khi bán là       : {traMoiGioiKhiBan}")

tinhLoiNhuan = (giaTriMua + traMoiGioiKhiMua ) - (giaTriBan - traMoiGioiKhiBan)
print(f"suy ra joe lo : {tinhLoiNhuan:.2f}")