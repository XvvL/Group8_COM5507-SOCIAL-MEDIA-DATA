#### Word frequency-Mainland-post

import jieba

txt = open("weibo-post.txt", "r", encoding="utf-8").read()

words = jieba.lcut(txt)
excludes = {"视频","微博","##","我们","时间","表示","没有","一个","自己","就是","已经",
            "他们","24","关注","开始","现在","可能","不会","什么","进行","不是","发布","报道",
            "可以","这个","目前","希望","提供","链接","宣布","如果","网页","最新进展","准备","消息",
            "地区","不要","还是","进入","25","真的","正在","完全","特别","时候","27","情况","发生",
            "举行","通过","今天","继续","看到","所有","因为","要求","28","影响","任何","这些","知道","乌克兰","俄罗斯","俄乌"}

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

