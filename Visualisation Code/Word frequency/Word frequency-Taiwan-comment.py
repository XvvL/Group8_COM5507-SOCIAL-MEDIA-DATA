#### Word frequency-Taiwan-comment


import jieba

txt = open("taiwan-comment.txt", "r", encoding="utf-8").read()
words = jieba.add_word('今日烏克蘭')
words = jieba.add_word('明日台灣')
words = jieba.add_word('小粉紅')

excludes = {"就是","八卦","一堆","不是","就是",
            "真的","自己","一家","一樣","4%"
            ,"可以","怎麼","什麼","不會","他們",
            "不要","就是","還是","因為","一直",
            "我們","如果","一個","還在","XD","這種",
            "一定","直接","看到","根本","只有",
            "這樣","現在","不敢","所以","只有",
            "根本","看到","直接","一定","這種",
            "知道","不用","可能","沒有","整天",
            "反觀","很多","應該","看看",
            "不能","有人","覺得","...","那些",
            "之前","只能","是不是","時候","不然",
            "反正","這麼","出來",
            "早就", "那麼", "開始", "這次",
            "這些", "那邊", "已經", "只是",
            "這次", "還有", "本來","中國","支那" ,"對岸","其實","新聞","大陸","人家","繼續","大家",
            "當然","..","只會","果然","烏克蘭","俄羅斯","俄國","台灣"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word =="全世界":
        rword = "世界"
    elif word == "粉紅":
        rword = "小粉紅"


    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(50):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
