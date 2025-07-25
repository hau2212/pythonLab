"""
Nguyễn Thanh Hậu - Chương 6 - Bài 4

Chức năng:
Tìm các giá trị tốc độ quay nhỏ hơn một giá trị min trong danh sách,
và trả về cả giá trị đó lẫn chỉ số (index) tương ứng.

Input:
    speeds (list of int): danh sách tốc độ quay của động cơ
    min_value (int): giá trị tốc độ tối thiểu để so sánh

Output:
    (list): danh sách tuple dạng (giá trị, chỉ số) với các tốc độ nhỏ hơn min
"""

def tim_toc_do_thap(speeds, min_value):
    """
    Tìm các tốc độ quay nhỏ hơn min_value và chỉ số của chúng.

    Input:
        speeds (list of int): danh sách tốc độ quay
        min_value (int): giá trị tối thiểu

    Output:
        result (list of tuple): mỗi tuple gồm (giá trị, chỉ số)
    """
    result = []
    for i in range(len(speeds)):
        if speeds[i] < min_value:
            result.append((speeds[i], i))
    return result

def main():
    """
    Hàm chính để nhập dữ liệu và hiển thị kết quả.
    """
    speeds = [1000, 950, 1200, 850, 1100, 800]
    min_value = 1000
    ket_qua = tim_toc_do_thap(speeds, min_value)

    print("Các tốc độ quay nhỏ hơn", min_value, "và chỉ số tương ứng:")
    for value, index in ket_qua:
        print(f"Giá trị: {value} - Vị trí: {index}")

# Gọi hàm main
main()
