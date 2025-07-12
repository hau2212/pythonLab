"""
nguyen thanh hau
24-0-00627
chuong 6 bai 4
tim ban ghi cao diem nhat , va dem tong cac ban ghi
"""
import os ,sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_dir,  ".."))
print(project_path)
h = os.path.join(current_dir,"Ch6")
print(h)
sys.path.append(project_path)
from resource import res as a


# Hàm tìm số cao nhất và đánh dấu vị trí các số
def timDiemCao(fileName):
    try:
        highest = 0
        i = 1
        with open(os.path.join(h,fileName),"r") as file:
            for line in file:
                contentInt = int(line)
                contentStr = f"{i}: {contentInt} \n"

                print(contentStr)
                i+=1
                if highest <= contentInt:
                    highest = contentInt
            print(f"so cao nhat la : {highest}")
    except Exception as a:
        print(str(a))


timDiemCao("steps.txt")