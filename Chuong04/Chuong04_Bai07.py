"""
nguyễn thanh hậu
24-0-00627
tính độ dài của từ
"""
# Nguyễn Thanh Hậu
# 24-0-00627
# Tính độ dài của từ

doDai =[]
# tinh chieu dai cua ky tu nguoi dung nhap vao
def tinhDoDai():
    tiepTuc = True
    while tiepTuc:
        tu = input("Nhập vào từ bạn muốn xem độ dài (nhấn Enter để thoát): ").strip()
        if tu == "":
            print("Kết thúc chương trình.")
            tiepTuc = False
        else:
            chieuDai = len(tu)
            doDai.append(chieuDai)
            print(f"Độ dài của từ '{tu}' là: {chieuDai}")

tinhDoDai()
