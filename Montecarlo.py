# MUHAMMAD AMMAR NUGRAHA
# 152018091
# PEMSI APLIKASI MONTECARLO
#-----------------------------------------#
import random

def probkum(inprob):
    out = []
    out.append(inprob[0])
    panjang = len(inprob) - 1
    for x in range(panjang):
        n = out[x] + inprob[x+1]
        out.append(round(n,1))
    return out

def inputdata():
    while True:
        entry1 = input('permintaan = ')
        entry2 = input('minggu : ')
        if (entry1 == '') and (entry2 == ''):
                break
        try:
            datainput.append((int(entry1),int(entry2)))
        except:
            print("INPUT YANG BENAR!")

def interval(inprobkum):
    atas = []
    bawah = []
    bawah.append(0)
    for x in range((len(inprobkum))-1):
        n = inprobkum[x] + 0.001
        bawah.append(n)
    for x in range((len(inprobkum))):
        n = inprobkum[x]
        atas.append(n)
    return bawah, atas


def prob():
    ftot = 0
    out = []
    for x in range(len(datainput)):
        ftot += datainput[x][1]
    for x in range(len(datainput)):
        n = datainput[x][1] / ftot
        out.append(n)
    return out


def predict(banyaknya, bawah, atas, harga):
    total1 = 0
    total2 = 0
    data = []
    out = []
    for x in range(banyaknya):
        data.append(random.random())
    for x in range(banyaknya):
        if (data[x] >= bawah[0]) and (data[x] <= atas[0]):
            n=0
        elif (data[x] >= bawah[1]) and (data[x] <= atas[1]):
            n=1
        elif (data[x] >= bawah[2]) and (data[x] <= atas[2]):
            n=2
        elif (data[x] >= bawah[3]) and (data[x] <= atas[3]):
            n=3
        elif (data[x] >= bawah[4]) and (data[x] <= atas[4]):
            n=4
        out.append(n)
    data = []
    for x in  range(len(out)):
        total1 += out[x]
        n = out[x] * harga
        total2 += n
    print('Prediksi permintaan sebanyak = ', total1)
    print('Prediksi pengeluaran sebesar = Rp.',total2)

datainput = []
inputdata()
alpha = prob()
beta = probkum(alpha)
bo, ab = interval(beta)[:2]
npredict = int(input('Input banyak prediksi: '))
price = int(input('Input modal barang: '))
predict(npredict, bo, ab, price)