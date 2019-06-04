import sys
import math
import subprocess
import os
from time import time as epochTime

class CGaussSolver:
    def __init__(self, a, b, n):
        self.m_A = a
        self.m_B = b
        self.m_N = n
        self.m_Result = 0

    def legendre(self, m_N, x):
        if m_N == 0:
            return 1
        elif m_N == 1:
            return x
        else:
            return ((2.0 * m_N - 1) / m_N) * x * self.legendre(m_N - 1, x) - ((1.0 * m_N - 1) / m_N) * self.legendre(m_N - 2, x)

    def dLegendre(self, m_N, x):
        dLegendre = 0
        dLegendre = (1.0 * m_N / (x * x - 1)) * ((x * self.legendre(m_N, x)) - self.legendre(m_N - 1, x));
        return dLegendre;

    def legendreZeroes(self, m_N, i):
        xnew1, xold1 = 0, 0
        xold1 = math.cos(math.pi * (i - 1 / 4.0) / (m_N + 1 / 2.0));
        iteration = 1
        while (1 + abs((xnew1 - xold1)) > 1.):
            if iteration != 1:
              xold1 = xnew1
            xnew1 = xold1 - self.legendre(m_N, xold1) / self.dLegendre(m_N, xold1)
            iteration += 1
        return xnew1;

    def weight(self, m_N, x):
        weightI = 0
        weightI = 2 / ((1 - pow(x, 2)) * pow(self.dLegendre(m_N, x), 2))
        return weightI

    def exec(self):
        integral = 0
        iteration = 1
        iteration += 1
        for i in range(1, self.m_N+1):
            integral = integral + self.aFunction(self.legendreZeroes(self.m_N, i)) * self.weight(self.m_N, self.legendreZeroes(self.m_N, i))
        self.m_Result = ((self.m_B - self.m_A) / 2.0) * integral

    def getResult(self):
        return self.m_Result;

    def aFunction(self, x):
        xN = 0.5 * x + 0.5
        return (pow(xN, 3) / (xN + 1))*math.cos(pow(xN, 2))

if __name__ == '__main__':
    a, b = 0, 1
    n = int(sys.argv[1])
    aSolver = CGaussSolver(a, b, n)
    aSolver.exec()
    print(f'Result of python code (n = {n} ): {aSolver.getResult()}')
    subprocess.call([os.path.join(os.getcwd(), 'HW5.exe'), str(n)])
    print('\n')

    for i in range(10):
        p_t1 = epochTime()
        aSolver = CGaussSolver(a, b, i)
        aSolver.exec()
        aSolver.getResult()
        p_t2 = epochTime()

        subprocess.call([os.path.join(os.getcwd(), 'HW5.exe'), str(i)])
        print(f' n = {i} & Python took: {(p_t2 - p_t1)*1000} ms\n')
