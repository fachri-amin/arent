harga = '123456789'
# hargaOut = ''
# i = 4
# j = 0
# while(i<len(harga)):
#     hargaOut += harga[:(len(harga)-(i-j))]+'.'+harga[i:]
#     j+=1
#     i+=2

# print(hargaOut)

# for i in range(0,len(harga),1):
#     print('ini harga[:',i,']')
#     print(harga[:i])
#     print('ini harga[',i,':]')
#     print(harga[i:])
#     print('=========================')

# j=0
keluaran = []
for i in range(0,len(harga),(1)):
    keluaran.append(harga[i])

for i in range(len(keluaran),0,-3):
    keluaran.insert(i,'.')
del keluaran[(len(keluaran)-1)]
outan = ''.join(keluaran)
print(outan)