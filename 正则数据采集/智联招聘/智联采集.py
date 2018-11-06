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
with open('html/zl_bj01.html', 'rb') as news:
    # 读取文件所有信息
    content = news.read().decode('utf-8')
    # print(content)

    # 2. 正则筛选：第一次筛选每一条需要的数据
    reg1 = r'<div class="clearfix">\s*<ul>.*?</ul>'
    _content = re.findall(reg1, content, re.S)
    # print(_content)
    print(len(_content))

    # 3. 筛选具体数据
    for info in _content:
        print('##'*10)
        print('##'*10)
        print('##'*10)
        # print(info)

        job_reg = r'onclick="submitLog.*?">(.*?)</a>'
        joburl_reg = r'href="(.*?)".*?submitLog'
        company_reg = r'<li class="newlist_deatil_three gsmc"><a.*?>(.*?)</a>'
        jobinfo_reg = r'<li class="newlist_deatil_two">(.*?)</li>'
        jobrequire_reg = r'<li class="newlist_deatil_last">(.*?)</li>'

        job = re.findall(job_reg, info, re.S)
        job = job[0].replace('<b>', '')
        job = job.replace('</b>', '')
        job = job.replace('&nbsp;', '')
        # print(job)

        joburl = re.findall(joburl_reg, info, re.S)
        joburl = joburl[0]
        # print(joburl)

        company = re.findall(company_reg, info, re.S)
        company = company[0].strip()
        # print(company)

        jobinfo = re.findall(jobinfo_reg, info, re.S)
        jobinfo = jobinfo[0].replace('<span>', '')
        jobinfo = jobinfo.replace('</span>', '')
        # print(jobinfo)

        jobrequire = re.findall(jobrequire_reg, info, re.S)
        jobrequire = jobrequire[0].strip()
        jobrequire = jobrequire.replace('  ', '')
        jobrequire = jobrequire.replace('<b>', '')
        jobrequire = jobrequire.replace('</b>', '')
        jobrequire = jobrequire.replace('&nbsp;', '')
        # print(jobrequire)

        print(job)  # 职位
        print(joburl)  # 链接
        print(company)  # 公司名称
        print(jobinfo)  # 职位信息
        print(jobrequire)  # 职位要求


'''
        # 入库
        # print('dfdfdfdfd')
        put_data(url, title)
        # print('dfdfdfd')
'''

