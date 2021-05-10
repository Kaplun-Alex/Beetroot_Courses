import matplotlib.pyplot as plt


x1 = [0.0015202999999999953, 0.005945599999999995, 0.013430999999999998, 0.02443859999999999, 0.038843900000000015,
     0.05742839999999999, 0.07877159999999997, 0.10202069999999996, 0.12967900000000004, 0.1668254]
x2 = [0.00030519999999999853, 0.0010538999999999965, 0.002384000000000004, 0.004232899999999998, 0.007105599999999997,
      0.0096819, 0.01312880000000001, 0.0169454, 0.02193189999999999, 0.027263399999999993]
x3 = [1.0400000000000686e-05, 1.860000000000056e-05, 2.7200000000004998e-05, 3.739999999999993e-05, 5.129999999999718e-05,
 6.0200000000003306e-05, 7.179999999999687e-05, 8.64999999999963e-05, 9.60999999999948e-05, 0.00010809999999999986]
y = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]

plt.plot(y, x1)
plt.plot(y, x2)
plt.plot(y, x3)
plt.show()