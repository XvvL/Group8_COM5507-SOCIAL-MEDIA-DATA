import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'cookie': 'SCF=Ag84xxWVv1VYGdzyDd0Cv-vi2RFrKcmJh0NXNDj15zPw1xVovYcTWKaVFr4naRSawg_PQLzjpoKWZTJJAYeletU.; SSOLoginState=1669314951; SUB=_2A25Oj38xDeRhGeNI4lEW9y_OyDWIHXVqcAF5rDV6PUJbkdCOLVqlkW1NSAFUB5Nf1J5CrniNONL-KuH6WyAibl1L; __bid_n=184d738456db21e1b24207; _T_WM=82554529382; MLOGIN=1; M_WEIBOCN_PARAMS=luicode=20000174; WEIBOCN_FROM=1110106030'}

content_list = []

#Crawl Comments, get wbid, comment_content and comment_time
def get_contents_from_page(url):
    r = requests.get(url, headers=headers)  # Use cookie to deal with login issues
    r.encoding = 'utf-8'  # Deal with coding issues
    soup = BeautifulSoup(r.text, 'html.parser')  

    contents = soup.select("div[id^='C_']")  # All comments are in the div that id starts with 'C_ '
    count = 0
    for content in contents:
        temp = {
            'wbid': content['id'].split("_")[1],
            'comment_content': content.find("span", class_="ctt").text,
            'comment_time': content.find("span", class_="ct").text
        }
        content_list.append(temp)
        count += 1
        if count % 40 == 0:
            time.sleep(2)
    

    # print(content_list)
    df = pd.DataFrame(content_list)
    df.to_csv('weibo_comment.csv', mode='w', sep=',', header=False, index=False, encoding="utf_8_sig")  # Save to csv file
   

# Read xlsx file containing target URLs
def getIdMidList():
    comment = pd.read_excel("./TOP50热搜词条.xlsx") 

    result = []
    
    for i in range(0, len(comment)):
        assert(type(comment.iloc[i, 5]) == str) # Locate the sixth column of each line in this file
        result.append(comment.iloc[i, 5])  

    return result

# Splice out the URLs of the target posts one-by-one
def get_contents(page,start=1): # page: The number of pages we want to crawl, start: Crawl from the first page by default
    post_links = getIdMidList()

    for j, idmid in enumerate(post_links):
        print("the {0} comment, current idmid:{1}".format(j, idmid))

        for current_page in range(start,page+1): 
            print(current_page) 
            url = 'https://weibo.cn/%s?page=%d' % (idmid,current_page) # Replace the ids and mids of different posts and the number of pages of comments
            get_contents_from_page(url)
        time.sleep(1)



get_contents(50)
# Only up to 50 pages of comment content can be crawled, beyond 50 pages will be anti-crawled