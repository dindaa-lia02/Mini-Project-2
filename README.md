# Mini-project-2
Nama: Dinda Aulia Rizky    NIM: 2409116076

# ***Program Penyewaan Baju Adat***

# `A. Penjelasan baris kode`
1. Pada baris ini digunakan untuk membuat dan menampilkan tabel dengan format yang rapi dan struktur pada terminal, sehingga dapat dengan mudah untuk dibaca.

    ![Screenshot 2024-10-15 005714](https://github.com/user-attachments/assets/fae9b754-a3ac-4bdd-97cb-167812f74167)

2. Membuat dua variabel berupa list kosong.

   daftar_baju = [] Pada kode ini digunakan untuk menyimpan data mengenai baju, seperti kode baju, nama, masa sewa, harga sewa, status baju

   riwayat_sewa = [] Pada kode ini juga merupakan list kosong yang disiapkan untuk menyimpan riwayat penyewaan baju. Setiap kali ada transaksi penyewaan, seperti  nama penyewa, lama sewa, kode baju, nama baju bisa ditambahkan ke dalam      list ini.
   
   ![Screenshot 2024-10-15 005744](https://github.com/user-attachments/assets/d68929da-0c54-4501-a21d-9ef64902db68)

4. Menampilkan daftar baju

   Untuk menampilkan daftar baju dalam format tabel yang rapi menggunakan PrettyTable.
   table.clear_rows() digunakan untuk menghapus semua baris dari tabel sebelumnya agar tidak ada data lama yang tertinggal.

   table.field_names =[] digunakan untuk mengatur nama pada kolom table

   for baju in daftar_baju: menerapkan perulangan untuk mengambil setiap item baju melalui list daftar_baju

   print(table) digunakan untuk menampilkan table pada output di terminal

   ![Screenshot 2024-10-15 014730](https://github.com/user-attachments/assets/bc82ed1a-6888-42e9-8a37-abf834a5826e)

6. Digunakan untuk merapikan tampilan pada baris kode untuk memisahkan bagian judul dari kode lain

   ![Screenshot 2024-10-15 005759](https://github.com/user-attachments/assets/d7058e49-abdb-46f8-b9bd-f20034933676)

7. Menambahkan baju

   Mendefinisikan sebuah fungsi untuk menambahkan baju dengan empat parameter: Kode_baju, nama, masa_sewa, dan harga_sewa. Parameter ini akan berisi data terkait baju yang ditambahkan. Selain itu, pada fungsi ini juga membuat  sebuah dictionary baju yang berisi informasi tentang baju. Baris kode ini juga menggunakan append yang bertujuan untuk menambahkan dictionary baju ke dalam list daftar_baju.

   ![Screenshot 2024-10-15 013319](https://github.com/user-attachments/assets/e251d0f3-a633-4722-ba26-5b0c2700c6cc)

8. Mengupdate data baju

   Digunakan untuk memperbarui data baju yang ada di dalam daftar_baju dengan menerapkan 4 parameter dan perulangan. Baris ini juga akan menampilkan pesan bahwa data baju berhasil diperbarui, lalu fungsi berhenti dengan return. Jika 
   kode yang dimasukkan tidak ada yang cocok, maka akan menampilkan pesan bahwa baju dengan kode tersebut tidak ditemukan.

    ![Screenshot 2024-10-15 012211](https://github.com/user-attachments/assets/4148c996-f7ae-4bca-94ca-f3528c9654e4)

9. Menghapus baju

    Pada baris ini digunakan untuk mendefinisikan fungsi dengan parameter Kode_baju untuk menentukan baju mana yang akan dihapus dari daftar_baju berdasarkan kode baju.

   ![Screenshot 2024-10-15 015455](https://github.com/user-attachments/assets/f031fcfb-d7d9-47fb-936c-55d588012ccc)

10. Sewa baju

    Menyewa baju dari daftar baju berdasarkan kode baju dengan rincian lama sewa dan harga total. Jika lama sewa kurang atau sama dengan masa sewa yang ditentukan, harga sewa adalah harga normal.
Jika lama sewa melebihi masa sewa, ditambahkan biaya tambahan 10% dari harga normal untuk setiap hari tambahan.  Lalu, menambahkannya ke riwayat_sewa untuk menyimpan informasi tentang penyewa, baju yang disewa, lama sewa, dan harga total ke dalam list riwayat_sewa.

    ![Screenshot 2024-10-15 020016](https://github.com/user-attachments/assets/8e8be24a-7955-48cf-a66b-be8da5666a2b)

11. Mengembalikan baju

    Digunakan untuk mengembalikan baju yang telah disewa, lalu ditandai kembali sebagai tersedia.

    baju["tersedia"] = True: Mengubah status baju menjadi tersedia, artinya baju sudah dikembalikan.

    ![Screenshot 2024-10-15 020312](https://github.com/user-attachments/assets/a5f04b46-9c32-4495-9839-07735ec71bc9)

12. Menampilkan riwayat sewa

    Fungsi ini digunakan untuk menampilkan semua riwayat penyewaan baju yang disimpan dalam list riwayat_sewa yang akan muncul dalam format table.

    ![Screenshot 2024-10-15 021026](https://github.com/user-attachments/assets/8e50d5ce-f148-4a1e-9efb-f8785ce63376)

13. Menu admin

    Fungsi ini akan menampilkan semua menu untuk admin yang dimana memungkinkan admin untuk mengelola daftar baju dari penyewaan baju hingga pengembalian baju dengan konsep CRUD (Create, Read, Update, Delete).

    pada fungsi ini menggunakan looping while true untuk memulai loop tak terbatas yang akan terus berjalan hingga admin memilih untuk keluar. Pada fungsi ini juga menerapkan percabangan.
    
    ![Screenshot 2024-10-15 021433](https://github.com/user-attachments/assets/d846417e-8607-439d-b536-c73c2b79566f)

14. Menu Customer

    Fungsi ini menampilkan semua menu untuk customer berinteraksi dengan sistem yang memungkinkan mereka jika ingin menyewa baju dan mengembalikan baju. Pada fungsi ini menerapkan looping dan juga percabangan. 
    
    ![Screenshot 2024-10-15 022024](https://github.com/user-attachments/assets/71220dff-b77a-4586-a5fa-180a77a28e5e)

15. Menu login

    users: merupakan sebuah dictionary yang berfungsi menyimpan informasi pengguna dengan username sebagai kunci

    def login(): mendefinisikan fungsi login yang bertujuan untuk mengautentikasi pengguna.

    while True:: Memulai loop tak terbatas sehingga terus meminta input pengguna sampai login berhasil.

    username = input("Masukkan username: "): meminta pengguna untuk memasukkan username.

    password = input("Masukkan password: "): meminta pengguna untuk memasukkan password.

    if username in users and users[username]["password"] == password:: untuk mengecek apakah username     
    terdapat dalam users dan apakah password yang dimasukkan sudah sesuai.
    Jika benar akan menampilkan pesan bahwa login berhasil dan menyebutkan role pengguna.
    mengembalikan role pengguna (return users[username]["role"]). Dan apabila jika salah, maka akan 
    menampilkan pesan bahwa username atau password salah dan meminta pengguna untuk mencoba lagi.

    ![Screenshot 2024-10-15 024302](https://github.com/user-attachments/assets/bdb05b0f-d077-4ac6-87f5-04186c3adbb1)

    
17. Fungsi utama

    Fungsi main merupakan fungsi utama dalam program yang akan menyusun alur kerja program saat mengeksekusi sistem penyewaan baju adat yang dimulai dari menambahkan data baju, menyediakan sistem bagi admin atau customer, dan mengelola interaksi dengan sistem, hingga user memilih untuk keluar.

    if __name__ == "__main__":: fungsinya untuk memastikan bahwa fungsi main() hanya dijalankan ketika file ini dieksekusi sebagai program utama.

    ![Screenshot 2024-10-15 024225](https://github.com/user-attachments/assets/f7952f3e-9fd2-4eb9-a64c-ca6e458f4134)

   
# `B.Penjelasan Output`

# Menu Customer

1. Pada awal program akan menampilkan menu awal seperti pada gambar diatas, kita diminta menginput angka yang kita pilih.

   ![Screenshot 2024-10-15 024718](https://github.com/user-attachments/assets/35d4a3db-fd56-4f21-89d3-1dcccd3985ba)

2. Kemudian kita akan diminta untuk menginput username dan password sebagai customer
   
    ![Screenshot 2024-10-15 024735](https://github.com/user-attachments/assets/b27e9725-b815-473d-9ef8-b8b73ab821ab)

3. Login berhasil sebagai customer, maka akan muncul semua menu untuk customer dan customer akan diminta untuk menginput pilihan. 

   Pilihan 1 memiliki fungsi untuk menampilkan daftar baju yang disewakan

   Pilihan 2 memiliki fungsi agar customer bisa melakukan transaksi untuk menyewa baju yang tersedia pada daftar baju

   Pilihan 3 memiliki fungsi untuk mengembalikan baju yang telah disewa oleh customer

   pilihan 4 memiliki fungsi untuk kembali ke menu utama untuk memilih role atau keluar dari program

    ![Screenshot 2024-10-15 024745](https://github.com/user-attachments/assets/dd15632a-9e06-469d-92f4-03b4db457d70)

4.  Apabila customer memilih 1, maka program akan menampilkan daftar baju yang tersedia
    
    ![Screenshot 2024-10-15 030237](https://github.com/user-attachments/assets/2368b981-151b-4642-b5ac-48df545785e8)

5. Apabila customer memilih 2, maka akan melakukan transaksi dalam penyewaan baju adat. Customer akan diminta untuk memasukkan kode baju yang ingin disewa, nama penyewa, dan lama sewa. setelah itu, baju berhasil untuk disewa dengan 
   total harga sewa yang tertera pada terminal. 
   
   ![Screenshot 2024-10-15 030431](https://github.com/user-attachments/assets/555dccab-fbc5-4d7e-b7f2-b69ee9c30983)

   Sehingga status data baju akan berubah menjadi "Disewa" seperti pada gambar dibawah ini:
   
   ![Screenshot 2024-10-15 035946](https://github.com/user-attachments/assets/c09ee753-67b5-40b0-9159-cc120923b868)

6. Apabila memilih 3, maka baju yang disewa oleh customer akan dikembalikan kepada admin 

   ![Screenshot 2024-10-15 035141](https://github.com/user-attachments/assets/aa85cfb0-fcb4-4f58-802b-e3949ea49af4)

   dan status baju untuk kode tersebut akan kembali "Tersedia" seperti pada gambar dibawah ini:
   
   ![Screenshot 2024-10-15 040004](https://github.com/user-attachments/assets/396dbada-d2f0-4b75-a7f8-78bf6920de0f)

7. Jika memilih 4, maka akan kembali ke menu utama untuk memilih role atau keluar dari program
   
   ![Screenshot 2024-10-15 030723](https://github.com/user-attachments/assets/135a7c28-ae5d-4df6-acea-969364005de2)



# Menu Admin

1. Pada awal program akan menampilkan menu awal seperti pada gambar diatas, kita diminta menginput angka yang kita pilih.

   ![Screenshot 2024-10-15 030932](https://github.com/user-attachments/assets/6d8cd2d1-8d12-403e-9295-ec7e602f48ec)
 
3. Kemudian kita akan diminta untuk menginput username dan password sebagai admin

   ![Screenshot 2024-10-15 032123](https://github.com/user-attachments/assets/679d5537-8cbf-40c5-81ee-a1d253c1e231)

3. Login berhasil sebagai admin, maka akan muncul semua menu untuk admin dan admin akan diminta untuk menginput pilihan. 

   Pilihan 1 memiliki fungsi untuk menampilkan daftar baju yang disewakan

   Pilihan 2 memiliki fungsi agar admin dapat menambahkan kode baju baru dengan detail yang diberikan ke dalam table

   Pilihan 3 memiliki fungsi untuk untuk memperbarui atau mengupdate salah satu data baju yang ada di dalam table

   pilihan 4 memiliki fungsi untuk menghapus salah satu data baju yang terdapat di dalam table

   pilihan 5 memiliki fungsi untuk melihat riwayat sewa yang dilakukan oleh customer

   pilihan 6 memiliki fungsi untuk kembali ke menu utama untuk memilih role atau keluar dari program

   ![Screenshot 2024-10-15 030951](https://github.com/user-attachments/assets/343e83cf-5437-4a7b-be9b-d7b3ebf593eb)
    
5. Apabila admin memilih 1, maka program akan menampilkan daftar baju yang tersedia

   ![Screenshot 2024-10-15 042608](https://github.com/user-attachments/assets/6d9ff3a9-79b0-4105-8aa8-4a27bb383fbf)

6. Apabila admin memilih 2, maka akan menambahkan data baju baru yang akan ditampilkan pada table dengan cara memasukkan nama baju, masa sewa, dan harga sewa. Maka, data untuk baju baru berhasil ditambahkan pada table

   ![Screenshot 2024-10-15 033050](https://github.com/user-attachments/assets/ff23b86c-59b4-43dc-8b58-aa87393c2379)

   dan akan terlihat seperti ini pada table

   ![Screenshot 2024-10-15 042356](https://github.com/user-attachments/assets/c616a608-afd1-4828-983f-6b29630faf32)


7. Apabila memilih 3, maka akan mengupdate data baju yang ada di dalam table. Disini akan mengubah dari kode baju, nama baru, masa sewa, dan harga baju. Lalu, data baju akan berhasil diupdate

   ![Screenshot 2024-10-15 034351](https://github.com/user-attachments/assets/d26eb141-a1c0-4dcc-a44d-ed52c1932671)

   dan akan terlihat seperti ini pada table

   ![Screenshot 2024-10-15 042514](https://github.com/user-attachments/assets/b3cbec2c-b0a8-4030-89e2-98b328a1b799)


8. Apabila memilih 4, maka akan menghapus salah satu data baju yang ada di dalam table dengan cara menmasukkan kode baju yang ingin dihapus.

   ![Screenshot 2024-10-15 034700](https://github.com/user-attachments/assets/b3270ee6-f507-487f-abac-beaafb009d62)

   dan akan terlihat seperti ini pada table

   ![Screenshot 2024-10-15 042608](https://github.com/user-attachments/assets/6e27c53a-f5c0-4de6-9d1b-d46b1e48735b)


9. Apabila memilih 5, maka akan menampilkan riwayat baju yang sudah disewa oleh customer

   ![Screenshot 2024-10-15 034726](https://github.com/user-attachments/assets/19f24447-e6ed-4046-97f5-65275d94bbaa)

10. apabila memilih 6, maka akan kembali ke menu utama untuk memilih role atau keluar dari program

    ![Screenshot 2024-10-15 035101](https://github.com/user-attachments/assets/89455c2c-672e-4c66-a358-4ec37a7e8325)






# `C. Flowchart`

![Flowchart MINPRO 2 UPDATE drawio (1)](https://github.com/user-attachments/assets/c2d13af7-3d4e-4cca-a6aa-c01306c84e52)
