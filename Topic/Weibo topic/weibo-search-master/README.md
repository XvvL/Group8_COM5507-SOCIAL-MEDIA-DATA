## 参考
https://github.com/dataabc/weibo-search

### 1.下载脚本
```bash
$ git clone https://github.com/dataabc/weibo-search.git
```
### 2.安装Scrapy
本程序依赖Scrapy
```bash
$ pip install scrapy
```
### 3.安装依赖
```
$ pip install -r requirements.txt
```
### 运行程序
```bash
$ scrapy crawl search -s JOBDIR=crawls/search
```

