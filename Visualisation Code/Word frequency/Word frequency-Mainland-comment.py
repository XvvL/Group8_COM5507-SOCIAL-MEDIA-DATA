#### Word frequency-Mainland-comment

import jieba

txt = open("weibo-comment.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
excludes = {"我们","就是","他们","一个","不是","自己","现在","什么","没有","不会","知道","一样","如果",
            "怎么","还是","这个","可以","可能","时候","觉得","这么","看看","已经","因为",
            "应该","这样","不能","所以","真的","但是","你们","看到","不要","是不是","只是","这些","然后","还有",
            "直接","一定","一直","而且","一下","赶紧","需要","咱们","那么","的话","肯定","以为","以后",
            "为什么","这种","出来","今天","起来","只有","很多","那个","那个","那些","它们","回复","哈哈哈","人家",
            "哈哈哈哈","别人","评论","微博","为了","开始","哈哈哈哈","多少","真是","之前","这是","确实","大家","感觉",
            "意思","只能","要是","不想","我国","一点","台湾","湾湾","弯弯","台湾人","两个","1450","天天","台湾省","任何","情况",
            "只要","最后","当然","甚至","大陆","中国","国内","乌克兰","俄罗斯","俄乌"}
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == " " or word == "":
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
