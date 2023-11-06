import json
from prettytable import PrettyTable
import pwinput
import time
import os
os.system ("cls")

ROOD_DIR = os.path.abspath(os.curdir)

print('''
+=======shopcoolz=================================================================================================+
|                                          +        SHOPCOOLZ         +                                           |
+-----------------------------------------------------------------------------------------------------------------+
|                                 SELAMAT DATANG DI TOKO ONLINE NO.1 DI INDONESIA!                                |
+=================================================================================================shopcoolz=======+
''')

# JSON untuk login
json_path = f"{ROOD_DIR}/regist.json"
def load_data_user():
    with open(json_path, "r") as data_user:
        login_data = json.loads(data_user.read())
    return login_data
        
def save_data_user(login_data):
    with open(json_path, "w") as data_user:
        data_user.write(json.dumps(login_data, indent=4))
        
# JSON untuk produk
json_produk = f"{ROOD_DIR}/produks.json"
def load_data():
    with open(json_produk, "r") as file:
        data = json.load(file)
    return data
        
def save_data(data):
    with open(json_produk, "w") as file:
        json.dump(data, file, indent=4)




'''============================================================================================================='''

'''                                            REGIST DAN LOGIN                                                 '''

'''============================================================================================================='''



# Data admin yang tersimpan
data_admin = {
    'athira': 'asahiganteng',
    'anni': 'abcde',
    'naura': 'lopbangcan'
}


# Fungsi Login admin
def admin_login():
    os.system("cls")
    
    print("+============================================ LOGIN ADMIN ===========================================+")
    print("|                                     Pastikan anda adalah admin                                     |")
    print("+====================================================================================================+")
    
    sisa_coba= 3
    while sisa_coba > 0:
        username = input("Masukkan username anda: ")
        password = pwinput.pwinput("Masukkan password anda: ")
        try:
            if username in data_admin and data_admin[username] == password:
                print("\n     ----Login Berhasil----        ")
                print(f"     Selamat datang!, {username}\n  ")
                
                admin()
                break
            elif username in data_admin and data_admin[username] != password or not username in data_admin:
                sisa_coba -= 1
                print("+=====================================================================+")
                print("| Login gagal. Username atau password anda salah, silahkan coba lagi! |")
                print(f"|                         Sisa percobaan: {sisa_coba}                           |")
                print("+=====================================================================+\n")
                if sisa_coba == 0:
                    print("\n+====================================================+")
                    print("|  Akun anda terkunci. Mohon tunggu untuk coba lagi  |")
                    print("+====================================================+")
                    for x in range (3, 0, -1):
                        time.sleep(1)
                        print(x)
                    sisa_coba = 3
                    start()
                    break
                    
        except (ValueError, KeyboardInterrupt):
            print("\n+===========================================================+")
            print("| Mohon masukkan data yang valid dan jangan tekan ctrl + C! |")
            print("+===========================================================+\n")




'''=============================================================================================================='''
'''                                             PILIHAN CUSTOMER (USER)                                          '''
'''=============================================================================================================='''



def user():
    os.system("cls")
    print("+=====================================+")
    print("|           SIGN IN / LOGIN           |")
    print("+-------------------------------------+")
    print("|   1. Register                       |")
    print("|   2. Login                          |")
    print("|   3. Back                           |")
    print("+-------------------------------------+")
    
    while True:
        try:
            pilih = str(input('Masukkan pilihan yang anda inginkan: '))
            if pilih == "1":
                user_regist()
                break
            elif pilih == "2":
                user_login()
                break
            elif pilih == "3":
                start()
            else: 
                print("+=====================================+")
                print("|  Tolong masukka angka 1, 2, atau 3  |")
                print("+=====================================+\n")
            pass
        except (ValueError, KeyboardInterrupt ):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}") 




'''=============================================================================================================='''
'''                                           REGISTER CUSTOMER(USER)                                            '''
'''=============================================================================================================='''



# Fungsi untuk user melakukan register
def user_regist ():
    os.system("cls")
    login_data = load_data_user()
    
    print("+======================================= SILAHKAN REGISTER ==========================================+")
    print("|                      Username maksimal 10 karakter dan Password 8 karakter                         |")
    print("+====================================================================================================+")
    
    # Looping untuk username dan password customer
    while True:
        try:
            # Untuk mengecek limit karakter
            username = input("Masukkan Username yang diinginkan: ")
            if not username.isalnum() or len(username) > 10:
                print("+===============================================================+")
                print("| Username tidak valid. Harus terdiri dari huruf dan angka saja |")
                print("|            dan tidak boleh lebih dari 10 karakter.            |")
                print("+===============================================================+\n")
                continue
            
            # Untuk mengecek apakah username sudah ada
            elif any(user["Nama User"] == username for user in login_data):
                print("+============================================+")
                print("| Username sudah ada. Tolong pilih yang lain |")
                print("+============================================+\n")
                continue
            
            password = pwinput.pwinput("Masukkan password yang diinginkan: ")
            if not password.isalnum() or len(password) > 8:
                print("+===============================================================+")
                print("| Password tidak valid. Harus terdiri dari huruf dan angka saja |")
                print("|            dan tidak boleh lebih dari 8 karakter.             |")
                print("+===============================================================+\n")
            else:
                # Untuk menambahkan data user ke variabel yang ada           
                akun = {
                    "Nama User": username,
                    "Pw User": password,
                    "Saldo": 0
                    }
                    
                login_data.append(akun)
                save_data_user(login_data)  
                print("\n+=======================================================+")
                print("|          ----Anda berhasil Registrasi----             |")
                print("|   Selamat bergabung menjadi cooler bersama kami!! :)  |")
                print("+=======================================================+\n")
                user_login()
                break
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")




'''=============================================================================================================='''
'''                                           LOGIN CUSTOMER(USER)                                               '''
'''=============================================================================================================='''



# Fungsi untuk user melakukan login
def user_login():
    global username
    login_data = load_data_user()
    print("+========================================== SILAHKAN LOGIN ==========================================+")
    print("|                            Pastikan akun anda telah terdaftar sebelumnya                           |")
    print("+====================================================================================================+")
    
    # Untuk mengecek kevalidan username dan password
    sisa_coba = 3
    is_logged_in = False
    while sisa_coba > 0 and not is_logged_in:
        try:
            username = input("Masukkan Username Anda: ")
            password = pwinput.pwinput("Masukkan Password Anda:")
            
            akun_tersedia = False
            # Untuk mengecek apakah ada username yang sama
            for user in login_data:
                if user["Nama User"] == username:
                    akun_tersedia = True
                    # Untuk mengecek apakah pw nya sesuai
                    if password == user["Pw User"]:
                        print("\n     ----Login Berhasil----      ")
                        print(f"     Selamat datang!, {username}\n")
                        is_logged_in = True  # Atur status login menjadi True
                        break
                    else:
                        sisa_coba -= 1
                        print("+==================================================+")
                        print(f"  Login gagal. Kata sandi salah. Sisa percobaan: {sisa_coba}")
                        print("+==================================================+\n")
                        continue
                # Jika username tidak ditemukan       
            if not akun_tersedia:
                    sisa_coba -= 1
                    print("+==================================================+")
                    print("       Login gagal. Pengguna tidak ditemukan.       ")
                    print(f"       Silahkan coba lagi! Sisa percobaan: {sisa_coba}")
                    print("+==================================================+\n")
                    continue
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}")
                        
    if sisa_coba == 0:
        print("\n+====================================================+")
        print("|  Akun anda terkunci. Mohon tunggu untuk coba lagi  |")
        print("+====================================================+")
        for x in range(3, 0, -1):
            time.sleep(3)
            print(x)
        sisa_coba = 3 # Reset percobaan
        start()
        
    if is_logged_in:
        customer()




'''=============================================================================================================='''
'''                                                                                                              '''
'''                                            MENU ADMIN (C R U D)                                              '''
'''                                                                                                              '''
'''=============================================================================================================='''



# Main program
def admin():
    while True:
        print("\n")
        print("+----------------------------------+")
        print("|            MENU ADMIN            |")
        print("+----------------------------------+")
        print("| 1. Tampilkan Produk              |")
        print("| 2. Tambah Produk                 |")
        print("| 3. Update Produk                 |")
        print("| 4. Hapus Produk                  |")
        print("| 5. Cari Produk                   |")
        print("| 6. Keluar                        |")
        print("+----------------------------------+")
        
        try:
            pilih = input("Pilih opsi (1/2/3/4/5/6): ")
            if pilih == "1":
                display_products()
            elif pilih == "2":
                create()
            elif pilih == "3":
                update()
            elif pilih == "4":
                delete()
            elif pilih == "5":
                search()
            elif pilih == "6":
                print("\n+=========================================================+")
                print("|             Anda telah keluar dari akun admin.          |")
                print("|  Silahkan login kembali jika ingin mengedit menu admin  |")
                print("+=========================================================+")
                break
            else:
                print("+=========================================================+")
                print("| Opsi tidak valid. Pilih opsi yang sesuai (1/2/3/4/5/6). |")
                print("+=========================================================+\n")
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}")




'''=============================================================================================================='''
'''                                           READ (Menampilkan Produk)                                          '''
'''=============================================================================================================='''



# Fungsi untuk menampilkan produk
def display_products():
    data = load_data()
    for kategori in data["Kategori"]:
        print(f"\nKategori: {kategori['Nama Kategori']}")
        
        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Harga", "Stok"]
        table.title = "Shopcoolz"
        
        for produk in kategori["produk"]:
            table.add_row([produk["ID"], produk["Nama Produk"], produk["Harga"], produk["Stok"]])
        
        print(table)




'''=============================================================================================================='''
'''                                          CREATE (Menambahkan Produk)                                         '''
'''=============================================================================================================='''



# Menambah produk baru
def create():
    while True:
        # Untuk memuat data dari file produks.json
        data = load_data()
        print("+=========================================+")
        print("|              Tambah Produk              |")
        print("+=========================================+")
        nama_kategori = str(input("Masukkan Kategori: "))  
        
        for kategori in data["Kategori"]:
            # Apabila nama kategori ada di dalam data kategori
            if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                try:
                    # Menginputkan data baru
                    nama_produk = input("Masukkan Nama Produk Baru: ")
                    harga = input("Masukkan Harga Produk: ")
                    stok = input("Masukkan Stok Produk: ")
                    
                    # Memeriksa apakah karakter produk sesuai
                    if not (2 <= len(nama_produk) <= 50 ):
                        print("+===========================================+")
                        print("| Minimal karakter produk 2 dan maksimal 50 |")
                        print("+===========================================+\n")
                        continue
                    elif not (nama_produk.strip() and harga.isdigit() and stok.isdigit()):
                        print("+======================================================+")
                        print("| Data tidak valid. Pastikan nama produk tidak kosong. |")
                        print("+======================================================+\n")
                        continue
                    elif not (100000000 >= int(harga) >= 100 and 10000 >= int(stok) > 0):
                        print("+======================================================+")
                        print("|   Harga minimal Rp 100 dan maksimal Rp 100.000.000   |")
                        print("|         dan stok minimal 1 & maksimal 10.000.        |")
                        print("+======================================================+\n")
                        continue
                        
                    # Untuk menyimpan produk baru
                    new_product = {
                    "ID": int(len(kategori["produk"])) + 1,
                    "Nama Produk": str(nama_produk),
                    "Harga": int(harga),
                    "Stok": int(stok)
                    }
                    
                    # Untuk menambahkan produk ke dalam data produk
                    kategori["produk"].append(new_product)
                    save_data(data)
                    print("\n---Produk baru telah ditambahkan.---\n")
                    
                except (ValueError, KeyboardInterrupt):
                    print("\n+=============================================================+")
                    print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
                    print("+=============================================================+\n")
                except Exception as a:
                    print(f"Error, {a}")
                else:
                    break
        
        # Apabila tidak termasuk di daftar kategori
        if not (kategori["Nama Kategori"].lower() == nama_kategori.lower()):
            print("----Kategori tidak ditemukan.----")
            return
        break




'''=============================================================================================================='''
'''                                        UPDATE (Mengubah Data Produk)                                         '''
'''=============================================================================================================='''



# Mengupdate produk
def update():
    try:
        data = load_data()
        print("+=========================================+")
        print("|              Update Produk              |")
        print("+=========================================+")
        nama_kategori = str(input("Masukkan Kategori: "))
        id_produk = int(input("Masukkan ID Produk yang akan diupdate: "))
        
        for kategori in data["Kategori"]:
            if kategori["Nama Kategori"].lower() == nama_kategori:
                for produk in kategori["produk"]:
                    if produk["ID"] == id_produk:
                    
                        while True:
                            nama_produk_baru = input("Masukkan Nama Produk Baru: ")
                            harga_baru = input("Masukkan Harga Produk Baru: ")
                            stok_baru = input("Masukkan Stok Produk Baru: ")
                            
                            if not (2 <= len(nama_produk_baru) <= 50 ):
                                print("+===========================================+")
                                print("| Minimal karakter produk 2 dan maksimal 50 |")
                                print("+===========================================+\n")
                                continue
                            elif not (nama_produk_baru.strip() and harga_baru.isdigit() and stok_baru.isdigit()):
                                print("+======================================================+")
                                print("| Data tidak valid. Pastikan nama produk tidak kosong. |")
                                print("+======================================================+\n")
                                continue
                            elif not (100000000 >= int(harga_baru) >= 100 and 10000 >= int(stok_baru) > 0):
                                print("+======================================================+")
                                print("|   Harga minimal Rp 100 dan maksimal Rp 100.000.000   |")
                                print("|         dan stok minimal 1 & maksimal 10.000.        |")
                                print("+======================================================+\n")
                                continue
                            
                            # Untuk memperbarui produk
                            produk["Nama Produk"] = str(nama_produk_baru)
                            produk["Harga"] = int(harga_baru)
                            produk["Stok"] = int(stok_baru)
                            save_data(data)
                            print("\n---Produk telah diupdate.---\n")
                            return
                else:
                    print('----ID tidak ditemukan----') 
                                
        if not any(kategori["produk"]):
            print("----Kategori tidak ditemukan----.")
    except (ValueError,KeyboardInterrupt):
        print("\n+=============================================================+")
        print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
        print("+=============================================================+\n")
    except Exception as a:
            print(f"Error, {a}")




'''=============================================================================================================='''
'''                                           DELETE (Menghapus Produk)                                          '''
'''=============================================================================================================='''



# Menghapus produk
def delete():
    data = load_data()
    print("+=========================================+")
    print("|              Hapus Produk               |")
    print("+=========================================+")
    while True:
        try:
            nama_kategori = input("Masukkan Kategori: ")
            id_produk = input("Masukkan ID Produk yang akan dihapus: ")
            if not nama_kategori.isalnum():
                print('Jangan pakai spasi atau karakter aneh apapun.')
                continue
            elif not id_produk.isdigit():
                print("+========================================================================+")
                print("| Mohon masukkan angka dan jangan pakai spasi atau karakter aneh apapun. |")
                print("+========================================================================+")
                continue
            # Untuk menghapus produk
            for kategori in data["Kategori"]:
                if kategori["Nama Kategori"].lower() == nama_kategori.lower():
                    for produk in kategori["produk"]:
                        if produk["ID"] == int(id_produk):
                            kategori["produk"].remove(produk)
                            save_data(data)
                            print("\n----Produk telah dihapus.----\n")
                            return
                    print("----Produk tidak ditemukan----.")
                    return
            
            print("----Kategori tidak ditemukan----.")
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}")




'''=============================================================================================================='''
'''                                            SEARCH (Mencari Produk)                                           '''
'''=============================================================================================================='''



def search():
    data = load_data()
    cari_produk = input("Masukkan Nama Produk yang akan dicari: ")
    hasil_pencarian = []
    
    for kategori in data["Kategori"]:
        for produk in kategori["produk"]:
            if cari_produk.lower() in produk["Nama Produk"].lower():
                hasil_pencarian.append(produk)
                
    if hasil_pencarian:
        print("Hasil Pencarian:")
        for kategori in data["Kategori"]:
            print(f"\nKategori: {kategori['Nama Kategori']}")
                
            table = PrettyTable()
            table.field_names = ["ID", "Nama Produk", "Harga", "Stok"]
            table.title = "Shopcoolz"
                
            for produk in kategori["produk"]:
                if produk in hasil_pencarian:
                    table.add_row([produk["ID"], produk["Nama Produk"], produk["Harga"], produk["Stok"]])
                    
            print(table)
    else:
        print("----Produk tidak ditemukan----.")
        
    return hasil_pencarian




'''=============================================================================================================='''
'''                                                                                                              '''
'''                                                 MENU CUSTOMER                                                '''
'''                                                                                                              '''
'''=============================================================================================================='''



# Fungsi untuk menu customer
def customer():
    while True:  
            print("\n")
            print("+-----------------------------------+")
            print("|           Menu Customer           |")
            print("+-----------------------------------+")
            print("|     1. Tampilkan Produk           |")
            print("|     2. Transaksi Pembelian        |")
            print("|     3. Lihat Saldo E-Money        |")
            print("|     4. Top Up Saldo E-Money       |")
            print("|     5. Cari                       |")
            print("|     6. Sorting Harga              |")
            print("|     7. Sorting ID                 |")
            print("|     8. Keluar                     |")
            print("+-----------------------------------+")
            
            try:
                pilih_cust = input("Masukkan menu yang anda inginkan (1/2/3/4/5/6/7/8): ")
                if pilih_cust == "1":
                    display_products()
                elif pilih_cust == "2":
                    transaksi()
                    break
                elif pilih_cust == "3":
                    lihat_saldo()
                    break
                elif pilih_cust == "4":
                    top_up()
                    break
                elif pilih_cust == "5":
                    search()
                elif pilih_cust == "6":
                    sort_products()
                elif pilih_cust == "7":
                    sort_id()
                elif pilih_cust == "8":
                    exit()
                    break
                else: 
                    print("+=====================================+")
                    print("| Tolong masukkan angka 1/2/3/4/5/6/7 |")
                    print("+=====================================+\n")
            except (ValueError, KeyboardInterrupt):
                print("\n+=============================================================+")
                print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
                print("+=============================================================+\n")
            except Exception as a:
                print(f"Error, {a}")




'''=============================================================================================================='''
'''                                              Transaksi Pembelian                                             '''
'''=============================================================================================================='''



# Fungsi untuk transaksi
def transaksi():
    # Untuk memuat data di file produks.json
    data = load_data()
    struk = {"Produk Dibeli": [], "Total Harga": 0}
    
    
    while True:
        print("\n------------------Diskon 10% minimal belanja Rp. 500.000--------------------\n")
        print("Kategori yang Tersedia:")
        # Menampilkan Nama Kategori dari data Kategori
        print("+=========================+")
        print("|         Kategori        |")
        print("+=========================+")
        for kategori in data["Kategori"]:
            print(kategori["Nama Kategori"])
        print("+=========================+\n")
        
        kategori_terpilih = input("Masukkan kategori yang ingin Anda telusuri atau 'selesai' untuk menyelesaikan transaksi: ")
        
        if kategori_terpilih.lower() == "selesai":
            break
            
        # Jika Nama Kategori yang dipilih ada di dalam Kategori maka akan menampilkan produk dalam bentuk prettyTable
        for kategori in data["Kategori"]:
            if kategori["Nama Kategori"].lower() == kategori_terpilih.lower():
                print(f"Produk dalam kategori {kategori_terpilih}:")
                produk_table = PrettyTable()
                produk_table.field_names = ["ID", "Nama Produk", "Harga", "Stok"]
                for produk in kategori["produk"]:
                    produk_table.add_row([produk['ID'], produk['Nama Produk'], produk['Harga'], produk['Stok']])
                print(produk_table)
                
                # Menginputkan ID dan Jumlahh produk yang  di beli
                id_produk_terpilih = int(input("Masukkan ID produk yang ingin Anda beli: "))
                jumlah = int(input("Masukkan jumlah yang ingin Anda beli: "))
                
                for produk in kategori["produk"]:
                    if produk["ID"] == id_produk_terpilih:
                        if int(produk["Stok"]) >= jumlah:
                            # Menghitung Subtotal per-item
                            Subtotal_harga = produk["Harga"] * jumlah
                            produk["Stok"] = str(int(produk["Stok"]) - jumlah)
                            struk["Produk Dibeli"].append({
                                "Produk": produk['Nama Produk'],
                                "Harga": produk['Harga'],
                                "Jumlah": jumlah,
                                "Subtotal Harga": Subtotal_harga
                            })
                            print(f"{jumlah} {produk['Nama Produk']} ditambahkan ke struk.")
                            struk["Total Harga"] += int(Subtotal_harga)
                        else:
                            print("+=================================================+")
                            print("| Stok tidak mencukupi untuk produk yang dipilih. |")
                            print("+=================================================+\n")
                        break
                else:
                    print("+==================================================+")
                    print("| Produk dengan ID yang diberikan tidak ditemukan. |")
                    print("+==================================================+\n")
                break
        else:
            print("----Kategori tidak ditemukan.----")
            
    cetak_struk(struk, username)
    save_data(data)
            
    while True:
        try:
            kembali = input("Apakah Anda ingin kembali ke menu customer? (y/t): ")
            if kembali.lower() == "y":
                customer()
                break
            elif kembali.lower() == "t":
                exit()
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan 'y' atau 't'.")
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}")




'''=============================================================================================================='''
'''                                                Mencetak STRUK                                                '''
'''=============================================================================================================='''



# Fungsi untuk struk
def cetak_struk(struk, username):
    login_data = load_data_user()
    print("\n+====================================================+")
    print("| Masukkan password anda untuk melanjutkan transaksi |" )
    print("+====================================================+")
    print(f"Username: {username}")
    
    while True:
        password = pwinput.pwinput("Password: ")
        akun_ada = False
        
        # Mengecek apakah akun ada dan password benar
        for user in login_data:
            if user["Nama User"].lower() == username.lower():
                if user["Pw User"] == password:
                    akun_ada = True
                    print("\n  ----Pembayaran berhasil. Silahkan cek struk anda----  \n")
                    with open("struk_belanja.txt", "a") as s:
                        print("\n=====================================================", file=s)
                        print("                   Struk Belanja", file=s)
                        print("=====================================================", file=s)
                        print(f"{'Produk':<15} {'Harga':<10} {'Jumlah':<10} {'Subtotal Harga':<15}", file=s)
                        print("-----------------------------------------------------", file=s)
                        for pembelian in struk["Produk Dibeli"]:
                            produk = pembelian['Produk']
                            harga = pembelian['Harga']
                            jumlah = pembelian['Jumlah']
                            subtotal = pembelian['Subtotal Harga']
                            print(f"{produk:<15} {harga:<10} {jumlah:<10} {subtotal:<15}", file=s)
                            
                        print("-----------------------------------------------------" , file=s)
                        total_harga_sebelum_diskon = sum(float(item['Subtotal Harga']) for item in struk["Produk Dibeli"])
                        print(f"Total Harga Sebelum Diskon: Rp. {int(total_harga_sebelum_diskon):>5}", file=s)
                            
                        minimal_belanja = 500000
                        total_harga = struk["Total Harga"]
                        
                        # Menghitung diskon jika syarat terpenuhi
                        if total_harga >= minimal_belanja:
                            diskon = total_harga_sebelum_diskon * 0.1
                            total_harga_setelah_diskon = int(total_harga_sebelum_diskon - diskon)
                            print("=====================================================", file=s)
                            print(f"Diskon (10%): -Rp. {diskon:.2f}", file=s)
                            print(f"Total Harga Setelah Diskon: Rp. {total_harga_setelah_diskon:.2f}", file=s)
                        else:
                            total_harga_setelah_diskon = total_harga
                            print("=====================================================", file=s)
                            print(f"Total Harga: Rp. {total_harga_setelah_diskon:>5}", file=s)
                            
                        # Mengecek saldo user
                        saldo_sekarang = user['Saldo']
                        if saldo_sekarang < total_harga_setelah_diskon:
                            print(f"Saldo Anda tidak mencukupi untuk transaksi ini (Saldo: Rp. {saldo_sekarang}).")
                            print("Transaksi dibatalkan.")
                            print("Silahkan lakukan top up sebelum transaksi ulang")
                            customer()
                        else :
                            user['Saldo'] -= total_harga_setelah_diskon
                            save_data_user(login_data)
                            break
        if akun_ada:
            break
        else:
            print("+==================================================================+")
            print("|  Akun tidak ditemukan atau kata sandi salah. Silakan coba lagi.  |")
            print("+==================================================================+\n")
            break




'''=============================================================================================================='''
'''                                                  Lihat Saldo                                                 '''
'''=============================================================================================================='''



# Fungsi untuk lihat saldo
def lihat_saldo():
    login_data = load_data_user()
    print("\n+====================================================+")
    print("| Masukkan password anda untuk melanjutkan transaksi |" )
    print("+====================================================+")
    print(f"Username: {username}")
    
    while True:
        password = pwinput.pwinput("Masukkan Password: ")
        akun_ada = False
        
        for user in login_data:
            if user["Nama User"].lower() == username.lower():
                if user["Pw User"] == password:
                    akun_ada = True
                    saldo_cust = user["Saldo"] 
                    print("+----------------------------------------------------+")
                    print("|                    Saldo E-Money                   |")
                    print("+----------------------------------------------------+")
                    print(f"> Username: {username}                               ")
                    print(f"> Saldo E-Money Anda saat ini adalah Rp. {saldo_cust}")
                    print("+----------------------------------------------------+")
                    continue
                
        while True:       
            back = input("Ketik b untuk kembali ke menu customer: ")
                
            if back.lower() == "b":
                customer()
                break
            else:
                print("!!! Ketik b jika ingin kembali ke menu customer !!!")
                pass
                    
        if akun_ada:
            break
        else:
            print("+================================================================+")
            print("| Akun tidak ditemukan atau kata sandi salah. Silakan coba lagi. |")
            print("+================================================================+\n")




'''=============================================================================================================='''
'''                                                 TOP UP Saldo                                                 '''
'''=============================================================================================================='''



def top_up():
    login_data = load_data_user()
    print("\n+====================================================+")
    print("| Masukkan password anda untuk melanjutkan transaksi |" )
    print("+====================================================+")
    print(f"Username: {username}")
    
    while True:
        password = pwinput.pwinput("Masukkan Password: ")
        akun_ada = False
        
        for user in login_data:
            if user["Nama User"].lower() == username.lower():
                if user["Pw User"] == password:
                    akun_ada = True
                    saldo_cust = user["Saldo"] 
                    print(f"Saldo sekarang: {saldo_cust}")
                    break
                    
        if akun_ada:
            break
        else:
            print("+================================================================+")
            print("| Akun tidak ditemukan atau kata sandi salah. Silakan coba lagi. |")
            print("+================================================================+\n")
            
            
    while True:
        print("\n+------------TOP UP SALDO-----------+")
        print("| 1. RP. 500.000                    |")
        print("| 2. RP. 1.000.000                  |")
        print("| 3. RP. 2.000.000                  |")
        print("| 4. RP. 3.000.000                  |")
        print("| 5. RP. 7.000.000                  |")
        print("| 6. Nominal Lain                   |")
        print("+-----------------------------------+")
            
        try:
            pilihan = input("Pilih opsi top-up (1/2/3/4/5/6): ")
            
            if pilihan in ["1", "2", "3", "4", "5", "6"]:
                pilihan = int(pilihan)
                if pilihan == 1:
                    jumlah_topup = 500000
                elif pilihan == 2:
                    jumlah_topup = 1000000
                elif pilihan == 3:
                    jumlah_topup = 2000000
                elif pilihan == 4:
                    jumlah_topup = 3000000
                elif pilihan == 5:
                    jumlah_topup = 7000000
                elif pilihan == 6:
                    jumlah_topup = int(input("Masukkan nominal yang anda inginkan: "))
                    
                if jumlah_topup > 15000000:
                    print("+===========================================+")
                    print("| Top-up melebihi batas maksimal (15 juta). |")
                    print("+===========================================+\n")
                elif jumlah_topup < 0:
                    print("+=========================================================+")
                    print("| Input nominal tidak valid. Top-up tidak boleh dibawah 0 |")
                    print("+=========================================================+\n")
                else:
                    saldo_cust += jumlah_topup
                    print(f"---Saldo E-Money berhasil ditambahkan sebesar Rp. {jumlah_topup}---")
                    print(f"     Total saldo E-Money anda sekarang adalah Rp. {saldo_cust}     ")
                    
                    for user in login_data:
                        if user["Nama User"].lower() == username.lower():
                            user["Saldo"] = saldo_cust
                            save_data_user(login_data)
                            
                            with open("emoney.txt", "a") as saldo:
                                print("+=====================================================+", file=saldo)
                                print("|                   TOP UP SALDO                      |", file=saldo)
                                print("+-----------------------------------------------------+", file=saldo)
                                print(f"Username: {username}", file=saldo)
                                print(f"Saldo E-Money berhasil ditambahkan sebesar Rp. {jumlah_topup}", file=saldo)
                                print(f"Total saldo E-Money anda sekarang adalah Rp. {saldo_cust}", end="\n", file=saldo)
                                print("+=====================================================+", file=saldo)
                            break
            else:
                print("+=====================================================+")
                print("| Pilihan tidak valid. Silakan pilih opsi yang benar. |")
                print("+=====================================================+\n")
                
            ulangi = input("Apakah Anda ingin melakukan top-up lagi? (y/t): ")
            if ulangi.lower() == "y":
                pass
            elif ulangi.lower() == "t":
                back = input("Apakah anda ingin kembali ke menu customer? (y/t): ")
                if back.lower() not in ["y", "t"]:
                    print("+======================================================================+")
                    print("| Input tidak valid. Silahkan pilih 'y' untuk ya atau 't' untuk tidak. |")
                    print("+======================================================================+\n")
                if back.lower() == "y":
                    customer()
                    break
                elif back.lower() == "t":
                    print("\n===================================================\n")
                    print("Masih ingin top up saldo?, silahkan top up kembali")
                    pass
            else:
                print("+======================================================================+")
                print("| Input tidak valid. Silahkan pilih 'y' untuk ya atau 't' untuk tidak. |")
                print("+======================================================================+\n")
                    
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}")




'''=============================================================================================================='''
'''                                        Sorting Produk Berdasarkan Harga                                      '''
'''=============================================================================================================='''



def sort_products():
    data = load_data()
    
    for kategori in data["Kategori"]:
        kategori["produk"] = sorted(kategori["produk"], key=lambda x: x["Harga"])
        
    save_data(data)
    print("\n-------Data telah diurutkan berdasarkan harga-------")
    display_products()
        
    try:
        back = input("Apakah anda ingin mengurutkan kembali berdasarkan ID? (y/t): ").lower()
        while back not in ["y", "t"]:
            print("+======================================================================+")
            print("| Input tidak valid. Silahkan pilih 'y' untuk ya atau 't' untuk tidak. |")
            print("+======================================================================+\n")
            back = input("Apakah anda ingin mengurutkan kembali berdasarkan ID? (y/t): ").lower()
            
        if back == "y":
            sort_id()
        elif back == "t":
            customer()
    except (ValueError, KeyboardInterrupt):
        print("\n+=============================================================+")
        print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
        print("+=============================================================+\n")
    except Exception as a:
        print(f"Error, {a}")




'''=============================================================================================================='''
'''                                          Sorting Produk Berdasrkan ID                                        '''
'''=============================================================================================================='''



def sort_id():
    data = load_data()
        
    for kategori in data["Kategori"]:
        kategori["produk"] = sorted(kategori["produk"], key=lambda x: x["ID"])
        
    save_data(data)
    print("\n-------Data telah diurutkan berdasarkan ID produk-------")
        
        
    display_products()
    customer()




'''=============================================================================================================='''
'''                                                       EXIT                                                   '''
'''=============================================================================================================='''



def exit():
            print("+================================+")
            print("|       TERIMA KASIH TELAH       |")
            print("|     BERBELANJA DI SHOPCOOLZ    |")
            print("+--------------------------------+")
            print("|       sampai jumpa lagi!       |")
            print("+================================+")




'''=============================================================================================================='''
'''                                                Menentukan ROLE                                               '''
'''=============================================================================================================='''



def start():  
    while True:  
        print("+-----------------------------------+")
        print("|               ROLE                |")
        print("+-----------------------------------+")   
        print("|           1. Admin                |")
        print("|           2. Customer             |")
        print("+-----------------------------------+")
        
        try:
            peran = input("Masukkan Peran Anda (1/2): ")
            if peran == "1":
                if admin_login():
                    admin()
                break
            elif peran == "2":
                user()
                break
            else:
                print("+==================================+")
                print("|  Tolong masukkan angka 1 atau 2  |")
                print("+==================================+")
                pass
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}")
start()
