import pandas as pd
# 读取Excel文件
df = pd.read_excel('summerOly_medal_counts.xlsx')
# 直接使用DataFrame进行过滤
# 将DataFrame转换为字典列表
data = df.to_dict(orient='list')
# 打印结果以验证
#print(data)
# 提取关键字为'NOC'的列表
noc_list = data.get('NOC', [])
# 假设需要处理的列是 'NOC'
column_name = 'NOC'
# 去掉列中每个值的最后一个字符 '聽'
#这里是出现了乱码需要去掉
df[column_name] = df[column_name].str.rstrip('聽')
# 如果需要保存修改后的DataFrame到新的Excel文件
df.to_excel('cleaned_summerOly_medal_counts.xlsx', index=False)
df = pd.read_excel('cleaned_summerOly_medal_counts.xlsx')
# 使用set()函数将列表转换为集合
my_set = set(noc_list)
# 打印结果
print(my_set)
# 打印结果以验证
#print(noc_list)
# 使用for循环遍历集合中的每个元素
for element in my_set:
    specificvalue = element
    newdf = df[df['NOC'] == specificvalue]
    # 使用f-string构建文件名，其中包含当前元素的值
    filename = f'{element}_sheet.xlsx'
    # 将过滤后的DataFrame保存到新的Excel文件
    newdf.to_excel(filename, index=False)
