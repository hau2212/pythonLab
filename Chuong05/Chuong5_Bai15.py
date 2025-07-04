"""
nguyen thanh hau
24-0-00627
bai 15 chuong 5
chuyen doi diem va tinh diem trung binh
"""
import tiep_tuc as t
import ma_mau as m

flag = True
diemChu = []
def chuyenDoi(diem):
    match diem:
        case _ if 100 >= diem >= 90:
            return "A"
        case _ if 89 >= diem >= 80:
            return "B"
        case _ if 79 >= diem >= 70:
            return "C"
        case _ if 69 >= diem >= 60:
            return "D"
        case _ if diem <= 59:
            return "F"
        case default:
            return "loi"

def main():
    tongDiem = 0
    while flag:
        try:
            while flag:
                soDiem = float(input("nhap vao diem so cua ban : "))
                if soDiem == 0:
                    break
                diemChu.append(chuyenDoi(soDiem))
                tongDiem += soDiem
            diemTrungBinh = tongDiem / len(diemChu)
            print(m.mauChu["do"][0]+f" diem trung binh cua ban la : {diemTrungBinh}"+m.mauChu["do"][1])
            for num in range(len(diemChu)):
                print(m.mauChu["xanh_nhat"][0]+f"diem chu thu {num} cua ban la : {diemChu[num]}"+m.mauChu["xanh_nhat"][1])

        except ValueError as A:
            print(str(A))
if __name__ == '__main__':
    main()
