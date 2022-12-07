###############################################
### 政治人物 大陆
### Political figures Mainland China

import jieba

txt = open("weibo-post.txt", "r", encoding="utf-8").read()
words=jieba.add_word('毕登')
words=jieba.add_word('蔡女士')
words=jieba.add_word('菜菜子')
words=jieba.add_word('英英')
words=jieba.add_word('菜裆菊')
words=jieba.add_word('蔡大妈')
words=jieba.add_word('蔡英文')
words=jieba.add_word('朔尔茨')
words=jieba.add_word('习主席')
words=jieba.add_word('习大大')
words=jieba.add_word('泽连斯基')
words=jieba.add_word('拉夫罗夫')
words = jieba.lcut(txt)

worddict1 = {'普京': 0, '普丁': 0, '俄总统': 0,'连斯基': 0, '泽连斯基': 0,'戏子': 0, '演员': 0, '戲子': 0, '戏精': 0, '拜登': 0,
            '毕登': 0,'白灯': 0, '白等': 0,'王毅': 0, '卡德罗夫': 0, '小卡': 0, '蔡英文': 0, '蔡女士': 0
             , '菜菜子': 0, '英英': 0,'菜裆菊': 0,'蔡大妈': 0,'朔尔茨': 0, '华春莹': 0, '华姐': 0,'特朗普': 0,'川普': 0, '习近平': 0,'习主席': 0,
             '习大大': 0,'马克': 0,'汪文斌': 0,'卢卡申科': 0,'拉夫罗夫': 0
            }

for i in words:
    if i in worddict1:
        worddict1[i] = worddict1[i] + 1
print(worddict1)


###############################################
### 政治人物台湾
### Political figures Taiwan


import jieba

txt = open("taiwan-post.txt", "r", encoding="utf-8").read()

words=jieba.add_word('澤連司機')
words=jieba.add_word('蔡英文')
words=jieba.add_word('習近平')
words=jieba.add_word('盧卡申科')
words=jieba.add_word('馮德萊恩')
words=jieba.add_word('特朗普')
words=jieba.add_word('習大大')
words=jieba.add_word('馬英九')
words=jieba.add_word('布丁狗')
words=jieba.add_word('丁皇')
words=jieba.add_word('普老大')
words=jieba.add_word('林九萬')
words=jieba.add_word(' 9萬')
words=jieba.add_word('閃尿佐')
words=jieba.add_word('林閃尿')
words=jieba.add_word('漏尿佐')
words=jieba.add_word(' 閃0')
words=jieba.add_word('蔣介石')
words=jieba.add_word('馬斯克')
words=jieba.add_word('musk')
words=jieba.add_word('老馬')
words=jieba.add_word('拉夫羅夫')
words = jieba.lcut(txt)

worddict1 = {'川普': 0, '特朗普': 0, '拜登': 0, '約翰遜': 0, '習近平': 0,  '習維尼': 0,
            '維尼': 0, '習大大': 0, '蔡英文': 0,'英文': 0 ,'蔡總統': 0, '蔡母豬': 0
             , '馬英九': 0, '澤倫斯基': 0, '演員': 0, '澤連司機': 0, '普丁': 0, '普京': 0,
             '布丁狗': 0,'布丁': 0, '普亭': 0, 'putin': 0, '丁皇': 0,'普欽': 0, '蒲亭': 0,  '普老大': 0
    , '盧卡申科': 0, '馮德萊恩': 0, '林九萬': 0, ' 9萬': 0, '林飛帆': 0, '非凡': 0, '岸田文雄': 0,
     '林昶佐': 0, '閃尿佐': 0,'林閃尿': 0,'閃尿': 0,'漏尿佐': 0,'閃0': 0,'馬斯克': 0,'王毅': 0,
             '華春瑩': 0 ,'Musk': 0,'musk': 0 ,'老馬': 0, '汪文斌': 0, '拉夫羅夫': 0}

for i in words:
    if i in worddict1:
        worddict1[i] = worddict1[i] + 1
print(worddict1)



###############################################
### 国家地区 大陆
### Country Region Mainland

import jieba

txt = open("weibo-post.txt", "r", encoding="utf-8").read()
words=jieba.add_word('灯塔国')
words=jieba.add_word('漂亮国')
words=jieba.add_word('阿霉瑞克')
words=jieba.add_word('中国')
words = jieba.add_word('拆那')
words = jieba.add_word('zg兔')
words = jieba.add_word('阿霉瑞克')
words = jieba.add_word('西巴')
words = jieba.add_word('啊三')
words = jieba.add_word('蛙蛙')


words = jieba.lcut(txt)

worddict1 = {'俄罗斯': 0,'毛子': 0,'狗熊': 0,'大毛': 0,'鹅': 0,'俄': 0,'乌克兰': 0,'二毛': 0,'乌': 0,'基辅': 0,'西乌': 0,'乌西': 0,'乌东': 0,
             '乌冬': 0,'东乌': 0,'卢甘斯克': 0,'蛇岛': 0,'美国': 0,'霉国': 0,'灯塔国': 0,'漂亮国': 0,'米国': 0,'美帝': 0,'老美': 0,
             '阿霉瑞克': 0,'丑国': 0,'中国 ': 0,'祖国': 0,'大陆': 0,'拆那': 0,'zg兔': 0,'种花': 0,'华夏': 0,'中华': 0,'🐰': 0,'台湾': 0,
             '日本': 0,'韩国': 0,'棒子': 0,'西巴': 0,'泡菜': 0,'印度': 0,'阿三': 0,'啊三': 0,'三哥': 0,'欧洲': 0,'欧美': 0,'欧盟': 0,
             '北约': 0,'车臣': 0,'白俄罗斯': 0,'白俄': 0,'三毛': 0,'蒙古': 0,'波兰': 0,'香港': 0,'立陶宛': 0,'苏联': 0,'前苏联': 0,'苏修': 0,'德国': 0,'土耳其': 0,'阿塞拜疆': 0,'荷兰': 0,'英国': 0,'法国': 0,
             '台湾': 0, '湾湾': 0, '蛙': 0, '🐸': 0, '蛙蛙': 0, '台蛙': 0, '弯弯': 0, '青蛙': 0, '呆湾': 0, '蛙岛': 0,
            '1450': 0, '对岸': 0, '对面': 0}

for i in words:
    if i in worddict1:
        worddict1[i] = worddict1[i] + 1
print(worddict1)

###############################################
### 国家地区 大陆
### Country Region Taiwan



import jieba

txt = open("taiwan-post.txt", "r", encoding="utf-8").read()
words = jieba.add_word('老毛子')
words = jieba.add_word('歐洲議會')
words = jieba.add_word('白俄羅斯')
words = jieba.add_word('克里米亞')
words = jieba.add_word('某土')
words = jieba.add_word('支支')
words = jieba.lcut(txt)

worddict = {'美國': 0,'歐美': 0,'美帝': 0,'台灣': 0,'鬼島': 0,'大中華民國': 0,'日本': 0,'俄羅斯': 0,'俄國': 0,'俄': 0,'老毛子': 0,
             '鵝羅斯': 0,'俄爹': 0,'鵝爹': 0,'ROC': 0,'烏克蘭': 0,'烏': 0,'烏東': 0,'烏西': 0,'烏國': 0,
             '歐洲': 0,'歐美': 0,'北約': 0,'歐盟': 0,'歐洲議會': 0,'波蘭': 0,'捷克': 0,'白俄羅斯': 0,'白羅斯': 0,
             '白俄': 0,'克里米亞': 0,'蘇聯': 0,'英國': 0,'基輔': 0,'莫斯科': 0,'東歐': 0,'蛇島': 0,'法國': 0,'德法': 0,
                 '土耳其': 0,'某土': 0,'德國': 0,'愛沙尼亞': 0,'芬蘭': 0,'車臣': 0,'莫斯科': 0,'阿富汗': 0,
             '中華': 0, '大陸': 0, '對岸': 0, '中國': 0,  '支那': 0, 'china': 0,  '祖國': 0}

for i in words:
    if i in worddict:
        worddict[i] = worddict[i] + 1
print(worddict)
'''
