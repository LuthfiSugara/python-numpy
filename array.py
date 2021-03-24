import numpy as np

#membuat vektor
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([1.5, 2.4, 3, 7, 2])

#membuat vektor dengan range
c = np.arange(1, 10, 1)

#membuat linear space
d = np.linspace(1, 10, 4)

#membuat matrix
e = np.array([ (1, 2, 3), (4, 5, 6) ])

#matrix dengan nilai nol
f = np.zeros((5, 5))

#matrix dengan nilai 1
g = np.ones(5)

#matrix identitas
h1 = np.identity(5)
h2 = np.eye(5)

print(h2)