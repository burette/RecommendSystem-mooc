#!/usr/bin/env python
# encoding: utf-8
'''
@author: burette
@contact: lizhiwnebit@126.com
@file: produce_item_sim.py
@time: 2019/11/20 6:30 下午
@desc: produce item sim file
'''
import os
import numpy as np


def load_item_vec(input_file):
    """
    :param input_file: item vec file 训练完的文件
    :return:
    dict key: itemid value: np.array([num1,num2,...])
    """
    if not os.path.exists(input_file):
        return []
    linenum = 0
    item_vec = {}  # 用于记录返回结果
    fp = open(input_file)
    for line in fp:
        if linenum == 0:
            linenum += 1
            continue
        item = line.strip().split()
        if len(item) < 129:
            continue
        itemid = item[0]  # itemid为第一列
        if itemid == "</s>":  # 如果是换行符，则为第一列
            continue
        item_vec[itemid] = np.array([float(ele) for ele in line[1:]])
    fp.close()
    return item_vec


if __name__ == "__main__":
    item_vec = load_item_vec("../data/item_vec.txt")
    print(len(item_vec))
