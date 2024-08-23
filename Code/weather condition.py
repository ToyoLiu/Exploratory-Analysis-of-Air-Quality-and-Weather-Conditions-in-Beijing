import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('北京空气质量及天气情况缺失版.csv')

weather_list = df['天气状况'].tolist()

# 替换文本中所有'/'为'/#'
text = ' '.join([item.replace('/', '/#') for item in weather_list])

wordcloud = WordCloud(
    font_path='C:/Windows/Fonts/msyhbd.ttc',
    background_color='white',
    max_font_size=200,
    width=1000,
    height=800
).generate(text)

plt.imshow(wordcloud)
plt.axis('off')
plt.title('Weather Status Word Cloud', fontsize=20)

plt.show()
