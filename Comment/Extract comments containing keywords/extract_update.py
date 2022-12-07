# This script is used to filter comments crawled from Weibo, 
# and the process of handling comments crawled from PTT is the same.
import pandas as pd

# Read the xlsx table file with the API provided by Pandas
comments = pd.read_excel("./weibo_comment.xlsx")

# Manually enter all keywords
kall = ["台湾", "湾湾", "蛙", "蛙蛙", "台蛙", "弯弯", "青蛙", "呆蛙", "蛙岛", "1450", "对岸", "对面",
        "解放台湾", "武统", "梧桐", "开战", "收复", "统一", "回归", "台独", "台毒", "td", "核酸", "身份证", "台湾芯片"]

# Create a dataframe object to store the filter results
df4 = pd.DataFrame(columns = comments.columns)

# The variable that store the number of selected comments
l4 = 0

# Traverse all comments and start filtering
for i in range(1, len(comments)):
    if (type(comments.iloc[i, 1]) != str):
        continue # I think this is an example of numerical processing 
								 # to avoid exceptions in the following string processing logic.
    for word in kall:
        if word in comments.iloc[i, 1]:
            df4.loc[l4] = comments.iloc[i, :]
            l4 += 1
            break # I think this break statement indirectly eliminates 
									# the duplication of comments. When a comment contains multiple keywords in the above keyword list,
									# it will only be counted once.
# Save the results in csv format, in a 'utf-8_sig' manner 
# to avoid decoding errors during display.
df4.to_csv("./comment_extract.csv", encoding='utf-8_sig')