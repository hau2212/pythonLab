"""
nguyen thanh hau
chuong 5 bai 9
thế xuất bán hàng
"""
import ma_mau as m

THUE_TIEU_BANG = 0.025
THUE_QUAN = 0.05

def tinhThue(tongTien):
    totalThueQuan = tongTien * THUE_QUAN
    totalThueTieuBang = tongTien * THUE_TIEU_BANG
    return totalThueQuan ,totalThueTieuBang

def main():
    doanhThu = float(input("nhap vao doanh thu ban hang : "))
    thueQuan , thueTieuBang = tinhThue(tongTien=doanhThu)
    print(m.mauChu["xanh_la"][0] + f"thue phai tra cho quan la : {thueQuan}"+                    m.mauChu["xanh_la"][1])
    print(m.mauChu["xanh_duong"][0] + f"thue phai tra cho tieu bang la {thueTieuBang}"+          m.mauChu["xanh_duong"][1])
    print(m.mauChu["do"][0] + f"loi nhuan sau the la : {doanhThu - (thueQuan + thueTieuBang)}" + m.mauChu["do"][1])

if __name__ == '__main__':
    main()
