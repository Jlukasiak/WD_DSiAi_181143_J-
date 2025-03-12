import numpy as np

A = np.array([3, 5, 7, 9])
B = np.array([2, 4, 6, 8])
wynik1 = A / B #lub np.divide(A,B)

#zadanie2
X = np.array([[1, 2, 3], [4, 5, 6]])
skalar = 3
wynik2 = X + skalar

#zadanie3
C = np.array([10, 20, 30, 40])
D = np.array([1, 2, 3, 0])

wynik3 = C - D

#zadanie4
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([10, 20, 30])
wynik4 = M + v

#zadanie5
Z = np.zeros((3, 4))
O = np.ones(4)
wynik5 = Z + O

#zadanie6
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20])
wynik6 = A * B[:,np.newaxis]

#zadanie7
temps = np.array([0, 10, 20, 30, 40])

TEMPERATURAAAA = temps * 9/5 + 32

#zadanie 8
Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
wynik8 = np.sqrt(Y)

#zadanie 9
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

sin_values = np.sin(angles)
cos_values = np.cos(angles)
tan_values = np.tan(angles)

#zadanie 10
A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])

wynik10 = A % B

#zadanie11
X = np.array([[2, 5, 8], [1, 3, 7], [4, 6, 9]])
Y = np.array([1, 2, 3])
wynik11a = np.maximum(X, Y)

#zadanie12
values = np.array([-3, -2, -1, 0, 1, 2, 3])
wynik12 = np.abs(values)

#zadanie13
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[10, 20, 30], [40, 50, 60]])
wynik13 = np.power(A.astype(np.float64), B.astype(np.float64))

#zadanie14
probabilities = np.array([0.1, 0.01, 0.001, 0.0001])

wynik14a = np.log(probabilities)
wynik14b = np.log10(probabilities)

#zadanie15
M = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([[10], [20]])
wynik15 = M + v