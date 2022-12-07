## 参考
https://github.com/dataabc/weibo-search

### 1.下载脚本
```bash
$ git clone https://github.com/dataabc/weibo-search.git
```
### 2.安装Scrapy
本程序依赖Scrapy，要想运行程序，需要安装Scrapy。如果系统中没有安装Scrapy，请根据自己的系统安装Scrapy，以Ubuntu为例，可以使用如下命令：
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

