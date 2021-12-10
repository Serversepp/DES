from main import *
from fFunk import *
x = [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0]

IP =[56, 16, 7, 24, 6, 31, 36, 14, 45, 10, 39, 47, 13, 28, 46, 51, 30, 25, 11, 44, 50, 33, 42, 41, 55,
61, 26, 22, 19, 3, 34, 37, 21, 32, 59, 17, 27, 15, 20, 8, 58, 12, 0, 2, 54, 43, 38, 29, 48, 53, 49, 62,
23, 63, 52, 5, 4, 18, 60, 9, 40, 57, 35, 1]

AIP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53,
       21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

def IPERM(m):
    ret_m=[]
    for i in IP:
        ret_m.append(m[i])
    return ret_m[0:32], ret_m[32:]  #L0,R0

def iterations():
    t1 = PC1(k)
    t2 = key_gen(t1)
    L0,R0 = IPERM(x)

    for z in range(16):
        Lnext = R0                                  #r0 -> l1
        temp = f_funk(R0,t2[z])
        l_6 = prepSBox(temp)
        l_4 = []
        for i in range(0, len(l_6)):
            l_4.append(SBOX(l_6[i], sBoxen[i]))
        pe = []
        for i in l_4:
            pe = pe + i
        Rnext = [pe[i] ^ L0[i] for i in range(len(pe))]
        L0,R0=Lnext,Rnext
    ausgabe=R0+L0
    print(ausgabe)
    echtaus=[]
    for olaf in AIP:
        echtaus.append(ausgabe[olaf-1])

    return echtaus

print(iterations())