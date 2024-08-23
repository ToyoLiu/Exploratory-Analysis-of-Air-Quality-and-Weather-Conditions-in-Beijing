import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
df = pd.read_csv('北京空气质量及天气情况缺失版.csv')

# 定义属性列表
numeric_cols = ['AQI', 'PM2.5', 'PM10', 'SO2', 'NO2', 'O3_8h']
float_col = ['CO']

# 相关系数
corr = df[numeric_cols].corr()

# 单变量分布
for col in numeric_cols + float_col:

    plt.subplot(1, 2, 1)

    if col == 'CO':
        sns.distplot(df[col], bins=20)
        # 修改最大值为1
        plt.ylim(0, 1)
    else:
        sns.distplot(df[col])

    plt.title('Distribution of ' + col)

    # boxplot for CO
    if col == 'CO':
        plt.subplot(1, 2, 2)
        plt.boxplot(df[col])
        plt.title('Boxplot of CO')

    plt.show()
