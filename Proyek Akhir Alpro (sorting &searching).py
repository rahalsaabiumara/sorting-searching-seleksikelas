import tkinter as tk
from tkinter import ttk, messagebox

class SeleksiUjianApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Seleksi Ujian Kelas Unggul 2023")
        self.original_data_mahasiswa = [
            {"nama": "Bambang", "nilai": 80},
            {"nama": "Irfan", "nilai": 65},
            {"nama": "Yanto", "nilai": 90},
            {"nama": "Yanti", "nilai": 75},
            {"nama": "Putri", "nilai": 85},
            {"nama": "Anton", "nilai": 60},
            {"nama": "Budi", "nilai": 78},
            {"nama": "Miko", "nilai": 92},
            {"nama": "Rizki", "nilai": 68},
            {"nama": "Irma", "nilai": 88},
            {"nama": "Rahalsa", "nilai": 95},
            {"nama": "Erma", "nilai": 72},
            {"nama": "Erna", "nilai": 83},
            {"nama": "Krisna", "nilai": 67},
            {"nama": "Mawar", "nilai": 89},
            {"nama": "Budiman", "nilai": 76},
            {"nama": "Luthfi", "nilai": 93},
            {"nama": "Mikha", "nilai": 70},
            {"nama": "Mikail", "nilai": 82},
            {"nama": "Bimo", "nilai": 64},
            {"nama": "Bima", "nilai": 87},
            {"nama": "Wati", "nilai": 79},
            {"nama": "Wawan", "nilai": 74},
            {"nama": "Jamal", "nilai": 91},
            {"nama": "Andre", "nilai": 66},
        ]

        self.data_mahasiswa = list(self.original_data_mahasiswa)

        self.tree = ttk.Treeview(self.master, columns=("Nama", "Nilai"), show="headings")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Nilai", text="Nilai")
        self.tree.pack(pady=10) #membuat tabel dengan entitas nama dan nilai

        self.update_list_box() #memperbarui tampilan tabel yang berisi data nama dan nilai

        self.sort_label = tk.Label(self.master, text="Sort by:")
        self.sort_label.pack() #tata letak objek Label

        self.sort_var = tk.StringVar() #menyimpan nilai terpilih pada cmbbox
        self.sort_combobox = ttk.Combobox(self.master, values=["Nama", "Nilai"], textvariable=self.sort_var) #objek cmbbox
        self.sort_combobox.pack()

        self.order_var = tk.StringVar() #menyimpan nilai terpilih pada cmbbox
        self.order_combobox = ttk.Combobox(self.master, values=["Ascending", "Descending"], textvariable=self.order_var) #objek cmbbox
        self.order_combobox.pack()

        self.sort_button = tk.Button(self.master, text="Sort", command=self.sort_data)
        self.sort_button.pack(pady=10)

        self.search_label = tk.Label(self.master, text="Search by Name:")
        self.search_label.pack()

        self.search_var = tk.StringVar() #menyimpan nilai terpilih pada entry
        self.search_entry = tk.Entry(self.master, textvariable=self.search_var)
        self.search_entry.pack()

        self.search_button = tk.Button(self.master, text="Search", command=self.search_data)
        self.search_button.pack(pady=10)

    def update_list_box(self):
        self.tree.delete(*self.tree.get_children())  #menghapus semua baris dalam treeview
        for mahasiswa in self.data_mahasiswa: #melakukan iterasi pada setiap elemen dalam list self.data_mahasiswa
            self.tree.insert("", "end", values=(mahasiswa['nama'], mahasiswa['nilai']))  #menambah baris baru ke treeview

    def sort_data(self):
        criteria = self.sort_var.get().lower() 
        order = self.order_var.get().lower()
        #mengambil nilai dari cmbbox dan dikonversi ke huruf kecil

        reverse = False #inisialisasi reverse dengan false untuk asc
        if order == "descending": 
            reverse = True #true untuk desc

        if criteria == "nama":
            self.data_mahasiswa.sort(key=lambda x: x['nama'], reverse=reverse)
        elif criteria == "nilai":
            self.data_mahasiswa.sort(key=lambda x: x['nilai'], reverse=reverse)

        self.update_list_box() #memperbarui listbox setelah di sorting

    def search_data(self):
        search_name = self.search_var.get().capitalize() #mengambil nilai dari entry search dan ubah huruf pertama menjadi kapital
        found = False #inisialisasi found dengan false
        self.original_data_mahasiswa.sort(key=lambda x: x['nilai'], reverse=True) #mengurutkan data asli berdasarkan nilai secara descending
        #untuk mengetahui 10 nilai tertinggi

        for i, mahasiswa in enumerate(self.original_data_mahasiswa):  #melakukan iterasi pada data mahasiswa yang sudah diurutkan.
            if mahasiswa['nama'] == search_name:
                found = True  #jika nama ditemukan akan diinisialisasi menjadi true

                if i < 10 and mahasiswa['nilai'] >= 70:
                    messagebox.showinfo("Hasil Pencarian", f"SELAMAT! {search_name} Lolos Seleksi dengan Nilai {mahasiswa['nilai']}")
                else:
                    messagebox.showinfo("Hasil Pencarian", f"{search_name} Tidak Lolos Seleksi dengan Nilai {mahasiswa['nilai']} \nTETAP SEMANGAT DAN JANGAN MENYERAH")

        if not found:
            messagebox.showinfo("Hasil Pencarian", f"{search_name} tidak ditemukan.")

def main():
    root = tk.Tk()
    app = SeleksiUjianApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
