import des
k=[1,1,1,0,1,0,0,0 ,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0]

nos=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]




def PC1(k):
    k_p = []
    pc1=[1,51,6,28,15,16,42,48,57,20,34,8,14,39,17,37,26,54,7,3,46,25,10,5,22,45,58,4,53,32,30,44,59,36,56,21,60,43,27,18,19,2,38,52,47,23,0,61,62,9,40,24,35,55,13]
    print("hello")
    for x in pc1:
        k_p.append(k[x])
    return k_p
def PC2(k):
    pc2=[4,24,8,39,23,19,44,46,21,12,51,40,0,16,55,14,5,20,42,9,7,49,54,35,53,28,11,1,6,45,37,43,29,30,15,3,34,2,52,50,18,38,33,47,22,26,31,10]
    k_p2 = []
    for x in pc2:
        k_p2.append(k[x])
    return k_p2

def key_gen(input_key):
    keys=[]
    c0,d0=split(input_key)
    cnt = 0
    for x in nos:
        c0,d0=shift(c0,d0,x)
        keys.append(PC2(c0+d0))
        cnt+=1
    print(len(keys))
    return keys

def split(k_p):
    return k_p[:28],k_p[27:]

def shift(liste1,liste2,x):
    while x != 0:
        temp = liste1[0]
        liste1=liste1[1:]
        liste1.append(temp)
        temp = liste2[0]
        liste2=liste2[1:]
        liste2.append(temp)
        x=x-1
    return liste1,liste2



print(key_gen(PC1(k)))