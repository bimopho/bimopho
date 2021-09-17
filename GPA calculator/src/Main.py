print("Selamat datang di Kalkulator IPK!")

# meminta input kepada user
jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
while jumlah_matkul < 0:
    print("Input tidak valid, silahkan masukkan ulang.")
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
print()

# mendefinisikan variabel yang akan di increment
jumlah_sks = 0
jumlah_sks_tidak_lulus = 0
jumlah_mutu = 0
jumlah_mutu_tidak_lulus = 0

if jumlah_matkul == 0:
    print("Tidak ada mata kuliah yang diambil.")
else:
    # menggunakan for loop untuk meminta input
    for i in range(1, jumlah_matkul + 1):
        nama_matkul = input(f"Masukkan nama mata kuliah ke-{i}: ")
        sks = int(input(f"Masukkan jumlah SKS {nama_matkul}: "))
        nilai = float(input("Masukkan nilai yang kamu dapatkan: "))
        while nilai < 0:
            print("Nilai tidak valid, silahkan masukkan ulang nilai")
            nilai = float(input("Masukkan nilai yang kamu dapatkan: "))
        print()

        # pengkelompokkan bobot
        if nilai >= 85:
            bobot = 4.00
        elif 80 <= nilai < 85:
            bobot = 3.70
        elif 75 <= nilai < 80:
            bobot = 3.30
        elif 70 <= nilai < 75:
            bobot = 3.00
        elif 65 <= nilai < 70:
            bobot = 2.70
        elif 60 <= nilai < 65:
            bobot = 2.30
        elif 55 <= nilai < 60:
            bobot = 2.00
        elif 40 <= nilai < 55:
            bobot = 1.00
        else:
            bobot = 0.00

        # menambahkan sks dan mutu ke variabel global yg sudah didefinisikan diatas
        jumlah_sks += sks
        
        if bobot <= 1.00:
            jumlah_sks_tidak_lulus += sks
            mutu_tidak_lulus = sks * bobot
            jumlah_mutu_tidak_lulus += mutu_tidak_lulus
    
        mutu = sks * bobot
        jumlah_mutu += mutu
            
    # IPT memperhitungkan mata kuliah yang lulus dan tidak lulus, sementara IPK hanya memperhitungkan mata kuliah yang lulus.
    # printing dan formatting sekaligus perhitungan jumlah sks dan mutu serta total IPK dan IPT
    print()
    print(f"Jumlah SKS lulus : {jumlah_sks - jumlah_sks_tidak_lulus} / {jumlah_sks}")
    print(f"Jumlah mutu lulus: {(jumlah_mutu - jumlah_mutu_tidak_lulus): .2f} / {jumlah_mutu: .2f}")
    print(f"Total IPK kamu adalah {(jumlah_mutu - jumlah_mutu_tidak_lulus)/(jumlah_sks - jumlah_sks_tidak_lulus) if (jumlah_sks - jumlah_sks_tidak_lulus) != 0 else 0: .2f}")
    print(f"Total IPT kamu adalah {(jumlah_mutu/jumlah_sks):.2f}")