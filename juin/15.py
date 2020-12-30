#!/usr/bin/env python3

# 15 Juin

nb = 0
for n in range(10000, 100000):
    s = 0
    while n != 0:
        n, u = divmod(n, 10)
        s += u
    if u % 10 == 7:
        nb += 1

print("réponse:", nb)