import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取数据
df = pd.read_csv('北京空气质量及天气情况缺失版.csv')

# 拆分气温属性
df['气温'] = df['气温'].str.split('/')

df['temp_max'] = df['气温'].str[0]
df['temp_min'] = df['气温'].str[1]
df['temp_min'] = df['temp_min'].str[:-1]
df['temp_max'] = df['temp_max'].str[:-1]
df['temp_max'] = df['temp_max'].astype(float)
df['temp_min'] = df['temp_min'].astype(float)

# 日期格式转换
df['日期'] = pd.to_datetime(df['日期'])

# 在同一张图中画出最高、最低温度变化曲线
plt.plot(df['日期'], df['temp_max'], '-', color='orange', label="Highest Temperature")
plt.plot(df['日期'], df['temp_min'], '-', color='blue', label="Lowest Temperature")
plt.legend()
plt.yticks(np.arange(-5, 45, 5))
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()

# 绘制箱线图
plt.boxplot(df['temp_max'])
plt.ylim(0, 100)  # 设定y轴上限为100°C
plt.title('Boxplot of Highest Temperature')
plt.ylabel('Temperature (°C)')
plt.show()
