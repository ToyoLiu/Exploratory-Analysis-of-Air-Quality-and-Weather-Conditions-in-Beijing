import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 导入数据
df = pd.read_csv('北京空气质量及天气情况缺失版.csv')

# 处理列名编码
df.columns = df.columns.str.encode('utf-8').str.decode('utf-8')

# 设置支持中文的字体
font_chinese = {'family': 'SimSun',
                'weight': 'bold',
                'size': 12}

# 设置支持其他字符的通用字体
font_other = {'family': 'sans-serif',
              'weight': 'bold',
              'size': 12}

plt.rc('font', **font_chinese)

# 定义缺失值表示字符串
missing_value = "#########"

# 计算每个属性缺失值个数
null_count = df.isin([missing_value]).sum()

# 计算缺失率
missing_rate = null_count / len(df)

# 绘制缺失率条形图  
sns.barplot(x=missing_rate, y=missing_rate.index)
plt.xlabel('Missing Rate')
plt.ylabel('Attributes')
plt.show()

# 输出缺失率信息
print(missing_rate)
