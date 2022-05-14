import scmanz
import os
#Malu Tolol Udah Gede Masih Recode
#Recode Izin dulu dek
#Yang Recode Gua Doain Jadi Bodoh 
Hijau = '\033[1;32m'
Kuning = '\033[1;33m'
Merah = '\033[1;31m'
Putih = '\033[1;37m'
os.system('clear')
print(f'''{Merah}Program Kal{Putih}kulator V2
{Merah}  ----\\Xm4{Putih}nXp\\----
{Merah}Curva Boys {Putih}Cyber Team
        {Merah}--{Putih}--
''')
print(f"{Kuning}1. {Putih}Matematika")
print(f"{Kuning}2. {Putih}Fisika")
print("")
try:
  inpuser = int(input(f"Masukkan Nomor {Merah}>{Putih} "))
  os.system('clear')
  if inpuser == 1:
    print(f'''{Merah}Program Kal{Putih}kulator V2
{Merah}  ----\\Xm4{Putih}nXp\\----
     {Merah}MateM{Putih}aTika
        {Merah}--{Putih}--
''')
    print(f"{Kuning}1. {Putih}Pertambahan")
    print(f"{Kuning}2. {Putih}Pengurangan")
    print(f"{Kuning}3. {Putih}Perkalian")
    print(f"{Kuning}4. {Putih}Pembagian")
    print("")
    inpuser2 = int(input(f"Masukkan Nomor {Merah}>{Putih} "))
    os.system('clear')
    if inpuser2 == 1:
       print(f'''
{Hijau}Tools Pertambahan{Putih}
      ----
       ++
''')
       inpus = int(input(f"Masukkan Angka Pertama : {Kuning}"))
       inpus2 = int(input(f"{Putih}Masukkan Angka Kedua : {Kuning}"))
       print(f"{Putih}Hasil Dari {Kuning}{inpus} {Putih}+ {Kuning}{inpus2} {Putih}:  {Hijau}{scmanz.tambah(inpus,inpus2)}{Putih}")
    elif inpuser2 == 2:
       print(f'''
{Hijau}Tools Pengurangan{Putih}
      ----
       ++
''')
       inpus = int(input(f"Masukkan Angka Pertama : {Kuning}"))
       inpus2 = int(input(f"{Putih}Masukkan Angka Kedua : {Kuning}"))
       print(f"{Putih}Hasil Dari {Kuning}{inpus} {Putih}- {Kuning}{inpus2} {Putih}:  {Hijau}{scmanz.kurang(inpus,inpus2)}{Putih}")
    elif inpuser2 == 3:
       print(f'''
{Hijau}Tools Perkalian{Putih}
      ----
       ++
''')
       inpus = int(input(f"Masukkan Angka Pertama : {Kuning}"))
       inpus2 = int(input(f"{Putih}Masukkan Angka Kedua : {Kuning}"))
       print(f"{Putih}Hasil Dari {Kuning}{inpus} {Putih}* {Kuning}{inpus2} {Putih}:  {Hijau}{scmanz.kali(inpus,inpus2)}{Putih}")
    elif inpuser2 == 4:
       print(f'''
{Hijau}Tools Pembagian
      {Putih}----
       ++
''')
       inpus = int(input(f"Masukkan Angka Pertama : {Kuning}"))
       inpus2 = int(input(f"{Putih}Masukkan Angka Kedua : {Kuning}"))
       print(f"{Putih}Hasil Dari {Kuning}{inpus} {Putih}/ {Kuning}{inpus2} {Putih}:  {Hijau}{scmanz.bagi(inpus,inpus2)}{Putih}")
    else:
       print("iya")
  elif inpuser == 2:
    print(f'''{Merah}Program Kal{Putih}kulator V2
{Merah}  ----\\Xm4{Putih}nXp\\----
       {Merah}Fis{Putih}iKa
        {Merah}--{Putih}--
''')
    print(f"{Kuning}1.{Putih} Celcius To Farenheit")
    print(f"{Kuning}2.{Putih} Farenheit To Celcius")
    print(f"{Kuning}3.{Putih} Celcius To Kelvin")
    print(f"{Kuning}4.{Putih} Kelvin To Celcius")
    print(f"{Kuning}5.{Putih} Celcius To Reamur")
    print(f"{Kuning}6.{Putih} Reamur To Celcius")
    print("")
    inpuser2 = int(input(f"Masukkan Nomor{Merah} >{Putih} "))
    os.system('clear')
    if inpuser2 == 1:
        print(f'''
{Hijau}Tools C° To F°{Putih}
      ----
       ++
''')
        inpus = int(input(f"Angka Celcius(C°) Nya : {Kuning}"))
        print(f"{Putih}Hasil {Kuning}{inpus}C°{Putih} To F° : {Hijau}{scmanz.C(inpus)}F°{Putih}")
    elif inpuser2 == 2:
        print(f'''
{Hijau}Tools F° To C°{Putih}
      ----
       ++
''')
        inpus = int(input(f"Angka Farenheit(F°) Nya : {Kuning}"))
        print(f"{Putih}Hasil {Hijau}{inpus}F°{Putih} To C° : {Hijau}{scmanz.Fc(inpus)}F°{Putih}")
    elif inpuser2 == 3:
        print(f'''
{Hijau}Tools C° To K°{Putih}
      ----
       ++
''')
        inpus = float(input(f"Angka Celcius(C°) Nya : {Kuning}"))
        print(f"{Putih}Hasil {Hijau}{inpus}C°{Putih} To K° : {Hijau}{scmanz.ck(inpus)}K°{Putih}")
    elif inpuser2 == 4:
        print(f'''
{Hijau}Tools K° To C°{Putih}
      ----
       ++
''')
        inpus = int(input(f"Angka Kelvin(K°) Nya : {Kuning}"))
        print(f"{Putih}Hasil {Kuning}{inpus}K°{Putih} To C° : {Hijau}{scmanz.kc(inpus)}C°{Putih}")

    elif inpuser2 == 5:
        print(f'''
{Hijau}Tools C° To R°{Putih}
      ----
       ++
''')
        inpus = int(input(f"Angka Celcius(C°) Nya :{Kuning} "))
        print(f"{Putih}Hasil {Kuning}{inpus}C°{Putih} To R° : {Hijau}{scmanz.cr(inpus)}R°{Putih}")
    elif inpuser2 == 6:
        print(f'''
{Hijau}Tools R° To C°{Putih}
      ----
       ++                                                             ''')
        inpus = int(input(f"Angka Reamur(R°) Nya : {Kuning}"))
        print(f"{Putih}Hasil {Kuning}{inpus}R°{Putih} To C° : {Hijau}{scmanz.rc(inpus)}C°{Putih}")
    else:
        Print(f"{Merah}Masukin Yang Bener Dekk!!!")
except ValueError:
  print(f"{Merah}Yang Anda Masukkan Bukanlah Angka !{Putih}")
