from wordcloud import WordCloud  
import matplotlib.pyplot as plt  
import numpy as np
from PIL import Image
from matplotlib import colors

# 读数据
with open("taiwan-ciyun-comment.txt", "r", encoding='utf-8') as f:
    text = f.read()

#建立颜色数组，可更改颜色
color_list=['#4169E1','#6495ED','#87CEFA','#00BFFF','#B0E0E6',
            '#00BBFF','#00CED1','#008B8B','#48D1CC',
            '#20B2AA','#40E0D0','#00BFFF','#1E90FF','#00008B','#191970']

#调用
colormap=colors.ListedColormap(color_list)

mask = np.array(Image.open("Taiwan.png"))
wc1 = WordCloud(
    background_color="white",  # 背景为白色
    font_path='simfang.ttf',  # 使用的字体库:当前字体支持中文
    max_words=200,  # 最大显示的关键词数量
    width=1000,  # 生成词云的宽
    height=860,  # 生成词云的高
    collocations=False,  # 解决关键词重复：是否包括两个词的搭配
    colormap=colormap,  # 设置文字颜色
    mask=mask
    # stopwords=STOPWORDS, #屏蔽的内容
)
wc2 = wc1.generate(text)

plt.imshow(wc2)
plt.axis("off")
plt.savefig('Taiwan-comment.jpg', dpi=600, bbox_inches='tight')
plt.show()



