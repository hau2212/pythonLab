"""
Nguyễn Thanh Hậu
MSSV: 24-0-00627
Chương 5 - Bài 1: Đếm số lần xuất hiện của các chữ cái trong một câu
"""

def dem_chu_cai(cau):
    """
    Đếm số lần xuất hiện của các chữ cái trong câu (bỏ qua dấu câu và khoảng trắng).

    Input:
        - cau (str): chuỗi câu cần đếm ký tự.

    Output:
        - dict: dictionary chứa ký tự (chữ cái) làm key, số lần xuất hiện làm value.
    """
    ket_qua = {}
    for char in cau:
        if char.isalpha():  # chỉ đếm chữ cái
            if char in ket_qua:
                ket_qua[char] += 1
            else:
                ket_qua[char] = 1
    return ket_qua

def main():
    cau = "An eye for an eye makes the whole world blind. – Mahatma Gandhi"
    thong_ke = dem_chu_cai(cau)
    for chu, so_lan in sorted(thong_ke.items()):
        print(f"'{chu}': {so_lan} lần")

main()
