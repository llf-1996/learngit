import re
import pymysql
import datetime

# 定义数据库连接信息
HOST = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = '123456'
DATABASE = '正则采集'
CHARSET = 'utf8'


def put_data(url, title):
    '''
    数据入库
    :param url:
    :param title:
    :return:
    '''
    # 创建连接对象
    conn = pymysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        charset=CHARSET
    )

    # 获取游标对象
    my_cursor = conn.cursor()
    i_sql = 'insert into sina(url,title,collect_time) values(%s, %s, %s)'
    arg = (url, title, datetime.datetime.now())
    try:
        res = my_cursor.execute(i_sql, arg)
        print(res)
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()


# 读取存储到文件中的数据
with open('taobao/taobo01.html', 'rb') as goods:
    # 读取文件所有信息
    content = goods.read().decode('utf-8')
    # print(content)

    # 2. 正则筛选：第一次筛选所有需要的每一条数据
    reg1 = r'<div class="ctx-box.*?<div class="row row-3 g-clearfix">'
    _content = re.findall(reg1, content, re.S)
    # print(_content)
    print(len(_content))

    # 匹配名称和价格
    for good in _content:
        # print(type(good))
        # good = good
        reg2 = r'trace-price="(.*?)".*?<span class="baoyou-intitle icon-service-free"></span>\s*(.*?)\s*</a>'
        res = re.findall(reg2, good, re.S)
        # print(res)
        if res:
            price = res[0][0]
            name = res[0][1]
            # 清洗
            name = name.replace('<span class="H">', '')
            name = name.replace('</span>', '')
            # print(name)
        # 输出商品名称和价格
        print('=='*20)
        print("名称：", name)
        print("价格:", price)
        print(end='\n\n')



'''
    # 3. 匹配新闻链接和标题
    _content = str(_content)
    reg2 = r'<h2.*?href="(.*?)".*?>(.*?)</a>.*?</h2>'
    __content = re.findall(reg2, _content)
    # print(__content)
    for new in __content:
        url = new[0]
        title = new[1]
        # if url.startswith('http') and url.endswith('shtml'):
        print(url, title)
        # 入库
        print('dfdfdfdfd')
        put_data(url, title)
        print('dfdfdfd')
'''

