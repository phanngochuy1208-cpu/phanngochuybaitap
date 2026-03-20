import tkinter as tk
from tkinter import messagebox

# Hàm nhân hai số lớn dạng chuỗi
def multiply_strings(num1, num2):
    # Chuyển sang int để nhân, sau đó lại về chuỗi
    result = str(int(num1) * int(num2))
    return result

def run_multiplication():
    s1 = entry1.get().strip()
    s2 = entry2.get().strip()

    if not (s1.isdigit() and s2.isdigit()):
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên dương hợp lệ!")
        return

    product = multiply_strings(s1, s2)

    result_text = f"Số bị nhân: {s1}\nSố nhân: {s2}\n\nKết quả: {product}"
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result_text)

# Tạo giao diện
root = tk.Tk()
root.title("Nhân số lớn dạng chuỗi")

tk.Label(root, text="Số bị nhân:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root, width=40)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Số nhân:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, width=40)
entry2.grid(row=1, column=1, padx=5, pady=5)

btn = tk.Button(root, text="Thực hiện nhân", command=run_multiplication)
btn.grid(row=2, column=0, columnspan=2, pady=10)

text_output = tk.Text(root, width=60, height=10)
text_output.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
