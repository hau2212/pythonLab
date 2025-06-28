""""
nguyen thanh hau
chuong 3 bai 15
may tinh thoi gian
"""

"""
Nguyen Thanh Hau
Bai 15 Chuong 3
May tinh thoi gian
"""

# Định nghĩa số giây trong mỗi đơn vị thời gian
GIAY_TRONG_PHUT = 60
GIAY_TRONG_GIO = 3600
GIAY_TRONG_NGAY = 86400

# Nhập số giây từ người dùng
soGiay = int(input("Nhập vào số giây: "))

# Kiểm tra và chuyển đổi
if soGiay >= GIAY_TRONG_NGAY:
    ngay = soGiay // GIAY_TRONG_NGAY
    soGiay %= GIAY_TRONG_NGAY
    gio = soGiay // GIAY_TRONG_GIO
    soGiay %= GIAY_TRONG_GIO
    phut = soGiay // GIAY_TRONG_PHUT
    giay = soGiay % GIAY_TRONG_PHUT
    print(f"Kết quả: {ngay} ngày, {gio} giờ, {phut} phút, {giay} giây.")
elif soGiay >= GIAY_TRONG_GIO:
    gio = soGiay // GIAY_TRONG_GIO
    soGiay %= GIAY_TRONG_GIO
    phut = soGiay // GIAY_TRONG_PHUT
    giay = soGiay % GIAY_TRONG_PHUT
    print(f"Kết quả: {gio} giờ, {phut} phút, {giay} giây.")
elif soGiay >= GIAY_TRONG_PHUT:
    phut = soGiay // GIAY_TRONG_PHUT
    giay = soGiay % GIAY_TRONG_PHUT
    print(f"Kết quả: {phut} phút, {giay} giây.")
else:
    print(f"Kết quả: {soGiay} giây.")
