import numpy as np

#list python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

#element twise
hasil = arr1 + arr2
print(hasil)

hasil = arr1 - arr2
print(hasil)

hasil = arr1 * arr2
print(hasil)

hasil = arr1 / arr2
print(hasil)

hasil = arr1**2
print(hasil)

c = np.array(([1, 2, 3], [4, 5, 6]))
d = np.array(([7, 8, 9], [-1, -2, -3]))

hasil = c + d
print(hasil)