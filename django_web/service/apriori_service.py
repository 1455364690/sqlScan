# _*_ coding:utf-8 _*_
import datetime

from django_web.service import file_service
from django_web import models


def get_dataset(table_name, attribute_name):
    """
    测试集'ucr_iupc.PM_OFFER_REL', 'REL_OFFER_ID'
    :return:
    """
    data = []
    res = file_service.get_values_by_table_and_attribute_key(table_name, attribute_name)
    # for i in res:
    #     data.append(i[0:9])
    # print(data)
    print('res:', res)
    return res
    # return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5], [1, 2, 3, 5], [1, 2, 3, 4, 5]]


def init(data_set):
    """
    构建初始候选项集的列表，即所有候选项集只包含一个元素，
    C1是大小为1的所有候选项集的集合
    """
    C1 = []
    for transaction in data_set:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))


def get_freq_set_and_support_data(data_set, ck, min_support):
    """
    计算Ck中的项集在数据集合D(记录或者transactions)中的支持度,
    返回满足最小支持度的项集的集合，和所有项集支持度信息的字典。
    """
    support_dict_set = {}
    for tid in data_set:
        # 对于每一条transaction
        for can in ck:
            # 对于每一个候选项集can，检查是否是transaction的一部分
            # 即该候选can是否得到transaction的支持
            if can.issubset(tid):
                support_dict_set[can] = support_dict_set.get(can, 0) + 1
    data_num = float(len(data_set))
    freq_list = []
    support_data = {}
    for key in support_dict_set:
        # 每个项集的支持度
        support = support_dict_set[key] / data_num
        # 汇总支持度数据
        support_data[key] = support
        # 将满足最小支持度的项集，加入freq_list中
        if support >= min_support:
            freq_list.insert(0, key)
    return freq_list, support_data


# Aprior算法
def get_ck(lk, k):
    """
    由初始候选项集的集合Lk生成新的生成候选项集，
    k表示生成的新项集中所含有的元素个数
    """
    retList = []
    lk_len = len(lk)
    for i in range(lk_len):
        for j in range(i + 1, lk_len):
            tmp1 = list(lk[i])[: k - 2]
            tmp2 = list(lk[j])[: k - 2]
            sorted(tmp1)
            sorted(tmp2)
            if tmp1 == tmp2:
                tmp = list(lk[i] | lk[j])
                tmp.sort()
                retList.append(frozenset(tmp))
    return retList


def apriori(data_list, min_support=0.5):
    """
    计算频繁项集和支持度表
    :param data_list:
    :param min_support:
    :return:
    """
    # 构建初始候选项集C1；C1:{fset({1}),fset({2}),fset({3}),fset({4})...}
    C1 = init(data_list)
    # 将dataSet集合化，以满足scanD的格式要求D:{{'3','4','1'},{'5','3','2'}...}
    data_set = list(map(set, data_list))
    # 构建初始的频繁项集，即所有项集只有一个元素,freq_set是频繁项列表[]，support_data_set是支持度表{}
    freq_set, support_data_set = get_freq_set_and_support_data(data_set, C1, min_support)
    freq_sets = [freq_set]
    # 最初的L1中的每个项集含有一个元素，新生成的
    # 项集应该含有2个元素，所以 k=2
    k = 2
    while len(freq_sets[k - 2]) > 0:
        # 通过Lk获取Ck+1
        ck = get_ck(freq_sets[k - 2], k)
        freq_set_k, support_data_set_k = get_freq_set_and_support_data(data_set, ck, min_support)
        # 将新的项集的支持度数据加入原来的总支持度字典中
        support_data_set.update(support_data_set_k)
        # 将符合最小支持度要求的项集加入频繁项集中
        freq_sets.append(freq_set_k)
        # 新生成的项集中的元素个数应不断增加
        k += 1
    # 返回所有满足条件的频繁项集的列表，和所有候选项集的支持度信息
    # sorted(support_data_set)
    return freq_sets, support_data_set


# 规则生成与评价
def cal_confidence(freqSet, H, supportData, brl, minConf=0.7):
    """
    计算规则的可信度，返回满足最小可信度的规则。

    freqSet(frozenset):频繁项集
    H(frozenset):频繁项集中所有的元素
    supportData(dic):频繁项集中所有元素的支持度
    brl(tuple):满足可信度条件的关联规则
    minConf(float):最小可信度
    """
    prunedH = []
    for conseq in H:
        key = list(freqSet - conseq)
        # sorted(key)
        rKey = None
        for tKey in supportData:
            if len(tKey - frozenset(key)) == 0:
                rKey = tKey
        # print(supportData[freqSet - conseq], freqSet - conseq)
        conf = supportData[freqSet] / supportData[rKey]
        if conf >= minConf:
            # print(freqSet - conseq, '-->', conseq, 'conf:', conf)
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freq_set, H, support_data, brl, min_confidence=0.7):
    """
    对频繁项集中元素超过2的项集进行合并。

    freqSet(frozenset):频繁项集
    H(frozenset):频繁项集中的所有元素，即可以出现在规则右部的元素
    supportData(dict):所有项集的支持度信息
    brl(tuple):生成的规则
    """
    m = len(H[0])
    # 查看频繁项集是否大到移除大小为 m　的子集
    if len(freq_set) >= m + 1:
        cal_confidence(freq_set, H, support_data, brl, min_confidence)
        Hmp1 = get_ck(H, m + 1)
        # Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)

        # 如果不止一条规则满足要求，进一步递归合并
        if len(Hmp1) > 1:
            rulesFromConseq(freq_set, Hmp1, support_data, brl, min_confidence)


def get_confidence(freq_sets, support_data, min_confidence=0.7):
    """
    根据频繁项集和最小可信度生成规则。

    L(list):存储频繁项集
    supportData(dict):存储着所有项集（不仅仅是频繁项集）的支持度
    minConf(float):最小可信度
    """
    confidence_list = []
    for i in range(1, len(freq_sets)):
        print('run')
        for freq_set in freq_sets[i]:
            # 对于每一个频繁项集的集合freq_set
            H1 = [frozenset([item]) for item in freq_set]
            H1.sort()
            # 如果频繁项集中的元素个数大于2，需要进一步合并
            if i > 1:
                rulesFromConseq(freq_set, H1, support_data, confidence_list, min_confidence)
            else:
                cal_confidence(freq_set, H1, support_data, confidence_list, min_confidence)
    return confidence_list


def start_apriori(table_name, attribute_name):
    """
    Apriori方法计算求置信度
    :return:
    """
    data = get_dataset(table_name, attribute_name)
    # 获取频繁项集和支持度集
    freq_sets, support_data = apriori(data, 0.5)
    # 计算置信度
    confidences = get_confidence(freq_sets, support_data, min_confidence=0.3)
    # 清除数据库中原有置信度关系
    clear_confidence_rule()
    for confidence in confidences:
        frozen_rule_a = confidence[0]
        frozen_rule_b = confidence[1]
        confi_num = confidence[2]
        list_rule_a = []
        list_rule_b = []
        for i in frozen_rule_a:
            list_rule_a.append(i)
        for i in frozen_rule_b:
            list_rule_b.append(i)
        add_confidence_rule(table_name, attribute_name, list_rule_a, list_rule_b, confi_num)
    return confidences


def clear_confidence_rule():
    """
    删除数据库中所有的置信度关系
    :return:
    """
    try:
        models.confidence_rule.objects.all().delete()
        return True
    except Exception as e:
        print(e)
        return False


def add_confidence_rule(table_name, attribute_name, list_rule_a, list_rule_b, confi_num):
    """
    将置信度关系保存到数据库中
    :param table_name
    :param attribute_name
    :param list_rule_a:
    :param list_rule_b:
    :param confi_num:
    :return:
    """
    rule_a = ''
    rule_b = ''
    for i in list_rule_a:
        rule_a += ',' + i
    for i in list_rule_b:
        rule_b += ',' + i
    rule_a = rule_a[1:len(rule_a)]
    rule_b = rule_b[1:len(rule_b)]
    models.confidence_rule.objects.create(table_name=table_name, attribute_name=attribute_name, rule_a=rule_a,
                                          rule_b=rule_b, confidence=confi_num)


def get_rules(table_name, attribute_name):
    """
    从数据库中读取所有置信度关系
    :return:
    """
    return models.confidence_rule.objects.filter(table_name=table_name, attribute_name=attribute_name).values()


# start()

def task_apriori_check(file_name, table_name, attribute_name):
    """
    使用【关联规则挖掘算法求出的置信度关系】分析上传文件指定表中指定属性
    :param file_name:文件名
    :param table_name:数据库表名
    :param attribute_name:属性名
    :return:可能存在的错误及置信度数组{a:[1,0.5...],b:[1,0.5...]...}
    """
    confidences = get_rules(table_name, attribute_name)
    value_list = file_service.get_values_by_table_attribute_by_file(file_name,
                                                                    table_name,
                                                                    attribute_name)
    # 读取置信度信息，并按照置信度从大到小进行排序
    confidence_tuple_list = []
    for confidence in confidences:
        rule_a = confidence['rule_a']
        rule_b = confidence['rule_b']
        rule_a = set(rule_a.split(','))
        rule_b = set(rule_b.split(','))
        confi_num = confidence['confidence']
        confidence_tuple_list.append((rule_a, rule_b, confi_num))
    confidence_tuple_list.sort(key=lambda x: x[2], reverse=True)
    res = {}
    # 将list转成集合
    value_list = set(value_list)
    # 分析置信度规则
    for i in confidence_tuple_list:
        if i[0].issubset(value_list) and not i[1].issubset(value_list):
            for item in i[1]:
                if item not in res.keys():
                    res[item] = []
                res[item].append((i[0], i[2]))

    data = {}
    # 除去所有已在源文件中出现的值
    for i in res:
        if i not in value_list:
            data[i] = res[i]
    return data


def save_apriori_mistake(task_id, data, table_name, attribute):
    """
    保存关键属性错误
    :param task_id:
    :param data:
    :param table_name:
    :param attribute:
    :return:
    """
    for i in data:
        avg = 0
        num_up_8 = 0
        for confi in data[i]:
            avg += confi[1]
            if confi[1] > 0.8:
                num_up_8 += 1
        avg /= len(data[i])
        mistake_grade = ''
        if num_up_8 == 0:
            mistake_grade = '普通'
        elif num_up_8 <= 2:
            mistake_grade = '低危'
        elif num_up_8 <= 5:
            mistake_grade = '中危'
        else:
            mistake_grade = '高危'
        if avg >= 0.8:
            mistake_grade = '高危'
        curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        models.mistake.objects.create(task_id=task_id, mistake_type='关键属性错误', mistake_grade=mistake_grade,
                                      mistake_detail=table_name, find_time=curr_time, method=avg,
                                      extends=str(data[i]), similar_files=attribute, error_lines=i)
