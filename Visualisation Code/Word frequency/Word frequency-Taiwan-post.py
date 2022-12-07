### Word frequency-Taiwan-post

import jieba

txt = open("taiwan-post.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
excludes = {"--","http","com","imgur","jpg","02","from","on","https","Sent","可以","就是",
            "我們","現在","他們","自己","不是","什麼","如果","一個","真的","這樣","還是","可能",
            "所以","因為","不會","怎麼","看到","應該","這個","不要","my","www","是不是",
            "直接","目前","2022","一樣","已經","沒有","只是","今天","news","一堆","-----","24","這些","JPTT",
            "但是","一直","有人","還有","...","大家","這種","一下","很多","希望","03","根本","不過",
            "其實","不能","這是","不可","表示","知道","這次","其他","提供","甚至","這麼","網址","一定","開始",
            "宣布","這是","認為","覺得","原始","the","需放","iPhone","指出","25","重要","之前","那麼",
            "時間","標題","影片","來源","時候","結果","完整","連結","報導","內文","10","只有","27",
            "你們","發生","而且","只要","完全","好像","媒體","記者","八卦","新聞","烏克蘭","俄羅斯","俄國"}

counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "" or word == "":
        rword = ""
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(50):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

