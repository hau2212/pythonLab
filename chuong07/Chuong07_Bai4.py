"""
nguyen thanh hau
24-0-00627
chuong 7 bai 4 : nhập một chuỗi 20 số vào danh sách
"""

def kiemTra(tempt_danh_sach):
    try:
        tempt_high = max(tempt_danh_sach)
        tempt_low = min(tempt_danh_sach)
        tempt_total = sum(tempt_danh_sach)
        tempt_avg = tempt_total / len(tempt_danh_sach)

    except Exception as Er:
        print(str(Er))
    return tempt_high , tempt_low , tempt_avg , tempt_total

def main():
    try:
        danhSach = []
        times = 20
        for num in range(1,times+1):
            danhSach.append(int(input(f"nhap vao so cho Vi tri {num} :  ")))
        higest , lowest , avG , total = kiemTra(danhSach)
        print(f"so cao nhat la : {higest} \n so thap nhat la : {lowest} \n so trung binh la : {avG} \n so tong cong : {total}")
    except ValueError as Val:
        print(str(Val))
    except IndexError as Ind:
        print(str(Ind))

main()