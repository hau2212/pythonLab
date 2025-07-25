"""
Nguyễn Thanh Hậu - Chương 6 - Bài 7

Chức năng:
Viết hoa chữ cái đầu của mỗi từ trong chuỗi, còn lại viết thường.

Input:
    s (str): Chuỗi đầu vào (ví dụ: "nGuyeN hiEu NGhiA")

Output:
    (str): Chuỗi sau khi viết hoa chữ cái đầu mỗi từ (ví dụ: "Nguyen Hieu Nghia")
"""

def viet_hoa_chu_cai_dau(s):
    """
    Viết hoa chữ cái đầu mỗi từ trong chuỗi

    Input:
        s (str): chuỗi gốc

    Output:
        str: chuỗi sau khi viết hoa chữ cái đầu từ
    """
    tu_danh_sach = s.split()
    tu_viet_hoa = [tu.capitalize() for tu in tu_danh_sach]
    return ' '.join(tu_viet_hoa)

def main():
    """
    Hàm chính để nhập chuỗi và xử lý
    """
    chuoi = input("Nhập chuỗi: ")
    ket_qua = viet_hoa_chu_cai_dau(chuoi)
    print("Chuỗi sau khi chuẩn hóa:", ket_qua)

# Gọi hàm main
main()
