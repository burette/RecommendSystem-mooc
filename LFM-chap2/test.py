#!/usr/bin/env python
# encoding: utf-8
'''
@author: burette
@contact: lizhiwnebit@126.com
@file: test.py
@time: 2019/11/19 2:54 下午
@desc:
'''

print(float("-1.234"))
# print(float(" "))
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[1:-1])

print(float("318"))

dict = {
    'b': 2,
    'h': 2,
    'c': 5,
    'e': 4,
    'w': 3,
    'q': 3,
    'a': 7,
}

print(dict)
sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(dict)
for zuhe in sorted(dict.items(), key=lambda x: x[1], reverse=True)[:]:
    print(str(zuhe[0]) + "_" + str(zuhe[1]))
