# @Time     ： 2023/3/30 11:18
# @Author   ： Byz
# -*- coding: UTF-8 -*-
import re

file = r"E:\python\study\Log_sum\test_log.txt"
ip_1 = "223.73.89.192"

# 1.日志分析，计算某用户`223.73.89.192`访问次数
with open(file) as f:
    lines = f.readlines()

group_223 = []
for line in lines:
    if ip_1 in line:
        group_223.append(line)

print(f"使用'223.73.89.192'IP的用户访问了{len(group_223)}次。\n")

# 2.日志分析升级，计算所有用户的访问次数。
results = []
with open(file) as file_object:
    for line in file_object.readlines():
        # 匹配IP，\d+是重复匹配0-9的数字
        compile_rule = re.compile(r'\d+[.]\d+[.]\d+[.]\d+')
        # 使用re模块筛选行中匹配的字段，返回结果为str
        result = re.findall(compile_rule, line)
        for result in result[:1]:
            results.append(result)

calculate_result = {}
for ip in results:
    """计算每个值的数量，放在dic内"""
    if ip not in calculate_result:
        calculate_result[ip] = 1
    else:
        calculate_result[ip] += 1

for key in calculate_result.keys():
    print(f"使用'{key}'IP的用户访问了{calculate_result[key]}次。")
