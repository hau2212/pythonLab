"""
nguyen thanh hau
24-0-00627
Viết một chương trình lấy chuỗi chứa họ và tên của một người dưới dạng các giá trị riêng biệt,
sau đó hiển thị "tên viết tắt",
 "tên trong sổ địa chỉ" và "tên người dùng" của họ. Ví dụ: nếu người dùng nhập tên của "John" và họ của "Smith",
 chương trình sẽ hiển thị "JS", "John SMITH" và "jsmith".
"""

class Name():
    def __init__(self):
        self.__name = "default"
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value


def formatString(temptString):
    try:
        tempt_string = temptString.split()
        return (f"case 1 : {tempt_string[0][0].upper() + tempt_string[-1][0].upper()} \n"
                f"case 2 : {tempt_string[0] +" "+ tempt_string[-1].upper()} \n"
                f"case 3 : {tempt_string[0][0] + tempt_string[-1]}")

    except Exception as Ex:
        print(str(Ex))
def main():
    tiepTuc = True
    h = Name()
    try:
        while tiepTuc:
            name = input("nhap ten vao : ")
            h.name = name
            print(formatString(h.name))

    except Exception as Ex:
        print(str(Ex))

main()