teori = int(input("Masukkan nilai ujian teori: "))
praktek = int(input("Masukkan nilai ujian praktek: "))

if teori >= 70 and praktek >= 70 :
    print("Selamat, anda lulus!")
elif teori <= 70 and praktek <= 70 :
    print("Anda harus menulang ujian teori dan praktek")
elif teori <= 70 and praktek >= 70 :
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian praktek")