"""
nguyen thanh hau
24-0-00627
tang hoc phi
"""

HOC_PHI = 8000

def tinhHocPhi():
    global HOC_PHI
    for i in range(1, 5+1):
        HOC_PHI += HOC_PHI * 0.03
        print(f"hojc phi ki {i} la : {HOC_PHI:.2f}")


tinhHocPhi()