"""
nguyen thanh hậu
24-0-00627
doi feet sang inch
"""
import tiep_tuc as TT
import ma_mau as m
FEET = 12

# Ham tich hop day du cac chuc nang trong do
def main():
    while True:
        try:
            inputSoFeet = float(input("nhap vao so feet muon chuyen : "))
            inch = lambda feet : feet * FEET
            print("\n"*10)
            print(m.mauChu["xanh_la"][0]+f"{inputSoFeet} Feet chuyen doi thanh {inch(inputSoFeet)} Inch "+m.mauChu["xanh_la"][1])
            TT.tiepTuc()
        except ValueError as A:
            print(str(A))

if __name__ == "__main__":
    main()