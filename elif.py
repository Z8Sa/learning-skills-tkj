# elif

gaya1 = 10*":" + " MATERI TKJ " + 10*":"
judul = 15*" " + "TKJ" + 15*" "
menu = f"""
{gaya1}
• DASAR KOMPUTER (DKR)
• JARINGAN DASAR (JDR)
• ADMINISTRASI SISTEM (ASM)
• MIKROTIK (MRK)
• CISCO DAN JARINGAN (CDJ)
• WEB DAN PEMROGRAMAN DASAR (WPD)
• KEAMANAN JARINGAN (KJN)
• CLOUD DAN VIRTUALISASI (CDV)
• SKILL PENDUKUNG (SPG)
{gaya1}
"""
print(menu)
materi = input("PILIHAN MATERI : ")

print()

## DKR
if materi=="DKR":
    print(f"""{judul}
{gaya1}
• DASAR KOMPUTER
  0.EXIT
  1.Merakit PC
  2 Instalasi sistem operasi
  3.Troubleshooting komputer
  4.Partisi hard disk
  5.Backup dan restore data
{gaya1}""")

    DKR = input("PILIHAN PELAJARAN : ")
    if DKR=="0":
      print("EXIT")
    elif DKR=="1":
      print(f"LINK BELAJAR : https://youtu.be/yx7n_MsHqF0?si=08FgEJM7JsSTKTeb ")
    elif DKR=="2":
      print(f"LINK BELAJAR : 2")
    elif DKR=="3":
        print(f"LINK BELAJAR :3 ")
    elif DKR=="4":
        print(f"LINK BELAJAR :4 ")
    elif DKR=="5":
        print(f"LINK BELAJAR :5 ")


## JDR
if materi=="JDR":
    print(f"""{judul}
{gaya1}
• JARINGAN DASAR
  0.exit
  1.Konsep jaringan komputer
  2.Topologi jaringan
  3.Pengkabelan UTP
  4.Crimping kabel LAN
  5.Konfigurasi IP Address
  6.Subnetting
  7.Sharing file dan printer
{gaya1}""")

    JDR = input("PILIHAN PELAJARAN : ")
    if JDR=="0":
      print("EXIT")
    elif JDR=="1":
      print(f"LINK BELAJAR :1 ")
    elif JDR=="2":
      print(f"LINK BELAJAR :2 ")
    elif JDR=="3":
      print(f"LINK BELAJAR :3 ")
    elif JDR=="4":
      print(f"LINK BELAJAR :4 ")
    elif JDR=="5":
      print(f"LINK BELAJAR :5 ")
    elif JDR=="6":
      print(f"LINK BELAJAR :6 ")
    elif JDR=="7":
      print(f"LINK BELAJAR :7 ")


## ASM
elif materi=="ASM":
    print(f"""{judul}
{gaya1}
• ADMINISTRASI SISTEM
  0.exit
  1.Instalasi Linux
  2.Manajemen user Linux
  3.Dasar command line Linux
  4.Instalasi Windows Server
  5.Active Directory
  6.DHCP Server
  7.DNS Server
  8.File Server
{gaya1}""")
    ASM = input("PILIHAN PELAJAN : ")
    if ASM=="0":
      print("EXIT")
    elif ASM=="1":
      print("LINK BELAJAR : 1")
    elif ASM=="2":
      print("LINK BELAJAR : 2")
    elif ASM=="3":
      print("LINK BELAJAR : 3")
    elif ASM=="4":
      print("LINK BELAJAR : 4")
    elif ASM=="5":
      print("LINK BELAJAR : 5")
    elif JDR=="6":
      print(f"LINK BELAJAR :6 ")
    elif JDR=="7":
      print(f"LINK BELAJAR :7 ")
    elif JDR=="8":
      print(f"LINK BELAJAR :8 ")

## MRK
elif materi=="MRK":
    print(f"""
• MIKROTIK
  0.exit
  1.Konfigurasi router Mikrotik
  2.Routing dasar
  3.NAT
  4.Firewall
  5.Hotspot
  6.Bandwidth management
  7.VPN dasar
""")
    MRK = input("PILIHAN PELAJARAN : ")
    if MRK=="0":
      print("EXIT")
    elif MRK=="1":
      print("LINK BELAJAR : 1")
    elif MRK=="2":
      print("LINK BELAJAR : 2")
    elif MRK=="3":
      print("LINK BELAJAR : 3")
    elif MRK=="4":
      print("LINK BELAJAR : 4")
    elif MRK=="5":
      print("LINK BELAJAR : 5")
    elif MRK=="6":
      print("LINK BELAJAR : 6")
    elif MRK=="7":
      print("LINK BELAJAR : 7")
    

## CDJ
elif materi=="CDJ":
    print(f"""{judul}
{gaya1}
• CISCO DAN JARINGAN
  0.exit
  1.Switching
  2.VLAN
  3.Routing statis
  4.Routing dinamis
  5.Wireless networking
{gaya1}""")
    CDJ = input("PILIHAN PELAJARAN : ")
    if CDJ=="0":
      print("EXIT")
    elif CDJ=="1":
      print("LINK BELAJAR : 1")
    elif CDJ=="2":
      print("LINK BELAJAR : 2")
    elif CDJ=="3":
      print("LINK BELAJAR : 3")
    elif CDJ=="4":
      print("LINK BELAJAR : 4")
    elif CDJ=="5":
      print("LINK BELAJAR : 5")
    

## WPD
elif materi=="WPD":
    print(f"""{judul}
{gaya1}
• WEB DAN PEMROGRAMAN DASAR
  0.exit
  1.HTML
  2.CSS
  3.JavaScript dasar
  4.PHP dasar
  5.Database MySQL
{gaya1}""")
    WPD = input("PILIHAN PELAJARAN : ")
    if WPD=="0":
      print("EXIT")
    elif WPD=="1":
      print("LINK BELAJAR : 1")
    elif WPD=="2":
      print("LINK BELAJAR : 2")
    elif WPD=="3":
      print("LINK BELAJAR : 3")
    elif WPD=="4":
      print("LINK BELAJAR : 4")
    elif WPD=="5":
      print("LINK BELAJAR : 5")

## KJN
elif materi=="KJN":
    print(f"""{judul}
{gaya1}
• KEAMANAN JARINGAN
  0.exit
  1.Keamanan jaringan dasar
  2.Monitoring jaringan
  3.Analisis log
{gaya1}""")
    KJN = input("PILIHAN PELAJARAN : ")
    if KJN=="0":
      print("EXIT")
    elif KJN=="1":
      print("LINK BELAJAR : 1")
    elif KJN=="2":
      print("LINK BELAJAR : 2")
    elif KJN=="3":
      print("LINK BELAJAR : 3")

## CDV
elif materi=="CDV":
    print(f"""{judul}
{gaya1}
• CLOUD DAN VIRTUALISASI
  0.exit
  1.VirtualBox
  2.VMware
  3.Virtual server
  5.Cloud computing dasar
{gaya1}""")
    CDV = input("PILIHAN PELAJARAN : ")
    if CDV=="1":
      print("LINK BELAJAR : 1")
    if CDV=="2":
      print("LINK BELAJAR : 2")
    if CDV=="3":
      print("LINK BELAJAR : 3")
    if CDV=="4":
      print("LINK BELAJAR : 4")
    if CDV=="5":
      print("LINK BELAJAR : 5")

## SPG
elif materi=="SPG":
    print(f"""{judul}
{gaya1}
• SKILL PENDUKUNG
  0.exit
  1.Dokumentasi teknis
  2.Presentasi proyek
  3.Kerja tim
  4.PKL/Magang
  5.Manajemen proyek sederhana
  6.Penggunaan Git dan GitHub
{gaya1}""")
    SPG = input("PILIHAN PELAJARAN : ")
    if SPG=="0":
      print("EXIT")
    elif SPG=="1":
      print("LINK BELAJAR : 1")
    elif SPG=="2":
      print("LINK BELAJAR : 2")
    elif SPG=="3":
      print("LINK BELAJAR : 3")
    elif SPG=="4":
      print("LINK BELAJAR : 4")
    elif SPG=="5":
      print("LINK BELAJAR : 5")
    elif SPG=="6":
      print("LINK BELAJAR : 6")

else:
  print("Masukkan perintah yang benar")
  print()
print()
print("Close Program!!!....")
