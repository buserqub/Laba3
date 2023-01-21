import pytest
import numpy as np

def Phibonachi (N):
    mas = [1, 1]
    for i in range(2, N):
        mas.append(1)
        mas[i] = mas[i - 2] + mas[i - 1]
        print (mas)
    return mas
def Bubble (mas):
    n = len(mas)
    for i in range(n):
        for j in range(n - 1):
            if (mas[j] > mas[j + 1]):
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    return mas
def Calc (x1, x2, ch):
    if ch == '+':
        return x1+x2
    if ch == '-':
        return x1-x2
    if ch == '*':
        return x1*x2
