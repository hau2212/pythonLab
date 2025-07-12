"""
nguyen thanh hau
24-0-00627
ghi ten va diem vao file golf.txt
"""
danhSach =[]
tiepTuc = True
def ghi():

    while tiepTuc:
        try:
            print("nhap vao ten va diem 0 la dung")
            ten = input("nhap vao ten : ")
            diem = input("nhap vao diem : ")
            if ten == "0" or diem == "0":
                break
            danhSach.append(ten + " : " + diem)


        except Exception as a:
            print(str(a))

def fileGhi(filename):
    with open(filename , "w") as file:
        for line in danhSach:
           file.write(line + "\n")

ghi()
print(danhSach)
fileGhi("new.txt")