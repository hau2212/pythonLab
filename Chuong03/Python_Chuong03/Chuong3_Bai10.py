pennies = 1
niken = 5
dimes = 10
quarters = 25

DOLAR = 100

soPennies = int(input("nhap vao so pennis 1 cent : "))
soNiken = int(input("nhap vao so niken 5 cent : "))
soDimes = int(input("nhap vao so dimes 10 cent : "))
soQuartes = int(input("nhap vao so quartes 25 cent : "))

total = soPennies + soQuartes + soDimes + soNiken

if total == DOLAR:
    print("chuc mung ban chon dung ")
else:
    print("chia buon ban da chon ", "du " if total > DOLAR else "thieu")