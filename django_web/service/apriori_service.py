# _*_ coding:utf-8 _*_

from django_web.service import file_service


def get_dataset():
    """
    测试集
    :return:
    """
    data = []
    res = file_service.get_values_by_table_and_attribute_key('ucr_iupc.PM_OFFER_REL', 'REL_OFFER_ID')
    # for i in res:
    #     data.append(i[0:9])
    # print(data)
    print(res)
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
        # print('fre', freqSet)
        # print('con', conseq)
        # print('sup', supportData)
        # a = supportData[freqSet]
        # print(supportData[freqSet], freqSet)
        # b = supportData[freqSet - conseq]
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


def start():
    data = get_dataset()
    # for i in range(len(data)):
    #     for j in range(len(data[i])):
    #         data[i][j] = str(data[i][j])
    # 获取频繁项集和支持度集
    freq_sets, support_data = apriori(data, 0.5)
    # 计算置信度
    confidence = get_confidence(freq_sets, support_data, min_confidence=0.3)
    for i in confidence:
        print(i)
        for j in i:
            print(j)
    # print(confidence)
    return confidence
    # print('频繁项集: {}'.format(L))
    # print('所有候选项集的支持度信息: {}'.format(supportData))
    # print('rules: {}'.format(rules))

# start()
