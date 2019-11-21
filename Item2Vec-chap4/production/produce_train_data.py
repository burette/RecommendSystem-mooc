#!/usr/bin/env python
# encoding: utf-8
'''
@author: burette
@contact: lizhiwnebit@126.com
@file: produce_train_data.py
@time: 2019/11/19 9:18 下午
@desc: produce train data for item2vec
'''
import os
import sys


def produce_train_data(input_file, out_file):
    """
    :param input_file: 将要处理的用户行为文件
    :param out_file: 将得到的训练数据输出到的文件
    :return:
    """
    if not os.path.exists(input_file):
        return "input_file not exist"
    record = {}  # 用来记录用户喜欢过的物品
    score_thr = 4.0  # 区分用户喜欢与不喜欢的边界分数，认为定义
    linenum = 0
    fp = open(input_file)
    for line in fp:
        if linenum == 0:
            linenum += 1
            continue
        item = line.strip().split(',')
        if len(item) < 4:  # 小于4列过滤掉
            continue
        userid, itemid, rating = item[0], item[1], float(item[2])  # item2vec忽略时间因素，因此只取前三列
        if rating < score_thr:
            continue
        if userid not in record:
            record[userid] = []
        record[userid].append(itemid)
    fp.close()
    fw = open(out_file, 'w+')
    for userid in record:
        fw.write(" ".join(record[userid]) + "\n")
    fw.close()


if __name__ == "__main__":
    if len(sys.argv) <3:
        print("usage: python XX.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        produce_train_data(input_file,output_file)
    # produce_train_data("../data/ratings_1000000.csv", "../data/train_data.txt")
