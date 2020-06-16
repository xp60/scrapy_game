# Game
这个一个 Scrapy 项目来爬取 http://www.4399.com .

## Extracted data

数据格式

    {
        'name': "\u9003\u8dd1\u5427\uff01\u5c11\u5e74",
        'link': "http://news.4399.com/wmpy/"
    }





## 启动项目

您可以使用“ scrapy crawl”命令来运行：

    $ scrapy crawl 

如果要将抓取的数据保存到文件中，可以通过-o选项:
    
    $ scrapy crawl game -o quotes.json
