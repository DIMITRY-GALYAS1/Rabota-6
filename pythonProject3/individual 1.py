#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

if __name__ == '__main__':

    U = list([random.randint(20, 30) for i in range(7)])
    D = list([random.randint(20, 30) for i in range(7)])
    V = list([random.randint(20, 30) for i in range(7)])
    G = []
    for (u, d, v) in zip(U, D, V):
        G.append((u+d+v)/3)
    print("Среднее значение температуры по дням недели: ", G)
