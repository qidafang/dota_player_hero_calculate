#dota_player_hero_calculate

一个dota玩家与英雄契合度的计算器（[查看效果](http://page.zidafone.com/demos/dota-player/)），包括两部分代码：

* python的scrapy爬虫，总体思路是page->model->result，从网页中提取数据，组成有意义的数据结构，再拿这数据结构做点什么。

 在这个项目中，爬虫的用处是从[游久网dota数据库](http://db.dota.uuu9.com/)上抓取dota英雄和物品的数据和照片存到本地磁盘，数据存为json格式，方便在网页应用中直接使用。
 
* 网页应用，使用dota英雄数据、自己编写的小伙伴们的特征数据、自己编写的契合度计算公式，来计算对每个小伙伴来说最契合他的英雄。

 算法主要用到的英雄数据是【英雄标签】和【英雄事务评分】，前者说明了该英雄是近战还是远程，主属性是什么，是否能打辅助、Gank、后期等，
 后者则是对该英雄在Dps、Gank、Support等方面的能力的打分。
 
 这两个数据都来自网络，抓取到本地之后做了一些调整，例如将原来的“眩晕”“控制”两个标签改为了“小控”“小团控”“团控”三个标签，“后期”标签变为“后期”“大后期”两个标签，增加了“不稳定”“多线”“特殊”等特点，
 这让计算出的契合度更准确了一点，当然这也远远不是尽善尽美，例如同样是减速，冰女和暗牧的减速当然不同，但还没做更进一步的细分。
 
 另外，对英雄的标签也进行了一些修改和补充，这个工作也还没做完。
 
 我都是边计算契合度，边发现需要改的地方，改的目的就是使计算出的结果与实际情况相符，但又不是硬去凑这个数字。
 
 
 
##说说技术吧

只有爬虫值得一说，网页那部分只是做实验和玩儿的，没太多可说，算法自行参考代码就好。

scrapy爬虫，非常强大，基本的需求都覆盖到了，逻辑流程也已经定义好了，只需要程序员在特定的点编写特定角色组件的定义代码。
这种方式很熟悉，每个框架都是这么玩的，控制流是定义好的，而且在它的手里，只有涉及业务的地方需要程序员给出自己的实现。

这个[中文文档](http://scrapy-chs.readthedocs.org/zh_CN/latest/index.html)还是不错的，跟着其中的教程写helloworld，跑通了之后一点点改你的helloworld，遇到困难的地方就查文档，或者百度一下。

关键类：scrapy爬虫类，item模型类，pipeline处理器类。

* 爬虫组件从指定的url获取html字符串，并解析dom，从中采集信息，构造item对象
* 框架将构造好的item对象交给处理器组件，处理器组件根据item对象内容，进行处理

在本例中就是：

1. 爬虫从dota网站抓取html字符串，解析dom获得英雄的名称、图片路径、英雄详细页面url，以及物品的名称、图片路径
2. 爬虫又从英雄详细页面抓取html字符串，解析dom获得英雄的标签和各种数据
3. 每个英雄的名称、图片路径、标签、各种数据构成英雄模型对象
4. 每个物品的名称、图片路径构成物品模型对象
5. 保存图片处理器将英雄图片和物品图片存到本地磁盘，并根据英雄名称、物品名称，进行重命名（重命名之前是无意义的名称）
6. 保存英雄数据处理器将英雄数据存到本地磁盘的一个文本文件中，并组成json格式
7 保存物品数据处理器将物品数据存到本地磁盘的一个文本文件中，并组成json格式

显然前2步是抓取和解析，其后两步是做成模型对象，最后三步是处理模型对象。
顺序非常清楚。

由于我python不熟，都是边写代码边查，基本语法，库的使用，可能有的地方写得比较蠢，请不要在意这些细节。



##英雄数据的格式

        {
          "blue_add": 1.75, //智力成长（蓝色的是智力……）
          "gank": 7.2, //gank能力评分
          "speed": 315, //初始速度
          "id": "132", //英雄id
          "blue": 19, //初始智力
          "armor": 7.22, //初始护甲
          "excute_after": 0.51, //施法后摇
          "support": 5.1, //support能力评分
          "green_add": 3.2, //敏捷成长
          "attack_after": 0.6, //攻击后摇
          "ballistic": 0, //弹道速度
          "war": 8.1, //团战能力评分
          "red": 15, //初始力量（红色）
          "tags": "敏捷,近战,后期,减速",//标签们 
          "hp": 435, //初始生命
          "attack_before": 0.3,//攻击前摇 
          "attack_max": 54, //初始攻击上限
          "name": "恐怖利刃", //英雄名称
          "dps": 8.9, //dps能力评分
          "meat": 6.0, //肉盾能力评分（meat哈哈）
          "attack_min": 48, //初始攻击下限
          "red_add": 1.9, //力量成长
          "excute_before": 0.5, //施法前摇
          "range": 128, //攻击距离
          "green": 22, //初始敏捷（绿色）
          "mp": 247, //初始魔法
          "push": 8.5//push能力评分
        }

（英语水平见笑啦）



##采用node-webkit开发的json编辑器

为了方便地编辑英雄和玩家数据，开发了个小程序，具体见[这篇博文](http://427studio.net/blog/1/254)。



##从11平台获取数据进行分析

具体见[这篇博文](http://427studio.net/blog/1/255)。分析结果[看这里](http://page.zidafone.com/demos/dota-player/number.html)。
