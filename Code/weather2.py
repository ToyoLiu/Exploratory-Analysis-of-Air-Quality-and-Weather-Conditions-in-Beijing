import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
df = pd.read_csv('北京空气质量及天气情况缺失版.csv', encoding='utf-8')

# 查看数据属性
print(df.info())

# 选择需要分析的数值型属性
num_cols = ['AQI', 'PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3_8h']

# 计算数值属性之间的相关系数
corr = df[num_cols].corr()

# 绘制热图可视化相关系数
sns.set(font_scale=1)
ax = sns.heatmap(corr, annot=True,
                 xticklabels=corr.columns,
                 yticklabels=corr.columns)

# 设置标题和标签
plt.title('Correlation Heatmap of Numeric Air Quality Attributes')
plt.xticks(rotation=90)

# 显示热图
plt.show()
