import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Chọn file nguồn",
        filetypes=(("Tất cả file", "*.*"), ("File văn bản", "*.txt"), ("File C", "*.c"), ("File Python", "*.py"))
    )
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể mở file: {e}")
        return

    # Xóa nội dung cũ
    text_output.delete("1.0", tk.END)
    # Hiển thị nội dung file kèm số dòng
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
root.title("LINES - Hiển thị code kèm số dòng")

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

btn_open = tk.Button(frame_buttons, text="Mở file", command=open_file)
btn_open.pack(side=tk.LEFT, padx=5)

btn_save = tk.Button(frame_buttons, text="Lưu file có số dòng", command=save_file)
btn_save.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_output = tk.Text(root, width=100, height=30, yscrollcommand=scrollbar.set)
text_output.pack(padx=10, pady=10)

scrollbar.config(command=text_output.yview)

root.mainloop()
