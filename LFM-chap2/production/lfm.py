#!/usr/bin/env python
# encoding: utf-8
'''
@author: burette
@contact: lizhiwnebit@126.com
@file: lfm.py
@time: 2019/11/18 8:59 下午
@desc: lfm模型训练主函数
对应B站视频2.5:LFM模型训练
'''

import numpy as np
import LFM.util.read as read


def init_model(vector_len):
    """
    初始化函数，输入向量长度，返回a ndarray
    """
    return np.random.randn(vector_len)


def model_predict(user_vector, item_vector):
    """
    模型预测，返回user_vector和item_vector的距离远近，返回一个数，表示强度
    """
    res = np.dot(user_vector, item_vector) / (np.linalg.norm(user_vector) * np.linalg.norm(item_vector))  # 以cos作为相似度方式
    return res


def model_train_process():
    """
    测试lfm模型训练
    """
    train_data = read.get_train_data("../../data/movies/ratings.csv")
    user_vec, item_vec = lfm_main(train_data, 50, 0.01, 0.1, 50)
    print(user_vec['1'])
    # print(item_vec)
    # print(item_vec['1'])
    print(item_vec['2455'])
    recom_result = give_recom_result(user_vec, item_vec, "24")
    ana_recom_result(train_data, "24", recom_result)


def lfm_main(train_data, F, alpha, beta, step):
    """
    :param train_data: 训练数据
    :param F: 用户向量、item向量的长度
    :param alpha: 正则化参数
    :param bete: 学习率
    :param step: 训练步长
    :return:
    字典格式：key:itemid,value:list
            key:serid,value:list
    """
    user_vec = {}
    item_vec = {}
    for step_index in range(step):
        for data_instancce in train_data:
            userid, itemid, lable = data_instancce
            if userid not in user_vec:  # 初始化参数
                user_vec[userid] = init_model(F)
            if itemid not in item_vec:  # 初始化参数
                item_vec[itemid] = init_model(F)
        delta = lable - model_predict(user_vec[userid], item_vec[itemid])
        for index in range(F):  # 参数更新
            user_vec[userid][index] += beta * (delta * item_vec[itemid][index] - alpha * user_vec[userid][index])
            item_vec[itemid][index] += beta * (delta * user_vec[userid][index] - alpha * item_vec[itemid][index])
        beta = beta * 0.9  # 学习率进行衰减

    return user_vec, item_vec


def give_recom_result(user_vec, item_vec, userid):
    """
    传入训练好的user_vec和item_vec,以及userid，返回：a list:[(itemid,score),(itemid1,score1)]
    :param user_vec:
    :param item_vec:
    :param userid:
    :return:
    """
    # fix_num为固定的推荐结果
    fix_num = 10

    if userid not in user_vec:
        return []
    record = {}
    record_list = []
    user_vector = user_vec[userid]
    for itemid in item_vec:
        item_vector = item_vec[itemid]
        res = np.dot(user_vector, item_vector) / (np.linalg.norm(user_vector) * np.linalg.norm(item_vector))  # 采用欧式距离计算
        record[itemid] = res
    # print(record)

    # 将record（key-value）按照value从大到小排序 ，不采用原视频中operator到方式
    for zuhe in sorted(record.items(), key=lambda x: x[1], reverse=True)[:fix_num]:
        itemid = zuhe[0]
        score = round(zuhe[1], 3)
        record_list.append((itemid, score))
    return record_list


def ana_recom_result(train_data, userid, recom_list):
    """
    传入训练数据，用户id，推荐列表
    :param train_data: 展现用户对之前哪些电影感兴趣
    :param userid: 待分析用户
    :param recom_list:
    :return: 无返回，分析函数
    """
    item_info = read.get_item_info("../../data/movies/movies.csv")
    for data_instance in train_data:
        temp_userid, itemid, lable = data_instance
        if temp_userid == userid and lable == 1:  # 查看用户喜欢的item
            print(item_info[itemid])
    print("recommend result")
    for zuhe in recom_list:
        print(item_info[zuhe[0]])


if __name__ == "__main__":
    # ret = init_model(7)
    # print(ret)
    model_train_process()
