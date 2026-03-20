import tkinter as tk

def tinh_F():
    try:
        n = int(entry_n.get())
        F = 0
        
        for i in range(1, n+1):
            F += 1/(n**2 + i)
        
        label_kq.config(text="Fₙ = " + str(round(F,7)))
        
    except:
        label_kq.config(text="Vui lòng nhập số hợp lệ")

# tạo cửa sổ
window = tk.Tk()
window.title("Tính Fₙ")
window.geometry("320x200")

# tiêu đề
title = tk.Label(window, text="TÍNH GIÁ TRỊ Fₙ", font=("Arial",14))
title.pack(pady=10)

# nhập n
label_n = tk.Label(window, text="Nhập n:")
label_n.pack()

entry_n = tk.Entry(window)
entry_n.pack()

# nút tính
btn = tk.Button(window, text="Tính Fₙ", command=tinh_F)
btn.pack(pady=10)

# hiển thị kết quả
label_kq = tk.Label(window, text="")
label_kq.pack()

window.mainloop()
