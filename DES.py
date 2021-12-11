
pc1=[1,51,6,28,15,16,42,48,57,20,34,8,14,39,17,37,26,54,7,3,46,25,10,5,22,45,58,4,53,32,30,44,59,36,56,21,60,43,27,18,19,2,38,52,47,23,0,61,62,9,40,24,35,55,13,12]
pc2=[4,24,8,39,23,19,44,46,21,12,51,40,0,16,55,14,5,20,42,9,7,49,54,35,53,28,11,1,6,45,37,43,29,30,15,3,34,2,52,50,18,38,33,47,22,26,31,10]
nos=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

k=[1,1,1,0,1,0,0,0 ,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0]

class  DES:
    def __init__(self,IPTABLE,x):
        self.chiffre = []
        self.Klartext = x
        self.keygen = Keygen(pc1,pc2,nos)
        self.IPTABLE = IPTABLE
        self.REVIPTABLE = [42, 63, 43, 29, 56, 55, 4, 2, 39, 59, 9, 18, 41, 12, 7, 37, 1, 35, 57, 28, 38, 32, 27, 52, 3, 17, 26, 36, 13, 47, 16, 5, 33, 21, 30, 62, 6, 31, 46, 10, 60, 23, 22, 45, 19, 8, 14, 11, 48, 50, 20, 15, 54, 49, 44, 24, 0, 61, 40, 34, 58, 25, 51, 53]
        print(self.REVIPTABLE)
        print(self.IPTABLE)
        self.keygen.generatekeys(k)
        self.FN = FeistelNetwork(self.keygen.getkeylist())

    def IP(self,klartext):
        Permutatedkt = [klartext[x] for x in self.IPTABLE]
        return Permutatedkt

    def RIP(self,chiffre):
        Erg_chiffre =  [chiffre[x] for x in self.REVIPTABLE]
        return Erg_chiffre

    def encypt(self):
        momchiff = self.IP(self.Klartext)
        for i in range(17):
            momchiff=self.FN.Networkcycle(momchiff)
        self.chiffre=self.RIP(momchiff)
        return self.chiffre


class Keygen:
    def __init__(self,PC1TABLE,PC2TABLE,LSHIFTTABLE):
        self.PC1TABLE = PC1TABLE
        self.PC2TABLE = PC2TABLE
        self.LSHIFTTABLE = LSHIFTTABLE
        self.keys = []

    def getPC1(self, k):
        Perm_k=[]
        for position in self.PC1TABLE:
            Perm_k.append(k[position])
        return Perm_k

    def getPC2(self,k):
        Perm2_key=[]
        for position in self.PC2TABLE:
            Perm2_key.append(k[position])
        return Perm2_key


    def split28(self,obj):
        return obj[:28], obj[28:]

    def shift2x(self,input1, input2, repetitions):
        while repetitions != 0:
            temp = input1[0]
            input1 = input1[1:]
            input1.append(temp)
            temp = input2[0]
            input2 = input2[1:]
            input2.append(temp)
            repetitions-=1  # Wdh werden runter gezaehlt
        return input1, input2

    def generatekeys(self,k):
        self.keys = [] # RESET der key liste
        PCI_key= self.getPC1(k) # PCI auf key angewendet
        CN,DN = self.split28(PCI_key)
        for Lshiftcyclecount in self.LSHIFTTABLE:
            CN,DN = self.shift2x(CN,DN,Lshiftcyclecount)
            self.keys.append(self.getPC2(CN+DN))

    def getkeylist(self):
        return self.keys



class FeistelNetwork:
    def __init__(self,keylist): #IPX input x
        self.keylist = keylist
        self.position = 0

        self.EXPANSIONTABLE = [4,16,7,24,6,31,9,14,1,10,4,23,13,28,3,
                               8,30,25,11,30,17,3,20,5,5,18,26,22,19,
                               3,25,8,21,1,9,17,27,15,20,8,12,0,2,23,
                               23,18,29,1]

        self.PERMUTATIONTABLE = [23, 0, 27, 5, 26, 25, 21, 22, 28, 7,
                                 24, 17, 14, 11, 15, 20, 1, 4, 12, 9,
                                 13, 31, 8, 30, 19, 10, 2, 29, 6, 16,
                                 18, 3]

        sBox1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
                 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
                 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
                 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]

        sBox2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
                 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
                 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
                 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]

        sBox3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
                 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
                 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
                 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

        sBox4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
                 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
                 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
                 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]

        sBox5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
                 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
                 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
                 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]

        sBox6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
                 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
                 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
                 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

        sBox7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
                 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
                 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
                 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]

        sBox8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
                 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
                 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
                 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        self.sBoxen = [sBox1, sBox2, sBox3, sBox4, sBox5, sBox6, sBox7, sBox8]

    def split32(self,obj):
        return obj[:32],obj[32:]

    def Expansion(self,key):
        Expandet_key=[key[x] for x in self.EXPANSIONTABLE]
        return Expandet_key

    def Permutation(self, input):
        Permutatedkey = [input[x] for x in self.PERMUTATIONTABLE]
        return Permutatedkey

    def applySbox(self,bit_pair,sbox):
        Zeile = bit_pair[5] * 1 + bit_pair[0] * 2
        Spalte = bit_pair[4] * 1 + bit_pair[3] * 2 + bit_pair[2] * 4 + bit_pair[1] * 8
        return [int(x) for x in str(format(sbox[Zeile * 16 + Spalte], "04b"))]


    def xor(self,A, B):
        return [A[i] ^ B[i] for i in range(len(A))]

    def FFUNK(self,lRi,ki):
        key = self.Expansion(lRi)  # key is expender lRi
        key = self.xor(key,ki)      # key is XOR of Expendet lRi and ki
        bit_list = self.convert_to_6bit_list(key)
        concatenated_list = []
        for six_bit_pair, momsbox in zip(bit_list,self.sBoxen):
            concatenated_list+= self.applySbox(six_bit_pair, momsbox)

        return self.Permutation(concatenated_list)

    def convert_to_6bit_list(self,input):
        list_6_bit = []
        for x in range(8):
            list_6_bit.append(input[(x * 6):(x * 6 + 6)])
        return list_6_bit

    def Networkcycle(self,momkey):
        Lmom, Rmom = self.split32(momkey)  # L0,R0
        if (self.position == 16):
            print("Fertig")
            self.position=69
            return Rmom+Lmom
        elif(self.position == 69):
            print("FERTIG ALLA")
            return momkey
        f_funk_erg = self.FFUNK(Rmom,self.keylist[self.position])
        Rnew = self.xor(f_funk_erg,Lmom)
        Lnew = Rmom
        self.position+=1
        return Lnew+Rnew


ver = DES([56, 16, 7, 24, 6, 31, 36, 14, 45, 10, 39, 47, 13, 28, 46, 51, 30, 25, 11, 44, 50, 33, 42, 41, 55,
61, 26, 22, 19, 3, 34, 37, 21, 32, 59, 17, 27, 15, 20, 8, 58, 12, 0, 2, 54, 43, 38, 29, 48, 53, 49, 62,
23, 63, 52, 5, 4, 18, 60, 9, 40, 57, 35, 1], [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0])
print(ver.encypt())

""""
kg = Keygen(pc1,pc2,nos)
kg.generatekeys(k)


FN = FeistelNetwork(kg.getkeylist())
print(FN.FFUNK([1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1],[1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1]))
"""