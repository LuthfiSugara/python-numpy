import numpy as np

a = np.arange(10)**2

print(a)

#mengambil nilai
print('elemen ke 1 dari a adalah : ', a[0])
print('elemen ke 3 dari a adalah : ', a[2])
print('elemen terakhir dari a adalah : ', a[-1])

#slicing
print('elemen dari 1-6 adalah', a[0:6]) #a[start,end]
print('elemen dari 2-akhir adalah', a[1:]) #a[index ke 2,end]
print('elemen dari 5-awal adalah', a[:5]) #a[start, index ke 5]

#iterasi
for i in a:
    print('value : ', i)