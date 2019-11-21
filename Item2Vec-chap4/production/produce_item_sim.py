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
import sys


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
        item = line.strip().split(' ')  # 按空格进行切分
        if len(item) < 129:  # 设置输出向量为128微+itemid共129维
            continue
        itemid = item[0]  # itemid为第一列
        if itemid == "</s>":  # 如果是换行符，则为第一列
            continue
        item_vec[itemid] = np.array([float(ele) for ele in item[1:]])
    fp.close()
    return item_vec


def cal_tem_sim(item_vec, itemid, output_file):
    """
    item向量，待计算的itemit，保存到的输出文件
    :param item_vec:
    :param itemid:
    :param output_file:
    :return: 无返回，直接保存文件
    """
    if itemid not in item_vec:
        return
    score = {}  # 记录其它item的向量与itemid的cos计算距离
    topK = 10  # 自定义结果中的个数
    fix_item_vec = item_vec[itemid]
    for tmp_itemid in item_vec:
        if tmp_itemid == itemid:
            continue
        tmp_item_vec = item_vec[tmp_itemid]
        fenmu = np.linalg.norm(fix_item_vec) * np.linalg.norm(tmp_item_vec)
        if fenmu == 0:
            score[tmp_itemid] = 0
        else:
            score[tmp_itemid] = round(np.dot(fix_item_vec, tmp_item_vec) / fenmu, 3)
    fw = open(output_file, 'w+')
    out_str = itemid + "\t"
    tmp_list = []
    for zuhe in sorted(score.items(), key=lambda x: x[1], reverse=True)[:topK]:
        tmp_list.append(str(zuhe[0]) + "_" + str(zuhe[1]))
    out_str += ";".join(tmp_list)
    fw.write(out_str + "\n")
    fw.close()


# 测试函数
def run_main(input_file, output_file):
    item_vec = load_item_vec(input_file)
    cal_tem_sim(item_vec, "27", output_file)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage python XX.py input_file output_file")
        sys.exit()
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        run_main(input_file, output_file)
    # item_vec = load_item_vec("../data/item_vec.txt")
    # print(len(item_vec))
    # run_main("../data/item_vec.txt", "../data/sim_result.txt")
