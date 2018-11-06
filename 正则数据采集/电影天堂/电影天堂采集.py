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
with open('html/dytt01.html', 'rb') as news:
    # 读取文件所有信息
    content = news.read().decode('utf-8')
    # print(content)

    # 2. 正则筛选：第一次筛选每一条数据
    reg1 = r'<table class="tbspan" style="margin-top:6px" width="100%" cellspacing="0" cellpadding="0" border="0">.*?</table>'
    _content = re.findall(reg1, content, re.S)
    # print(_content)
    print(len(_content))

    # 3. 筛选具体数据
    for info in _content:
        print('##'*10)
        print('##'*10)
        print('##'*10)
        # print(info)

        name_url_reg = r'<a href="(.*?)".*?>(.*?)</a>'
        name_url = re.findall(name_url_reg, info, re.S)
        print(len(name_url))
        # 电影名字
        movie_name = name_url[0][1]
        # 电影链接
        movie_url = 'https://www.dy2018.com' + name_url[0][0]
        # print(movie_name)
        # print(movie_url)
        # print(name_url)
        moviedate_reg = r'<font.*?>日期：(.*?)\s+点击：(.*?)</font>'
        moviedate_click = re.findall(moviedate_reg, info)
        # 电影发布时间
        movie_date = moviedate_click[0][0].strip()
        # 电影点击量
        movie_click = moviedate_click[0][1].strip()
        # 电影信息
        movie_info_reg = r'<td colspan="2" style="padding-left:3px">(.*?)</td>'
        movie_info = re.findall(movie_info_reg, info)[0]
        movie_info = movie_info.replace('　　', '')
        movie_info = movie_info.replace('　', ':')
        movie_info = movie_info.replace('◎', '  ')
        movie_info = movie_info.strip()
        # print('  ')
        # print(movie_info)
        # print('电影名字：', movie_name)
        # print('电影链接：', movie_url)
        # print('发布时间：', movie_date)
        # print('点击量：', movie_click)
        # print('电影信息：', movie_info)
        arg = (movie_name, movie_url, movie_date, movie_date,
               movie_date, movie_click, movie_info,
               datetime.datetime.now())

        print(arg)
        # 入库
        # print('dfdfdfdfd')
        # put_data()
        # print('dfdfdfd')


