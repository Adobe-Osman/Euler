#!/usr/bin/env python3

val = 0
for x in range(3, 1000, 3):
    val += x
for y in range(5, 1000, 5):
    if y % 3 != 0:
        val += y
print(val)
