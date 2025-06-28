"""
nguyễn thanh hậu
chương 2 bài 10
tính số lương nguyên liệu
"""

sugar_ingredent = 1.5 / 48
floar_ingredent = 2.75 / 48
butter_ingredent = 1 / 48

soLuong = int(input("nhap vao so luong banh muon lam : "))

total_sugar = soLuong * sugar_ingredent
total_floar = soLuong * floar_ingredent
total_butter = soLuong * butter_ingredent

print(f"so luong đường cần thiết là : {total_sugar:.2f} , bơ : {total_butter:.2f} , bột là : {total_floar:.2f}")