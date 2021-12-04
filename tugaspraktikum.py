print ("------------------")
print ("Pertemuan ke 10")
print ("tugas praktikum")
print ("------------------")

import  O5,Sys
p = print
oc  = O5.system
while true:
    p("")
    p("")
    c = input("A)add, E)dit, D)dit, D)elete, S)search, L)ist, Q)uit:")
    if c.lower() == "q":
        break
    elif c.lower() == "q" : ""
    elif c.lower() == "l" : ""
    elif c.lower() == "s" : ""
    elif c.lower() == "d" : ""
    elif c.lower() == "e" : ""
    elif c.lower() == "a" :
        i = open("database.txt","a")
        P("tambah kontak")
        while (true):
            nama = input ("nama :")
            if nama == "":
                P("masukkan nama dengan benar")
            else:
                    break
        while (true):""
        while (true):""
        while (true):""
        while (true):
            try:
                uaus = int(input("uas :"))
                if uas == "":
                    P("masukkan uas dengan angka")
            except ValueError:
                P("masukkan uas dengan angka")
            else:
                break
        akhir = round ((float(tugas)*0.3)+(float(uts)*0.35)+(float(uas)*0.35),2)
        i.write("\nNama : "+nama+"|nim :"+str(nim)+"|tugas :"+str(tugas)+"|UTS :"+str(uts)+"|UAS :"+str(uas)+"|Akhir :"+str(akhir)+"\n")
        i.close()
        oc ("clear")