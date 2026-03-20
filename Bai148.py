import tkinter as tk
from tkinter import messagebox

# Hàm Bubble Sort đệ quy (giảm dần)
def bubble_sort_recursive(arr, n):
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:  # đổi chỗ để sắp xếp giảm dần
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)

def run_sort():
    try:
        # Lấy dữ liệu từ ô nhập, chuyển thành list số nguyên
        arr = list(map(int, entry.get().strip().split()))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập các số nguyên cách nhau bởi khoảng trắng!")
        return

    original = arr.copy()
    bubble_sort_recursive(arr, len(arr))

    result_text = (
        f"Mảng gốc: {original}\n"
        f"Mảng giảm: {arr}"
    )
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result_text)

# Tạo giao diện
root = tk.Tk()
root.title("Bubble Sort đệ quy - Sắp xếp giảm dần")

tk.Label(root, text="Nhập mảng (cách nhau bởi khoảng trắng):").grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1, padx=5, pady=5)

btn = tk.Button(root, text="Sắp xếp", command=run_sort)
btn.grid(row=1, column=0, columnspan=2, pady=10)

text_output = tk.Text(root, width=60, height=10)
text_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
