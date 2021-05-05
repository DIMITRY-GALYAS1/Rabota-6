#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = list(map(float, input("Введите значения U: ").split()))
    m = 999999999999
    n = 0
    count = 1
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    for item in a:
        if item > 0:
            count *= item
    print('Произведение положительных элементов', count)
    for i in range(len(a)):
        if m > a[i]:
            m = a[i]
            n = i
    c = a[:n]
    s = sum(c)
    print("Сумма перед минимальным числом", s)
    z = len(c)
    chet = []
    nechet = []
    for i in range(z):
        if i % 2 == 0:
            chet.append(c[i])
        else:
            nechet.append(c[i])
    print('По возрастанию', chet)
    print('По убыванию', nechet)
