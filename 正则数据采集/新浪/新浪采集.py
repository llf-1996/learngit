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
with open('html/sina01.html', 'rb') as news:
    # 读取文件所有信息
    content = news.read().decode('utf-8')
    # print(content)

    # 2. 正则筛选：第一次筛选所有需要的数据
    reg1 = r'id="feedCardContent".*?>.*?<div class="feed-card-loading'
    _content = re.findall(reg1, content)
    print(_content)
    # print(len(_content))

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
        # print('dfdfdfdfd')
        put_data(url, title)
        # print('dfdfdfd')

