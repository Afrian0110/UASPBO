# UASPBO
# Kelompok 5
# Nama Anggota Kelompok
- Davi Sulaiman (G1A022001)
- Rafi Afrian Al Haritz (G1A022033)
- Fahim Ahmad Saputra (G1A022037)

# 2. Notepad menggunakan Tkinter dengan Python: Tkinter adalah paket GUI dari python. Kita dapat membuat notepad sederhana yang terdiri dari berbagai menu seperti cara menyimpan, membuka, dan mengedit file.
 # Jawaban :
- from tkinter import *# Mengimpor modul tkinter
from tkinter import filedialog # Mengimpor modul filedialog dari tkinter

root = Tk() # Membuat objek Tkinter
root.geometry("600x600") # Mengatur ukuran jendela menjadi 600x600 piksel
root.title("Notepad") # Mengatur judul jendela menjadi "Notepad"
root.config(bg='lightblue') # Mengatur latar belakang jendela menjadi "lightblue"
root.resizable(False,False) # Membuat jendela tidak dapat diubah ukurannya

- def save_file(): # Membuat fungsi save_file untuk menyimpan file
    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt') # Membuka dialog untuk menyimpan file
    if open_file is None:  # Jika file tidak dipilih
        return # Keluar dari fungsi save_file
    
    text=str(entry.get(1.0,END)) # Ambil teks dari widget entry
    open_file.write(text) # Tulis teks ke dalam file
    open_file.close()  # Menutup file
    
- def open_file(): # Membuat fungsi open_file untuk membuka file
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')]) # Buka dialog untuk membuka file
    if file is not None: # Jika file terbuka dengan sukses
        content=file.read()# Baca konten dari file
    entry.insert(INSERT,content)# Masukkan konten ke dalam widget entry

    
b1=Button(root,width='20',height='2',bg='#fff',text='save file',command=save_file).place(x=100,y=5) # tombol untuk menyimpan file
b1=Button(root,width='20',height='2',bg='#fff',text='open file',command=open_file).place(x=300,y=5) # tombol untuk membuka file

entry=Text(root,height='33',width='72',wrap=WORD) # Buat widget teks
entry.place(x=10,y=60) # Menempatkan widget teks di jendela

root.mainloop() # Memulai perulangan utama untuk menjalankan aplikasi

# Aplikasi Notepad yang dibuat menggunakan kode program di atas memiliki kegunaan dalam keseharian sebagai berikut:

- Menyimpan dan Membuka File Teks: Aplikasi ini memungkinkan pengguna untuk menyimpan dan membuka file teks. Dengan menggunakan tombol "save file", pengguna dapat menyimpan teks yang dimasukkan ke dalam aplikasi ke dalam file dengan format .txt. Sedangkan tombol "open file" memungkinkan pengguna untuk membuka file teks yang sudah ada dan menampilkan isinya di dalam aplikasi.

- Menulis dan Mengedit Catatan: Aplikasi ini berfungsi sebagai tempat untuk menulis dan mengedit catatan atau teks penting dalam kehidupan sehari-hari. Pengguna dapat menggunakan area input teks (widget entry) untuk menuliskan teks atau catatan, dan aplikasi ini menyediakan kemampuan untuk menyimpan dan membuka kembali teks yang telah ditulis sebelumnya.

- Pengaturan Antarmuka Grafis: Aplikasi ini menggunakan antarmuka grafis yang disediakan oleh modul tkinter. Antarmuka grafis memungkinkan pengguna untuk berinteraksi dengan aplikasi secara visual melalui tombol dan area teks yang disediakan. Ini memudahkan pengguna dalam penggunaan aplikasi tanpa perlu mengetik perintah atau kode secara manual.

- Dalam keseharian, aplikasi seperti Notepad dapat digunakan untuk mencatat ide, menyimpan catatan penting, menulis draft pesan atau email, dan melakukan berbagai tugas penulisan sederhana. Dengan adanya kemampuan untuk menyimpan dan membuka file teks, aplikasi ini juga dapat digunakan untuk menyimpan dan mengelola dokumen teks dalam format yang mudah diakses dan dibaca.
