import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from lxml import etree
import json


# 爬虫主体
def get_page(url, params):
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'https://maoyan.com/board',
    }
    params = (
        ('offset', params),
    )
    try:
        response = requests.get(url=url, headers=headers, params=params)
        return response
    except ReadTimeout:  # 访问超时的错误
        print('Timeout')
    except ConnectionError:  # 网络中断连接错误
        print('Connect error')
    except RequestException:  # 父类错误
        print('Error')


# 解析网页
def parse_page(html):
    tree = etree.HTML(html)
    for movie in range(1, 11):
        """
        rank : 排名
        movie_name：电影名
        key_actor：主演
        up_time：上映时间
        movie_score:评分
        """
        rank = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[%s]/i/text()' % movie)[0]
        movie_name = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[%s]/div/div/div[1]/p[1]/a/text()' % movie)[0]
        key_actor = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[%s]/div/div/div[1]/p[2]/text()' % movie)[
            0].strip()  # strip去空格
        up_time = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[%s]/div/div/div[1]/p[3]/text()' % movie)[0]
        score1 = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[%s]/div/div/div[2]/p/i[1]/text()' % movie)[0]
        score2 = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[%s]/div/div/div[2]/p/i[2]/text()' % movie)[0]
        movie_score = score1 + score2
        rankList = []
        rankList.append({
            'rank': rank,
            'movie_name': movie_name,
            'key_actor': key_actor[3:],
            'up_time': up_time[5:],
            'movie_score': movie_score
        })
        return rankList


# 写入txt
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n\n')
    f.close()

if __name__ == '__main__':
    url = 'https://maoyan.com/board/4'
    for page in range(0, 100, 10):
        html = get_page(url=url, params=page).text
        rankList = parse_page(html)
        for item in rankList:
            write_to_file(item)
