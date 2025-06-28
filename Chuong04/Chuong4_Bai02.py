import tkinter as tk

CALO_GOT_BURNED = 4.2

def caloBiTieuTHu():
    # Lấy giá trị từ ô nhập
    input_text = input_user.get()
    if input_text.strip() == "":
        label_total.config(text="Vui lòng nhập số phút!")
        return
    try:
        thoiGian = int(input_text)
        total = 0
        for _ in range(thoiGian):
            total += CALO_GOT_BURNED

        label_total.config(text=f"Tổng calo tiêu thụ trong {thoiGian} phút là: {total}")
    except ValueError:
        label_total.config(text="Bạn phải nhập số nguyên!")

# Tạo cửa sổ
window = tk.Tk()
window.title("Tính calo bị đốt")
window.geometry("350x200")

# Label giới thiệu
new_label = tk.Label(window, text="App tính calo tiêu thụ bằng Tkinter")
new_label.pack(pady=10)

# Ô nhập dữ liệu
input_user = tk.Entry(window)
input_user.pack(pady=5)

# Nút bấm
btn = tk.Button(window, text="Tính calo", command=caloBiTieuTHu)
btn.pack(pady=5)

# Kết quả hiển thị
label_total = tk.Label(window, text="")
label_total.pack(pady=10)

# Chạy ứng dụng
window.mainloop()
