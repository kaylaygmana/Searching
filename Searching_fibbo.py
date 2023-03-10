import os
os.system("cls")

def fibo(q, nama, k):
    dataA = 0
    dataB = 1
    fibo = dataA + dataB
    while (fibo < k):
        dataA = dataB
        dataB = fibo
        fibo = dataA + dataB
    kurang = -1
    while (fibo > 1):
        i = min(kurang + dataA, k-1)
        if (q[i] < nama):
            fibo = dataB
            dataB = dataA
            dataA = fibo - dataB
            kurang = i
        elif (q[i] > nama):
            fibo = dataA
            dataB = dataB - dataA
            dataA = fibo - dataB
        else:
            return i
    if (dataB and q[k-1] == nama):
        return k-1
    return -1


list_nama = ["Arsel", "Avivah", "Daiva", ["wahyu", "wibi"]]

def cari():
    print ("="*15, "PENCARIAN KATA ".center(15), "="*15)
    for z in range(len(list_nama)):
        if type(list_nama[z]) == list:
            kolomdata = fibo(list_nama[z], nama, len(list_nama[z]))
            print(nama, "berada di array indenama ke -",z,"kolom",kolomdata)
            print("")
            return
        else:
            if list_nama[z] == nama:
                kolomdata = fibo(list_nama[z], nama, len(list_nama[z]))
                print(nama, "berada di array indenama ke -",z,)
                print("")
                return


nama = "Arsel"
cari()

nama = "Avivah"
cari()

nama = "Daiva"
cari()

nama = "wahyu"
cari()

nama = "wibi"
cari()