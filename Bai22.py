import tkinter as tk
from tkinter import messagebox

def tinh_uoc():
    try:
        n = int(entry_n.get())
        uoc = []
        tong = 0

        for i in range(1, n + 1):
            if n % i == 0:
                uoc.append(i)
                tong += i

        ketqua = f"Các ước số: {uoc}\n"
        ketqua += f"Có {len(uoc)} ước số\n"
        ketqua += f"Tổng các ước: {tong}"

        label_kq.config(text=ketqua)

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên dương!")

# Tạo cửa sổ
window = tk.Tk()
window.title("Liệt kê ước số")
window.geometry("350x200")

# Nhập số n
label_n = tk.Label(window, text="Nhập n:")
label_n.pack()

entry_n = tk.Entry(window)
entry_n.pack()

# Nút tính
btn = tk.Button(window, text="Tính ước số", command=tinh_uoc)
btn.pack(pady=10)

# Hiển thị kết quả
label_kq = tk.Label(window, text="")
label_kq.pack()

# Chạy chương trình
window.mainloop()
