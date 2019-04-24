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
    info = {'错误名称': mistake_name, '错误级别': mistake_grade, '错误类型': mistake_type, '错误描述': mistake_description,
            '详细信息': mistake_detail, '解决方案': method}
    return info


def generator_apriori_report(tmp_mistake, tmp_task):
    mistake_name = tmp_task['file_name'][21:]
    mistake_grade = tmp_mistake['mistake_grade']
    mistake_type = '关键属性错误'
    mistake_description = ''
    mistake_detail = tmp_mistake['mistake_detail']
    method = tmp_mistake['method']
    pass
