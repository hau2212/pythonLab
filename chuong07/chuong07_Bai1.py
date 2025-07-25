"""
nguyen thanh hau
24-0-00627
chuong 07 bai
"""
numbers = [74, 19, 105, 20,-2,67, 77, 124, -45, 38]
new_list = []
def kiemTraDanhSach(number):
    new_list1 = []
    for num in number:
        if 0 <= num <= 100:
            new_list1.append(num)
    return new_list1

def main():
    new_list = kiemTraDanhSach(number=numbers)
    trungBinh = sum(new_list)/len(new_list)
    print("Danh sách sau khi lọc ra là : "+str(new_list))
    print("Trung binh cộng của các số là :" + str(trungBinh))
    print("ổng của các số là : " + str(sum(new_list)))
main()