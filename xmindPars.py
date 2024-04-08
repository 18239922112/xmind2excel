# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/2 16:57
@Auth ： 七月
@File ：xmindPars.py
@IDE ：PyCharm
"""
from xmindparser import xmind_to_dict
from excelGenerate import excelGen, writeExcel










def dataParWriteExcel(xmind_path,excel_path):
    '''
    数据解析并写入excel
    :return:
    '''

    xmind_data = xmind_to_dict(xmind_path)

    #需求号
    ipd_number = xmind_data[0]['topic']['topics'][0]['title'].split('#')[1]
    #模块名称
    module_name = xmind_data[0]['topic']['topics'][0]['title'].split('#')[0]
    # 创建excel文件

    excelGen(file_path=excel_path)
    for i in xmind_data[0]['topic']['topics'][0]['topics']:
        count = 0
        # 操作步骤
        op_step = ''
        #期望结果
        exp_result = ''

        #用例名称
        case_name = i['title']
        #前提条件
        preconditions = i['note']
        #优先级
        level = i['makers'][0]
        if level == 'priority-1':
            level = '紧急'
        #print(i)
        for j in i['topics']:

            if j['title'] and j['topics'][0]['title']:
                count = count + 1
                #操作步骤
                op_step += str(count) + '.' + j['title'] + '\n'
                # 期望结果
                exp_result += str(count) + '.' + j['topics'][0]['title'] + '\n'

        parms_list = [case_name,ipd_number,'功能测试',module_name,level,'是','未自动化','否',preconditions,op_step,exp_result,'成功']

        #写入数据到excel文件中
        writeExcel(file_path=excel_path,parms=parms_list)





