import numpy as np

#membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3], [4,5,6]), dtype= float)

#membuat array dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return (kolom + baris)

b = np.fromfunction(kuadrat, (1,10), dtype=int)
c = np.fromfunction(jumlah, (4,4), dtype=float)

# print(c)

#membuat array atau matrix dengan menggunakan iterable
iterable = (x*x for x in range(5))

d = np.fromiter(iterable, dtype = int)

#multiple array
dtipe = [('nama', 'S355'), ('tinggi', int)]

data = [
    ('saya', 180),
    ('kamu', 160),
    ('dia', 150)
]

e = np.array(data, dtype= dtipe)

print(e)