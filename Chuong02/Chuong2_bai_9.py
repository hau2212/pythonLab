"""
nguyen thanh hậu
chương 2 bài 9
đo vòng tròn
"""

import math

# Nhập bán kính
ban_kinh = float(input("Nhập bán kính của vòng tròn: "))

# Tính diện tích và chu vi
dien_tich = math.pi * ban_kinh ** 2
chu_vi = 2 * math.pi * ban_kinh

# Hiển thị kết quả
print(f"Diện tích hình tròn là   : {dien_tich:.2f}")
print(f"Chu vi hình tròn    là   : {chu_vi:.2f}")
