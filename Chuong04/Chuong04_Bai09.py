"""
nguyen thanh hau
24-0-00627
tinh muc nuoc bien trong vong 25
"""
MUC_NUOC_BIEN = 1.6

def tinhMucNuocBien():
    total = 0
    for i in range(1,24+1):
        total += MUC_NUOC_BIEN
        print(f"muc nuoc bien trong nam {i} la : {total:.2f}")

tinhMucNuocBien()