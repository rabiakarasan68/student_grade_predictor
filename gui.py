import tkinter as tk
import joblib 
from utils import harf_notu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

model = joblib.load("model.pkl")

def tahmin():
    v = float(entry_vize.get())
    k = float(entry_katilim.get())
    result = model.predict([[v,k]])
    harf = harf_notu(result[0])

    # label_final = tk.Label(root, text="")
    # label_final.grid(row=3, column=0, columnspan=1)

    # label_harf = tk.Label(root, text="")
    # label_harf.grid(row=4, column=0, columnspan=2)

    label.config(text = f"Tahmin: {result[0]:.2f} | Harf Notu: {harf}")
    # label.config(text = f"Harf Notu: {harf}")

canvas = None

def grafik():
    global canvas

    v = float(entry_vize.get())
    k = float(entry_katilim.get())

    pred = model.predict([[v, k]])[0]

    gercek = [v, k, 100]
    tahmin = [v, k, pred]

    fig = plt.Figure(figsize=(4,3))
    ax = fig.add_subplot(111)

    ax.plot(gercek, label="Gerçek (input)")
    ax.plot(tahmin, label="Tahmin")
    ax.legend()

    if canvas:
        canvas.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("AI Not Tahmin Sistemi")
root.geometry("400x500")

tk.Label(root, text="Vize Notu").pack()
entry_vize = tk.Entry(root)
entry_vize.pack()

tk.Label(root, text="Katılım").pack()
entry_katilim = tk.Entry(root)
entry_katilim.pack()

btn = tk.Button(root, text="Tahmin Et", command=tahmin)
btn.pack()

btn = tk.Button(root, text="Grafik göster", command=grafik)
btn.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
