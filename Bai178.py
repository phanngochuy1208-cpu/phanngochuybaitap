import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Chọn file nguồn",
        filetypes=(("Tất cả file", "*.*"), ("File Python", "*.py"), ("File C", "*.c"))
    )
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể mở file: {e}")
        return

    text_output.delete("1.0", tk.END)
    for i, line in enumerate(lines):
        text_output.insert(tk.END, f"{i}: {line}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Lưu file mới",
        defaultextension=".txt",
        filetypes=(("Text file", "*.txt"), ("Tất cả file", "*.*"))
    )
    if not file_path:
        return

    try:
        content = text_output.get("1.0", tk.END)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Thành công", "Đã lưu file với số thứ tự dòng.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu file: {e}")

# Tạo giao diện
root = tk.Tk()
root.title("LINES - Hiển thị file kèm số dòng")

btn_open = tk.Button(root, text="Mở file", command=open_file)
btn_open.pack(pady=5)

btn_save = tk.Button(root, text="Lưu file có số dòng", command=save_file)
btn_save.pack(pady=5)

text_output = tk.Text(root, width=80, height=25)
text_output.pack(padx=10, pady=10)

root.mainloop()
