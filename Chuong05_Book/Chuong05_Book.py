"""
Nguyễn Thanh Hậu
MSSV: 24-0-00627
Chương 5 - Bài 2: Quản lý thời gian các hoạt động trong ngày
"""

def them_thoi_gian(hoat_dong, so_phut, bang_thoi_gian):
    """
    Thêm thời gian vào một hoạt động.

    Input:
        - hoat_dong (str): tên hoạt động.
        - so_phut (int): số phút thêm vào.
        - bang_thoi_gian (dict): dictionary chứa dữ liệu thời gian.

    Output:
        - Không có (dữ liệu được cập nhật trong dict truyền vào).
    """
    if hoat_dong in bang_thoi_gian:
        bang_thoi_gian[hoat_dong] += so_phut
    else:
        bang_thoi_gian[hoat_dong] = so_phut

def thong_ke_gio(bang_thoi_gian):
    """
    Thống kê thời gian của các hoạt động theo giờ.

    Input:
        - bang_thoi_gian (dict): dictionary chứa hoạt động và số phút.

    Output:
        - dict: dictionary mới với thời gian được chuyển sang giờ (float).
    """
    return {hd: round(phut / 60, 2) for hd, phut in bang_thoi_gian.items()}

def hoat_dong_max_min(bang_thoi_gian):
    """
    Tìm 2 hoạt động nhiều thời gian nhất và ít thời gian nhất.

    Input:
        - bang_thoi_gian (dict): dữ liệu hoạt động và số phút.

    Output:
        - tuple: gồm 2 list (2 hoạt động nhiều nhất, 2 hoạt động ít nhất)
    """
    sap_xep = sorted(bang_thoi_gian.items(), key=lambda x: x[1], reverse=True)
    hoat_dong_nhieu = sap_xep[:2]
    hoat_dong_it = sap_xep[-2:] if len(sap_xep) >= 2 else sap_xep
    return hoat_dong_nhieu, hoat_dong_it

def main():
    bang = {}

    # Nhập dữ liệu mẫu
    them_thoi_gian("Học", 300, bang)
    them_thoi_gian("Ngủ", 420, bang)
    them_thoi_gian("Chơi", 90, bang)
    them_thoi_gian("Di chuyển", 50, bang)
    them_thoi_gian("Thể dục", 60, bang)

    print("\n--- Thống kê theo giờ ---")
    gio = thong_ke_gio(bang)
    for hd, h in gio.items():
        print(f"{hd}: {h} giờ")

    nhieu, it = hoat_dong_max_min(bang)
    print("\n2 hoạt động nhiều thời gian nhất:")
    for hd, p in nhieu:
        print(f"{hd}: {p} phút")

    print("\n2 hoạt động ít thời gian nhất:")
    for hd, p in it:
        print(f"{hd}: {p} phút")

main()
