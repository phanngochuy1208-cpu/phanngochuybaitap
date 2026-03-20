import tkinter as tk
import random

# tạo ma trận 3x3 ngẫu nhiên
def tao_ma_tran():
    global A
    A = [[random.randint(0,9) for j in range(3)] for i in range(3)]
    
    text_A.delete("1.0", tk.END)
    
    for row in A:
        text_A.insert(tk.END, " ".join(map(str,row)) + "\n")

# nhân hai ma trận 3x3
def nhan_ma_tran(X, Y):
    C = [[0]*3 for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += X[i][k] * Y[k][j]
                
    return C

# tính A^k
def tinh_luy_thua():
    try:
        k = int(entry_k.get())
        
        result = A
        
        for i in range(k-1):
            result = nhan_ma_tran(result, A)
            
        text_kq.delete("1.0", tk.END)
        
        for row in result:
            text_kq.insert(tk.END, " ".join(map(str,row)) + "\n")
            
    except:
        text_kq.insert(tk.END,"Nhập k hợp lệ")

# giao diện
window = tk.Tk()
window.title("Bài 93 - Lũy thừa ma trận")
window.geometry("420x350")

tk.Label(window,text="Ma trận A (3x3):",font=("Arial",12)).pack()

text_A = tk.Text(window,height=4,width=20)
text_A.pack()

tk.Button(window,text="Tạo ma trận",command=tao_ma_tran).pack(pady=5)

tk.Label(window,text="Nhập k (k > 1):").pack()
entry_k = tk.Entry(window)
entry_k.pack()

tk.Button(window,text="Tính A^k",command=tinh_luy_thua).pack(pady=10)

tk.Label(window,text="Kết quả A^k:",font=("Arial",12)).pack()

text_kq = tk.Text(window,height=5,width=25)
text_kq.pack()

window.mainloop()
