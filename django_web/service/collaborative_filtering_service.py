# coding:utf-8
from math import *
from django_web.service import file_service
import pandas as pd


# movies = pd.read_csv(".\\recommend\\movies.csv")
# ratings = pd.read_csv(".\\recommend\\ratings.csv")  # 这里注意如果路径的中文件名开头是r，要转义。
# data = pd.merge(movies, ratings, on='movieId')  # 通过两数据框之间的movieId连接
# data[['userId', 'rating', 'movieId', 'title']].sort_values('userId').to_csv(
#     '.\\recommend\\data.csv', index=False)

# 读取文件，读取文件时加‘r’， encoding='UTF-8'
# file = open(".\\recommend\\data.csv", 'r', encoding='UTF-8')
#
# # 读取data.csv中每行中除了名字的数据
# data = {}  # 存放每位用户评论的电影和评分
# for line in file.readlines():
#     # 注意这里不是readline()
#     line = line.strip().split(',')
#     # 如果字典中没有某位用户，则使用用户ID来创建这位用户
#     if not line[0] in data.keys():
#         data[line[0]] = {line[3]: line[1]}
#     # 否则直接添加以该用户ID为key字典中
#     else:
#         data[line[0]][line[3]] = line[1]
#

# print(data)

# def Euclidean(user1, user2):
#     # 取出两位用户评论过的电影和评分
#     user1_data = data[user1]
#     user2_data = data[user2]
#     similar = 0
#     # 找到两位用户都评论过的电影，并计算欧式距离
#     for key in user1_data.keys():
#         if key in user2_data.keys():
#             # 注意，similar越大表示两者越相似
#             similar += pow(float(user1_data[key]) - float(user2_data[key]), 2)
#     # 这里返回值越小，相似度越大
#     return 1 / (1 + sqrt(similar))
#
#
# # 计算某个用户与其他用户的相似度
# def top10_similar(user_id):
#     res = []
#     for userid in data.keys():
#         # 排除与自己计算相似度
#         if not userid == user_id:
#             distance = Euclidean(user_id, userid)
#             res.append((userid, distance))
#     res.sort(key=lambda val: val[1])
#     return res[:10]
#
#
# # RES = top10_similar('1')
# # print(RES)
#
# def recommend(user):
#     # 相似度最高的用户
#     top_sim_user = top10_similar(user)[0][0]
#     # 相似度最高的用户的观影记录
#     items = data[top_sim_user]
#     recommendations = []
#     # 筛选出该用户未观看的电影并添加到列表中
#     for item in items.keys():
#         if item not in data[user].keys():
#             recommendations.append((item, items[item]))
#     recommendations.sort(key=lambda val: val[1], reverse=True)  # 按照评分排序
#     # 返回评分最高的10部电影
#     return recommendations[:10]


def get_similarity(new_tables, old_tables):
    distance = 1
    for i in new_tables:
        if i not in old_tables:
            distance += 1
    for i in old_tables:
        if i not in new_tables:
            distance += 1
    return 1 / float(distance)


def get_error_tables(new_tables, tables_times):
    res = []
    tables_in_his = {}
    for i in tables_times:
        if i not in new_tables:
            tables_in_his[i] = tables_times[i]
    for i in new_tables:
        if i not in tables_times.keys():
            tables_in_his[i] = 0
    for i in tables_in_his:
        data = {'sim': tables_in_his[i], 'table_name': i}
        if tables_in_his[i] >= 0.9:
            data['message'] = '高危'
        elif tables_in_his[i] >= 0.7:
            data['message'] = '中危'
        elif tables_in_his[i] >= 0.5:
            data['message'] = '低危'
        elif tables_in_his[i] <= 0.2:
            data['message'] = '多余'
        else:
            data['message'] = '普通'
        res.append(data)
    return res


def get_table_list(history, similar_table_key):
    table_dict = {}
    res = []
    """
    给定相似度最高几个套餐名，获取其中的包含的数据库表
    :param history:历史套餐数据
    :param similar_table_key:相似度最高的套餐的key，即套餐名
    :return:
    """
    for i in history:
        table_dict[i['name']] = i['tables']
    for i in similar_table_key:
        res.append(table_dict.get(i[0]))
    return res


def get_similar_tables_times(similar_tables_list):
    """
    获取相似套餐中所有表的出现次数
    :param similar_tables_list:
    :return:
    """
    tables_times = {}
    for tables in similar_tables_list:
        for table in tables:
            tables_times[table] = tables_times.get(table, 0) + 1
    # print(tables_times)
    return tables_times


def start(package):
    # 获取历史套餐数据
    history_map = file_service.get_history_tables()
    history = history_map['data']
    # 计算历史套餐与新套餐的相似度
    sims = []
    for his in history:
        sim = get_similarity(package['tables'], his['tables'])
        sims.append((his['name'], sim))
    # 将相似度从大到小排列
    sims.sort(key=lambda x: x[1], reverse=True)
    # 获取相似度最高的10个套餐的数据库表
    similar_tables_list = get_table_list(history, sims[:10])
    # 计算相似度最高的十个套餐中未在新套餐中出现的表出现的次数
    table_times = get_similar_tables_times(similar_tables_list)
    # 计算结果
    errors = get_error_tables(package['tables'], table_times)
    for i in errors:
        print(i)
    return errors
# Recommendations = recommend('1')
# print(Recommendations)
