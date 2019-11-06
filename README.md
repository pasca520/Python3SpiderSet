![](https://img.shields.io/badge/language-Python3.7-orange.svg)

# Python3SpiderSet
## 本文目录

- 一、内容社区
    - 1.知乎
        - [知乎图片](https://github.com/pasca520/Python3SpiderSet#%E7%9F%A5%E4%B9%8E%E5%9B%BE%E7%89%87)
        - 知乎用户信息
    - 2.豆瓣
        - [豆瓣电影排行榜](https://github.com/pasca520/Python3SpiderSet#%E8%B1%86%E7%93%A3%E7%94%B5%E5%BD%B1%E6%8E%92%E8%A1%8C%E6%A6%9C)
    - 3.猫眼
        - [猫眼电影排行榜](https://github.com/pasca520/Python3SpiderSet#3-%E7%8C%AB%E7%9C%BC)

- 二、购物网站
    - 1. 淘宝商品
    - 2. 京东商品

- 三、视频网站
    - 1. B站
    - 2. 抖音

- 四、新闻网站
  - 头条

- 五、房源
  - 1. 安居客
  - 2. 自如
  - 3. 58同城
  - 4. 贝壳找房

- 六、招聘信息
  - 1. IT桔子
  - 2. Boss 直聘
  - 3. 前程无忧

- 七、企业服务
  - 1. IT桔子
  - 2. 天眼查


- 八、最爱
  - 1. 大众点评
  - 2. 12306

## 前言
关于整理日常练习的一些爬虫小练习，可用作学习使用。

项目集对爬取和解析模块分类，简单分类主要以下几点：

|  | 简单 | 中等 | 进阶 |
| --- | --- | --- | --- |
| 爬取模块 | request |selenium|  scrapy|
| 解析模块 |xpath、ajax的json 接口 | css 选择器（BeautifulSoup等等） |  正则表达式re|
| 存储模块 | 文件（txt、csv 等等） | 云存储 | SQL |




## 爬虫练手项目集
## 一、内容社区
### 1. 知乎
#### 知乎图片
知乎上有很多钓鱼贴，也成功的钓上了很多鱼，你懂的~~~
这里简单的爬些图片分析，仅供联系使用：
| 示例 | python 库 | 
| --- | --- | 
| 爬取模块 | request | 
| 解析模块 | re |
|存储类型|存储图片到本地&七牛云存储|


参考知乎文章（回答数平均3k以上）：
- [女生素颜能漂亮到什么程度？ 
](https://www.zhihu.com/question/305888519)
- [平常人可以漂亮到什么程度？](https://www.zhihu.com/question/50426133)
- [你见过最漂亮的女生长什么样？](https://www.zhihu.com/question/34243513)
- [拥有一双大长腿是怎样的体验？](https://www.zhihu.com/question/285321190)
- [身材好是一种怎样的体验？](https://www.zhihu.com/question/26037846)
- [女生什么样的身材算是好身材？](https://www.zhihu.com/question/333026642)

接口返回的 json 数据 content 模块中，包含图片的有四个参数，被包含在
```
<figure>
 <noscript>
 <img src='用户ID水印图片' data-default-watermark-src='知乎 logo水印图片' data-original='用户ID水印图片'/>
  </noscript>
<img src=继承  data-default-watermark-src='知乎 logo水印图片' data-original='用户ID水印图片'/>
</figure>
```
分别是「img src、data-default-watermark-src、data-original、data-actualsrc」。
其中noscript标签是某些浏览器把Javascript禁用了才生效的，默认不生效。

**不足：**
- 因为仅仅学习使用，所以只开单线程模式，未开启多线程加速
- 对于错误异常未能很好的处理，我运行时没遇到


#### 知乎用户信息

### 2. 豆瓣
####  豆瓣电影排行榜
| 示例 | python 库 | 
| --- | --- | 
| 爬取模块 | request | 
| 解析模块 | BeautifulSoup |
|存储类型|list（方便存入数据库）|

![](http://blog.pasca.top/2019-11-01-15725793256187.jpg)
![](http://blog.pasca.top/2019-11-01-15726140784017.jpg)


    
### 3. 猫眼
#### 猫眼电影排行榜
    
| 示例 | python 库 | 
| --- | --- | 
| 爬取模块 | request | 
| 解析模块 | xpath |
|存储类型|文件（txt）|

![](http://blog.pasca.top/2019-11-01-15726233862181.jpg)

[代码链接](https://github.com/pasca520/Python3SpiderSet/blob/master/maoYan_rank_spider.py)

## 二、购物网站
### 1. 淘宝商品
### 2. 京东商品

## 三、视频网站
### 1. B站
### 2. 抖音

## 四、新闻网站
### 头条


##  五、房源
### 1. 安居客
### 2. 自如
### 3. 58同城
### 4. 贝壳找房


## 六、招聘信息
### 1. IT桔子
### 2. Boss 直聘
### 3. 前程无忧


## 七、企业服务
### 1. IT桔子
### 2. 天眼查


## 八、最爱
### 1. 大众点评
### 2. 12306
