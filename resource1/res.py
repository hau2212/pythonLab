import sys

mauChu = {
    "do": ["\033[91m", "\033[0m"],
    "xanh_la": ["\033[92m", "\033[0m"],
    "vang": ["\033[93m", "\033[0m"],
    "xanh_duong": ["\033[94m", "\033[0m"],
    "tim": ["\033[95m", "\033[0m"],
    "xanh_nhat": ["\033[96m", "\033[0m"],
    "trang": ["\033[97m", "\033[0m"]
}



def tiepTuc():
    """
    ham tiep tuc
    Returns:

    """
    while True:
        luaChon = input("Bạn muốn tiếp tục không (y/n): ").strip().lower()
        if luaChon == "n":
            print("Tạm biệt!")
            sys.exit()
        elif luaChon == "y":
            print("\n" * 10)
            break
        else:
            print("\n" * 10)
            print("Bạn nhập sai, chương trình sẽ tiếp tục.")
            break
