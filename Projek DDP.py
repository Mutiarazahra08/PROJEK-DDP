import tkinter as tk

def hitung_rata_rata():
    # Mengambil nilai dari setiap entry widget dan memprosesnya
    nilai_1 = float(entry_nilai_1.get())
    nilai_2 = float(entry_nilai_2.get())
    nilai_3 = float(entry_nilai_3.get())

    # Menghitung rata-rata
    rata_rata = (nilai_1 + nilai_2 + nilai_3) / 3
    label_hasil.config(text=f"Rata-rata: {rata_rata:.2f}")

# Membuat instance Tkinter
root = tk.Tk()
root.geometry("500x400")
root.title("Hitung Rata-rata 3 Nilai")

# Membuat label dan entry untuk setiap nilai
label_nilai_1 = tk.Label(root, text="Nilai 1:")
label_nilai_1.pack(pady=5)

entry_nilai_1 = tk.Entry(root)
entry_nilai_1.pack()

label_nilai_2 = tk.Label(root, text="Nilai 2:")
label_nilai_2.pack(pady=5)

entry_nilai_2 = tk.Entry(root)
entry_nilai_2.pack()

label_nilai_3 = tk.Label(root, text="Nilai 3:")
label_nilai_3.pack(pady=5)

entry_nilai_3 = tk.Entry(root)
entry_nilai_3.pack()

# Tombol untuk menghitung rata-rata
tombol_hitung = tk.Button(root, text="Hitung Rata-rata", command=hitung_rata_rata, font=("Arial", 10), bg="green", fg="white")
tombol_hitung.pack(pady=10, padx=5)

# Label untuk menampilkan hasil rata-rata
label_hasil = tk.Label(root, text="")
label_hasil.pack()

# Menjalankan loop Tkinter
root.mainloop()