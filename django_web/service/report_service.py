# _*_coding:utf-8_*_


def generator_collaborative_filtering_report(tmp_mistake):
    table_name = tmp_mistake['mistake_detail']
    mistake_name = ''
    mistake_grade = tmp_mistake['mistake_grade']
    mistake_type = '数据库表错误'
    mistake_description = ''
    mistake_detail = '与该套餐最相似的10个文件分别是：' + tmp_mistake['similar_files'] + '；\n' \
                     + table_name + '在：' + tmp_mistake['error_lines'] + '  等共' + tmp_mistake['extends'] + '个文件中出现'
    method = ''
    if mistake_grade == '高危':
        mistake_name = '数据库表[  ' + table_name + '  ]极有可能被遗漏'
        mistake_description = '数据库表高危错误，与该套餐最相似的10个历史套餐中，有' + tmp_mistake['extends'] + '个套餐使用到了该数据库表，而新创建的套餐未使用到。'
        method = '该错误为高危错误，极有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
    elif mistake_grade == '中危':
        mistake_name = '数据库表[  ' + table_name + '  ]很有可能被遗漏'
        mistake_description = '数据库表中危错误，与该套餐最相似的10个历史套餐中，有' + tmp_mistake['extends'] + '个套餐使用到了该数据库表，而新创建的套餐未使用到。'
        method = '该错误为中危错误，很有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
    elif mistake_grade == '低危':
        mistake_name = '数据库表[  ' + table_name + '  ]有可能被遗漏'
        mistake_description = '数据库表低危错误，与该套餐最相似的10个历史套餐中，有' + tmp_mistake['extends'] + '个套餐使用到了该数据库表，而新创建的套餐未使用到。'
        method = '该错误为低危错误，有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
    elif mistake_grade == '多余':
        mistake_name = '数据库表[  ' + table_name + '  ]有可能多余'
        mistake_description = '数据库表多余错误，与该套餐最相似的10个历史套餐中，均未使用到该数据库表，而新创建的套餐使用到了该表。'
        method = '该错误为低危错误，有可能导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
    else:
        mistake_name = '数据库表[  ' + table_name + '  ]有小概率被遗漏'
        mistake_description = '数据库表普通错误，与该套餐最相似的10个历史套餐中，有' + tmp_mistake['extends'] + '个套餐使用到了该数据库表，而新创建的套餐未使用到。'
        method = '该错误为普通错误，有小概率导致创建错误套餐，希望套餐业务员可以慎重核实该套餐是否涉及到本表，如果遗漏请尽快修补有关本数据库表的sql语句。'
    info = {'错误名称': mistake_name, '错误级别': mistake_grade, '错误类型': mistake_type, '错误描述': mistake_description,
            '详细信息': mistake_detail, '解决方案': method}
    return info


def generator_apriori_report(tmp_mistake):
    """
    生成关键属性错误报告详情
    :param tmp_mistake:
    :return:
    """
    table_name = tmp_mistake['mistake_detail']
    mistake_name = table_name + '表中的' + tmp_mistake['similar_files'] + '属性值可能存在错误'
    mistake_grade = tmp_mistake['mistake_grade']
    mistake_type = '数据库表错误'
    method = ''
    if mistake_grade == '高危':
        method = '该错误为高危错误，极有可能导致创建错误套餐，套餐业务员应尽快检查该属性值是否错误，如有错误请尽快修改。'
    elif mistake_grade == '中危':
        method = '该错误为中危错误，很有可能导致创建错误套餐，套餐业务员应尽快检查该属性值是否错误，如有错误请尽快修改。'
    elif mistake_grade == '低危':
        method = '该错误为低危错误，有可能导致创建错误套餐，套餐业务员应尽快检查该属性值是否错误，如有错误请尽快修改。'
    else:
        method = '该错误为普通错误，有小概率导致创建错误套餐，套餐业务员应尽快检查该属性值是否错误，如有错误请尽快修改。'
    mistake_description = '该属性值为' + table_name + '表中的属性' + tmp_mistake['similar_files'] + \
                          '中的值：' + tmp_mistake['error_lines'] + '，根据与该属性值相似的其他属性值分析，该数据出错的概率为：' \
                          + tmp_mistake['method'][0:5] + '。'
    mistake_detail_graph_key = ['[0,0.1]', '(0.1,0.2]', '(0.2,0.3]', '(0.3,0.4]', '(0.4,0.5]', '(0.5,0.6]',
                                '(0.6,0.7]', '(0.7,0.8]', '(0.8,0.9]', '(0.9,1]']
    mistake_detail_graph_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp_cont = tmp_mistake['extends']
    temp_cont = temp_cont.replace('}, ', '},')
    temp_cont = temp_cont.replace('\', ', '\',')
    # print()
    res = temp_cont[1:len(temp_cont)].split(', ')
    relate = {}
    for i in res:
        i = i[2:len(i) - 1]
        tmp = i.split('},')
        relate[tmp[0]] = tmp[1]
    for i in relate:
        mistake_detail_graph_value[int(float(relate[i][0:5]) * 10) - 1] += 1
        # print(float(relate[i][0:5]) * 10, int(float(relate[i][0:5]) * 10))
    rule_table = []
    for i in relate:
        temp = {'rule_a': i, 'rule_b': tmp_mistake['error_lines'], 'rule': relate[i][0: 5]}
        rule_table.append(temp)
    menu = ['已有元素', '缺少元素', '关联度']
    mistake_detail = {'graph_key': mistake_detail_graph_key, 'graph_value': mistake_detail_graph_value, 'menu': menu,
                      'table': rule_table}
    info = {'错误名称': mistake_name, '错误级别': mistake_grade, '错误类型': mistake_type, '错误描述': mistake_description,
            '详细信息': mistake_detail, '解决方案': method}
    return info
