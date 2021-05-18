#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':

    U = list([random.randint(20, 30) for i in range(7)])
    D = list([random.randint(20, 30) for i in range(7)])
    V = list([random.randint(20, 30) for i in range(7)])
    G = []
    i = 0
    while i < 7:
        G.append((U[i]+D[i]+V[i])/3)
        i += 1
    print("Среднее значение температуры по дням недели: ", G)
