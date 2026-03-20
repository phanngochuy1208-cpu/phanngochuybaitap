import tkinter as tk
from tkinter import messagebox

# Các hàm mô phỏng
def my_strlen(s):
    return len(s)

def my_strcpy(s):
    return s

def my_strcat(s1, s2):
    return s1 + s2

# Hàm xử lý khi nhấn nút
def run_operations():
    s1 = entry1.get()
    s2 = entry2.get()

    strlen1 = my_strlen(s1)
    strlen2 = my_strlen(s2)

    strcpy_buf = my_strcpy(s1)
    strcat_buf = my_strcat(strcpy_buf, s2)
    strlen_buf = my_strlen(strcat_buf)

    result = (
        f"Chuỗi 1: [{s1}] ({strlen1})\n"
        f"Chuỗi 2: [{s2}] ({strlen2})\n\n"
        f"strcpy(buf, s1) rồi strcat(buf, s2):\n"
        f"[{strcat_buf}] ({strlen_buf})"
    )

    messagebox.showinfo("Kết quả", result)

# Tạo giao diện
root = tk.Tk()
root.title("Mô phỏng string.h trong Python")

tk.Label(root, text="Chuỗi 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root, width=40)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Chuỗi 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, width=40)
entry2.grid(row=1, column=1, padx=5, pady=5)

btn = tk.Button(root, text="Thực hiện", command=run_operations)
btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
