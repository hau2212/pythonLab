"""
nguyen thanh hau
24-0-00627
tinh no ngu
"""
THOI_GIAN = 8*7
SO_NGAY = 7
gioNgu = []

def tinhTHoiGianNgu():
    try:
        total = 0
        for i in range(1,SO_NGAY+1):
            gioNgu.append(float(input(f"nhap vao thoi gian ngu ngay {i} :")))

        for day in gioNgu:
            total += day

        if total > THOI_GIAN:
            print(f"ban ngu duoc {total} hon gio tieu chuan {THOI_GIAN} la : {total-THOI_GIAN}")
        elif total < THOI_GIAN:
            print(f"ban ngu duoc {total} thap hon gio tieu chuan {THOI_GIAN} la : {total - THOI_GIAN}")
        else:
            print("ban ngu du giac tot lam ")
    except ValueError:
        print("<UNK>")

tinhTHoiGianNgu()