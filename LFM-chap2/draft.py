#!/usr/bin/env python
# encoding: utf-8
'''
@author: burette
@contact: lizhiwnebit@126.com
@file: draft.py
@time: 2019/11/19 2:55 下午
@desc:
'''

import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
print(np.dot(a, b))

print(np.add(a, b))
print(np.min(a))
print(np.max(b))

print(np.matmul(a,b))
print(np.linalg.norm(a))
print(np.linalg.norm(b))
