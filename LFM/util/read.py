#!/usr/bin/env python
# encoding: utf-8
'''
@author: burette
@contact: lizhiwnebit@126.com
@file: read.py
@time: 2019/11/17 4:06 下午
@desc:
'''
import os


def get_item_info(input_file):
    """
    将movies.csv文件中的title、genre读取，获得key-value的{itemid:[title,genre]}
    :param input_file:
    :return:
    """
    if not os.path.exists(input_file):
        return {}
    item_info = {}
    linenum = 0
    fp = open(input_file)
    for line in fp:
        if linenum == 0:
            linenum += 1
            continue
        item = line.strip().split(',')
        if len(item) < 3:
            continue
        elif len(item) == 3:
            itemid, title, genre = item[0], item[1], item[2]
        elif len(item) > 3:
            itemid = item[0]
            title = item[1]
            genre = ",".join(item[1:-1])
        item_info[itemid] = [title, genre]
    fp.close()
    return item_info


def get_ave_score(input_file):
    """
    获得影片的平均评分,返回数据格式：key-value:{itemid:ave_score}
    :param input_file:
    :return:
    """
    if not os.path.exists(input_file):
        return {}
    linenum = 0
    record_dict = {}
    score_dict = {}
    fp = open(input_file)
    for line in fp:
        if linenum == 0:
            linenum += 1
            continue
        item = line.strip().split(',')
        if len(item) < 4:
            continue
        userid, itemid, rating = item[0], item[1], item[2]
        if itemid not in record_dict:
            record_dict[itemid] = [0, 0]
        record_dict[itemid][0] += 1
        record_dict[itemid][1] += float(rating)
    fp.close()
    for itemid in record_dict:
        score_dict[itemid] = round(record_dict[itemid][1] / record_dict[itemid][0], 3)  # 保留三位有效数字
    return score_dict


def get_train_data(input_file):
    """
    输入的是user-item的rating文件，输出的是list:[(userid,itemid,lable)]
    :param input_file:
    :return:
    """
    if not os.path.exists(input_file):
        return []

    score_dict = get_ave_score(input_file)
    neg_dict = {}  # 负样本
    pos_dict = {}  # 正样本
    train_data = []  # 输出的数据结构
    score_thr = 4.0  # 正负样本的边界分数值（自己设定）
    linenum = 0
    fp = open(input_file)
    for line in fp:
        if linenum == 0:
            linenum += 1
            continue
        item = line.strip().split(',')
        if len(item) < 4:
            continue
        userid, itemid, rating = item[0], item[1], item[2]
        if userid not in pos_dict:
            pos_dict[userid] = []
        if userid not in neg_dict:
            neg_dict[userid] = []
        if float(rating) >= score_thr:
            pos_dict[userid].append((itemid, 1))
        else:
            score = score_dict.get(itemid, 0)
            neg_dict[userid].append((itemid, score))
    fp.close()
    for userid in pos_dict:
        data_num = min(len(pos_dict[userid]), len(neg_dict.get(userid, [])))
        if data_num > 0:
            train_data += [(userid, zuhe[0], zuhe[1]) for zuhe in pos_dict[userid]]
        else:
            continue
        sorted_neg_list = sorted(neg_dict[userid], key=lambda element: element[1], reverse=True)[:data_num]
        train_data += [(userid, zuhe[0], 0) for zuhe in sorted_neg_list]
    return train_data


if __name__ == "__main__":
    # item_info = get_item_info("../../data/movies/movies.csv")
    # # print (item_info)../../data/movies/ratings.csv
    # print(len(item_info))
    # print(item_info['1'])
    # print(item_info['3'])

    # score_dict = get_ave_score("../../data/movies/ratings.csv")
    # print(len(score_dict))
    # print(score_dict['31'])

    # 测试 get_train_data
    train_data = get_train_data("../../data/movies/ratings.csv")
    print(len(train_data))  # 原数据100005条，结果为84735条--负采样筛选了一些数据
    print(train_data[:20])
    pass
