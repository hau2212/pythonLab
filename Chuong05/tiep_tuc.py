import sys


import sys

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
