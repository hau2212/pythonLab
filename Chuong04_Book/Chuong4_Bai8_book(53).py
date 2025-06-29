"""
nguyen thanh hau
24-0-00627
bai 8
"""

def nhap_list_tang_dan():
    lst = []
    try:
        n = int(input("Nhập số lượng phần tử trong list tăng dần: "))
        for i in range(n):
            while True:
                try:
                    x = float(input(f"Phần tử thứ {i+1}: "))
                    if i == 0 or x >= lst[-1]:
                        lst.append(x)
                        break
                    else:
                        print("⚠️ Phần tử phải >= phần tử trước đó (để đảm bảo tăng dần).")
                except ValueError:
                    print("⚠️ Vui lòng nhập số thực.")
    except ValueError:
        print("⚠️ Nhập số nguyên.")
    return lst

def chen_vao_vi_tri_tang(lst, B):
    for i in range(len(lst)):
        if B < lst[i]:
            lst.insert(i, B)
            return
    # Nếu B lớn hơn tất cả, chèn vào cuối
    lst.append(B)

# === Chương trình chính ===
def main():
    lst = nhap_list_tang_dan()
    print("✅ List ban đầu:", lst)

    try:
        B = float(input("Nhập số thực B cần chèn: "))
        chen_vao_vi_tri_tang(lst, B)
        print("✅ List sau khi chèn:", lst)
    except ValueError:
        print("⚠️ B phải là số thực.")

main()
