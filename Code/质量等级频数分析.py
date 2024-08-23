import matplotlib.pyplot as plt
import pandas as pd

# 加载数据
df = pd.read_csv('北京空气质量及天气情况缺失版.csv')

# 将quality_level列转换为分类型
df['质量等级'] = df['质量等级'].astype('category')

# 计数各级别出现次数
level_count = df['质量等级'].value_counts()\

# 设置支持中文的字体
font_chinese = {'family': 'SimSun',
                'weight': 'bold',
                'size': 12}

plt.rc('font', **font_chinese)

# 绘制频数柱状图
plt.bar(level_count.index, level_count)
plt.title('Number of samples in each quality level')
plt.xlabel('Quality Level')
plt.ylabel('Sample Count')

plt.show()
