a= '=' *40
b= '-'*40

print(a)
print('SWALAYAN SEHAT SENTAUSA'.center(40))
print(a)

nama = input('Masukkan Nama Anda: ')
barang= input('Masukkan Nama Barang : ')
harga = int(input('Masukkan Harga Barang : '))
jumlah = int(input('Masukkan Jumlah Beli : '))
total = harga * jumlah

diskon = 0
if harga>200000 :
    diskon = 0.10 * total
    print('Selamat Anda Mendapatkan Diskon 10%')

total2 = total - diskon

pajak = 0.05*total2

all = total2 + pajak

print('\n')
print(a)
print(' STRUK BELANJA '.center(40))
print(a)
print(f'Barang               : {barang}')
print(f'Harga/Unit           : Rp {harga}')
print(f'Jumlah               : {jumlah}')
print(b)
print(f'Total                : Rp {total}')
print(f'Diskon               : Rp {diskon}')
print(f'Harga setelah diskon : Rp {total2}')
print(f'Pajak                : Rp {pajak}')
print(f'Total Bayar          : Rp {all}')
print(a)

bayar = int(input('Masukkan Uang Anda : '))
kembali = bayar - all

print(f'Uang Tunai : Rp {bayar}')
print(b)
print(f'Kembalian  : Rp {kembali}')
print(a)

print("\napakah anda puas dengan layanannya?")
apa = input("(y/n): ").lower () == 'n'
if apa:
    print(input("apa keluhan anda: "))
    print(a)
    print("terimakasih telah berbelanja")
    print(a)

else:
    print(a)
    print("terimakasih telah berbelanja")
    print(a)