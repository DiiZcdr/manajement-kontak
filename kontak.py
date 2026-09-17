import json
import os

#utamanya

File = "kontak.json"

def muat_data():
    if os.path.exists(File):
        with open(File, "r") as file:
            return json.load(file)
    return[]

def simpan_data(kontak_list):
    with open(File, "w") as file:
        json.dump(kontak_list, file, indent=4)

#operasi
def lihat(kontak_list):
    if not kontak_list:
        print("Belum ada kontak yg tersimpan")
        return
    print("\n---Daftar Kontak---")
    for i, kontak in enumerate(kontak_list, start=1):
        print(f"{i}, {kontak['nama']} | {kontak['No']} | {kontak['Email']}")

def add(kontak_list):
    print("\n---Tambah Kontak---")
    Nama = input("Masukan Nama: ").strip()
    No = input("Masukan No Hp: ").strip()
    Email = input("Masukan Email: ").strip()

    kontak_list.append({"nama": Nama, "No": No, "Email": Email})
    simpan_data(kontak_list)
    print(f"{Nama} Berhasil di masukkan ke dalam kontak")

def search(kontak_list):
    print("\n---cari kontak---")
    keyword = input("Masukan nama kontak yang ingin dicari: ")
    hasil = [k for k in kontak_list if keyword in k['Nama'].lower()]

    if hasil:
        print(f"\nkontak ditemukan {len(hasil)} kontak: ")
        for k in hasil:
            print(f"- {k['Nama']} | {k['No']} | {k['Email']}")

    else:
        print("Kontak tidak ditemukan")

def hapus(kontak_list):
    lihat(kontak_list)
    if not kontak_list:
        return

    print("\n---hapus kontak---")
    try:
        no = int(input("Masukkan Nomor Kontak Yang Ingin Dihapus: "))
        if 1 <= no <= len(kontak_list):
            kontak_dihapus = kontak_list.pop(no - 1)
            simpan_data(kontak_list)
            print("Kontak Berhasil Dihapus")

        else:
            print("Kontak tidak ditemukan")
    except ValueError:
        print("input harus menggunakan angka")

#program
def main():
    kontak_list = muat_data()

    while True:
        print("\n=======Kontak=======")
        print("1. Melihat kontak")
        print("2. Menambah Kontak")
        print("3. Menghapus Kontak")
        print("4. Mencari Kontak")
        print("5. Keluar")
        print("\n====================")

        pilihan = input("Pilih Menu: ")

        #if else
        if pilihan == "1":
            lihat(kontak_list)
            input("\nTekan [Enter] Untuk kembali ke menu...")
        elif pilihan == "2":
            add(kontak_list)
        elif pilihan == "3":
            hapus(kontak_list)
        elif pilihan == "4":
            search(kontak_list)
        elif pilihan == "5":
            print("Terimakasih Telah Menggunakan sistem ini")
            break
        else:
            print("Pilihan Tidak Valid")
            break

if __name__ == "__main__":
    main()

