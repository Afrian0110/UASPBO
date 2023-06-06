from tkinter import *# Mengimpor modul tkinter
from tkinter import filedialog # Mengimpor modul filedialog dari tkinter

root = Tk() # Membuat objek Tkinter
root.geometry("600x600") # Mengatur ukuran jendela menjadi 600x600 piksel
root.title("Notepad") # Mengatur judul jendela menjadi "Notepad"
root.config(bg='lightblue') # Mengatur latar belakang jendela menjadi "lightblue"
root.resizable(False,False) # Membuat jendela tidak dapat diubah ukurannya

def save_file(): # Membuat fungsi save_file untuk menyimpan file
    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt') # Membuka dialog untuk menyimpan file
    if open_file is None:  # Jika file tidak dipilih
        return # Keluar dari fungsi save_file
    
    text=str(entry.get(1.0,END)) # Ambil teks dari widget entry
    open_file.write(text) # Tulis teks ke dalam file
    open_file.close()  # Menutup file
    
def open_file(): # Membuat fungsi open_file untuk membuka file
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')]) # Buka dialog untuk membuka file
    if file is not None: # Jika file terbuka dengan sukses
        content=file.read()# Baca konten dari file
    entry.insert(INSERT,content)# Masukkan konten ke dalam widget entry

# tombol untuk menyimpan file     
b1=Button(root,width='20',height='2',bg='#fff',text='save file',command=save_file).place(x=100,y=5)
# tombol untuk membuka file
b1=Button(root,width='20',height='2',bg='#fff',text='open file',command=open_file).place(x=300,y=5)

# Buat widget teks
entry=Text(root,height='33',width='72',wrap=WORD)
# Menempatkan widget teks di jendela
entry.place(x=10,y=60) 

# Memulai perulangan utama untuk menjalankan aplikasi
root.mainloop()
