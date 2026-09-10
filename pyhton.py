print ("=====PROGRAM GENAP=====")
awal = int (input ("ketik nilai awal anda ="))
selisih = int ("ketik nilai selisihnya =")
akhir= int (input("ketik nilai akhir anda ="))

while awal <= akhir :
    if awal % 2 == 0:
        print (awal)
        awal += selisih 
