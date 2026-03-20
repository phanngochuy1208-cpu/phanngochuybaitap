import tkinter as tk

# kiểm tra số là lũy thừa của 2
def la_luy_thua_2(n):
    return n > 0 and (n & (n - 1)) == 0

# xử lý chương trình
def xu_ly():
    try:
        arr = list(map(int, entry_arr.get().split()))
        x = int(entry_x.get())

        # đếm lũy thừa 2
        dem = 0
        for i in arr:
            if la_luy_thua_2(i):
                dem += 1

        # xóa phần tử bằng x
        arr_moi = []
        for i in arr:
            if i != x:
                arr_moi.append(i)

        kq = "Mảng: " + str(arr) + "\n"
        kq += "Có " + str(dem) + " số là lũy thừa của 2\n"
        kq += "Mảng sau khi xóa " + str(x) + ": " + str(arr_moi)

        label_kq.config(text=kq)

    except:
        label_kq.config(text="Dữ liệu nhập không hợp lệ!")

# cửa sổ
window = tk.Tk()
window.title("Bài 64 - Xử lý mảng")
window.geometry("400x300")

# nhập mảng
tk.Label(window, text="Nhập các phần tử (cách nhau bằng dấu cách):").pack()
entry_arr = tk.Entry(window, width=40)
entry_arr.pack(pady=5)

# nhập x
tk.Label(window, text="Nhập x cần xóa:").pack()
entry_x = tk.Entry(window)
entry_x.pack(pady=5)

# nút chạy
btn = tk.Button(window, text="Thực hiện", command=xu_ly)
btn.pack(pady=10)

# kết quả
label_kq = tk.Label(window, text="", justify="left")
label_kq.pack(pady=10)

window.mainloop()
