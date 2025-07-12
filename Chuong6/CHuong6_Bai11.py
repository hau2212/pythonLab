"""
nguyen thanh hau
24-0-00627

"""

# 11. Trình tạo trang web cá nhân
# Tác giả: nguyen thanh hau

def tao_trang_web():
    # Nhập từ người dùng
    ten = input("Nhập tên của bạn: ")
    mo_ta = input("Mô tả bản thân: ")

    # Tạo nội dung HTML
    noi_dung = f"""
    <html>
    <head>
        <title>Trang cá nhân của {ten}</title>
    </head>
    <body>
        <center>
            <h1>{ten}</h1>
        </center>
        <hr />
        <p>{mo_ta}</p>
        <hr />
    </body>
    </html>
    """

    # Ghi vào file
    with open("trang_ca_nhan.html", "w", encoding="utf-8") as f:
        f.write(noi_dung)

    print("✅ Đã tạo file trang_ca_nhan.html thành công!")

# Gọi hàm
tao_trang_web()
