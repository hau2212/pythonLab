"""
nguyen thanh hau
24-0-00627
chuong 7 bai 6
"""
import sys

# Hàm chuyển từ hệ 2, 10 hoặc 16 về số thập phân
# Input: chuỗi số và hệ số gốc (2, 10 hoặc 16)
# Output: số nguyên thập phân (int) hoặc None nếu lỗi
def chuyenVeThapPhan(gia_tri, he):
    try:
        return int(gia_tri, base=he)
    except ValueError:
        print("⚠️ Lỗi: Giá trị không hợp lệ cho hệ", he)
        return None

# Hàm chuyển từ số thập phân sang nhị phân và thập lục phân
# Input: một số nguyên thập phân
# Output: in ra dạng nhị phân và thập lục
def hienThiCacHe(so_thap_phan):
    print(f"🔢 Giá trị thập phân: {so_thap_phan}")
    print(f"💻 Hệ nhị phân   : {bin(so_thap_phan)[2:]}")
    print(f"📦 Hệ thập lục   : {hex(so_thap_phan)[2:].upper()}")

# Hàm nhận đầu vào từ người dùng: hệ và giá trị
# Output: tuple (base, value)
def getInput():
    print("\n🎯 Hệ số được hỗ trợ: 2 (nhị phân), 10 (thập phân), 16 (thập lục phân)")
    try:
        base = int(input("Nhập hệ số gốc (2/10/16): "))
        if base not in [2, 10, 16]:
            print("⚠️ Chỉ hỗ trợ hệ 2, 10 và 16.")
            return None, None

        value = input(f"Nhập giá trị cần chuyển (hệ {base}): ").strip()
        return base, value
    except ValueError:
        print("⚠️ Lỗi: Hệ số phải là số nguyên.")
        return None, None

# Hàm chính điều phối chương trình
def main():
    while True:
        base, value = getInput()
        if base is None:
            continue

        so_thap_phan = chuyenVeThapPhan(value, base)
        if so_thap_phan is not None:
            hienThiCacHe(so_thap_phan)

        # Hỏi người dùng có muốn tiếp tục không
        while True:
            cont = input("Bạn có muốn tiếp tục? (y/n): ").lower()
            if cont == "n":
                print("Tạm biệt.")
                sys.exit(0)
            elif cont == "y":
                break
            else:
                print("⚠️ Chỉ nhập 'y' hoặc 'n'.")

# Gọi chương trình
main()
