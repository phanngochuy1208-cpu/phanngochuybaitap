import tkinter as tk
import math

def tinh_cos():
    try:
        x = float(entry.get())   # x tính bằng phút
        
        degree = x / 60          # đổi phút -> độ
        rad = math.radians(degree)  # đổi độ -> radian
        
        result = math.cos(rad)
        
        label_result.config(text="cos(x) = " + str(round(result,6)))
        
    except:
        label_result.config(text="Nhập số hợp lệ!")

# tạo cửa sổ
window = tk.Tk()
window.title("Tính cos(x)")
window.geometry("320x200")

# tiêu đề
title = tk.Label(window, text="TÍNH COS(x)", font=("Arial",14))
title.pack(pady=10)

# nhập dữ liệu
tk.Label(window, text="Nhập x (phút):").pack()
entry = tk.Entry(window)
entry.pack()

# nút tính
btn = tk.Button(window, text="Tính", command=tinh_cos)
btn.pack(pady=10)

# kết quả
label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
