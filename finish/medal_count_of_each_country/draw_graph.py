import os
import pandas as pd
import matplotlib.pyplot as plt

# 获取当前工作目录下所有的 .xlsx 文件
file_list = [f for f in os.listdir() if f.endswith(".xlsx")]

# 循环处理每个文件
for file_name in file_list:
    try:
        # 读取 Excel 文件
        file_path = os.path.join(os.getcwd(), file_name)  # 获取文件完整路径
        df = pd.read_excel(file_path)

        # 检查是否包含 'Gold' 和 'Year' 列
        if "Gold" in df.columns and "Year" in df.columns:
            # 提取两列数据（横纵坐标调换）
            x = df["Year"]  # 将 'Year' 作为 X 轴
            y = df["Gold"]  # 将 'Gold' 作为 Y 轴

            # 从指定列中提取某个值作为标题（例如 'NOC' 列的第二行值）
            if "NOC" in df.columns:  # 假设标题值在 'NOC' 列
                title_value = df["NOC"].iloc[1]  # 获取 'NOC' 列的第二行值
            else:
                title_value = "默认标题"  # 如果 'NOC' 列不存在，使用默认标题

            # 绘制柱状图（横纵坐标调换）
            plt.figure()  # 创建一个新的图形
            plt.bar(x, y, color="g", label="Data")
            plt.xlabel("Year")  # X 轴标签
            plt.ylabel("Gold Medals")  # Y 轴标签
            plt.title(f"柱状图示例 - {title_value}")  # 使用指定列的值作为标题
            plt.legend()
            plt.grid(True)
            plt.show()  # 显示图形
        else:
            print(f"文件 {file_name} 中缺少 'Gold' 或 'Year' 列，跳过处理。")
    except Exception as e:
        print(f"处理文件 {file_name} 时出错: {e}")