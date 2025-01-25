import os
import pandas as pd

# 定义文件夹路径
combined_df = pd.DataFrame()
folder_path = r'C:\Users\ASUS\Desktop\MCM\finish\medal_count_of_each_country'  # 替换为你的文件夹路径
# 初始化一个空的 DataFrame 用于存储所有数据
# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    # 检查文件是否为 Excel 文件
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, file_name)
        # 读取 Excel 文件
        df = pd.read_excel(file_path)
        # 将读取的数据拼合到 combined_df 中
        combined_df = pd.concat([combined_df, df], ignore_index=True)
# 将拼合后的数据保存到一个新的 Excel 文件中
output_file = 'combined_excel_files.xlsx'
combined_df.to_excel(output_file, index=False)
print(f"所有 Excel 文件已拼合并保存到 {output_file}")