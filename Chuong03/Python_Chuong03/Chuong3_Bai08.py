"""
nguyen thanh hau
chuong 3 bai 8
tinh hotdag

"""
import math

motGoiXucXich = 10
motGoiBanh = 8
soLuongCan = 0
soLuongGoiXucXich = 0
soLuongGoiBanh = 0

soLuongXUcXichThua = 0
soLuongBanhThua = 0

nguoiThamDu = int(input("nhap vao so người : "))
quaTang = int(input("nhap vao so qua moi nguoi duoc tang"))


soLuongCan = nguoiThamDu * quaTang
soLuongGoiXucXich = math.ceil(soLuongCan / motGoiXucXich)
soLuongGoiBanh = math.ceil(soLuongCan / motGoiBanh )
soLuongXUcXichThua = (soLuongGoiXucXich * motGoiXucXich) - soLuongCan
soLuongBanhThua = (soLuongGoiBanh * motGoiBanh)-soLuongCan
print(f"so luong hotdog can la : {soLuongCan}")
print(f"so luong goi xuc xich can la : {soLuongGoiXucXich}")
print(f"so luong goi banh can la {soLuongGoiBanh}")
print(f"so luong xuc xich thua la {soLuongXUcXichThua}")
print(f"so luong goi banh thua la : {soLuongBanhThua}")

