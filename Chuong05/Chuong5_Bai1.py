"""
nguyen thanh hau
24-0-00627
chuyen doi km sang dam
"""

import sys

MILES = 0.6214
tiepTuc = True

# Hàm chịu trách nhiệm chuyển đổi từ km sang dặm
# Input : số km người dùng nhập vào
def chuyenDoi(km):
    dam = km * MILES
    print(f"{km} Km transfer to miles is {dam:.2f} miles")

# Hàm chịu trách nhiệm nhận số km từ người dùng nhập vào
# Input : không có input
# Output : trả về số km người dùng đã được lọc
def getInput():
    try:
        userInput = float(input("Dial km :"))
        if userInput < 0:
            print("no even number")
            getInput()
        return userInput
    except ValueError:
        print("fail , only number not string , not even number ")
        getInput()

# Hàm chịu trách nhiệm chính logic , gọi các hàm con
def main():
    while tiepTuc:
        km = getInput()
        chuyenDoi(km)
        
        while tiepTuc:
            cont = input("Do you want to continue? (y/n): ").lower()
            if cont == "n":
                print("Goodbye.")
                sys.exit(0)
            elif cont == "y":
                break
            else:
                print("⚠️ Only 'y' or 'n' accepted.")

main()
