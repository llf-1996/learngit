import os
import random, string
import hashlib
import hmac
import logging
import re

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.shortcuts import render

# from django.conf import settings
from mysite import settings


def clear_html_re(content):
    '''
    正则清除HTML标签
    :param content:
    :return:
    '''
    s_content = re.sub(r"</?(.+?)>", "", content)
    s_content = re.sub(r"&nbsp;", "", s_content)
    logging.warning(s_content)
    return s_content


def require_login(fu):
    '''
    判断用户登录的装饰器
    :param fu:
    :return:
    '''
    def inner(request, *args, **kwargs):
        if request.session.has_key("loginuser"):
            logging.warning("该用户已经登录")
            return fu(request, *args, **kwargs)
        else:
            logging.warning("请先登录")
            return render(request, "blog/login.html", {"msg": "请先登录"})
    return inner


def getRandomChar(count=4):
    '''
    # 生成4个随机字符串
    :param count:
    :return:
    '''
    # string 模块包含各种字符串，以下为小写字母加数字
    ran = string.ascii_lowercase + string.ascii_uppercase + string.digits
    char = ''
    for i in range(count):
        char += random.choice(ran)
    return char


def getRandomColor():
    '''
    # 返回一个随机的 RGB 颜色, 红绿蓝，0——255（由暗到亮）
    :return:
    '''
    return (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))


def create_code():
    '''
    # 创建图片
    :return:
    '''
    # 创建图片，      模式，大小，背景色
    img = Image.new('RGB', (120, 30), (255, 255, 255))
    # 创建画布
    draw = ImageDraw.Draw(img)
    # 设置字体
    font = ImageFont.truetype('arial.ttf', 25)
    code = getRandomChar()
    # 将生成的字符画在画布上
    for t in range(4):
        # 位置、元素、元素颜色、字体
        draw.text((30 * t + 5, 1), code[t], getRandomColor(), font)
    # 生成干扰点
    for _ in range(random.randint(0, 50)):
        # 位置，颜色
        draw.point((random.randint(0, 120), random.randint(0, 30)), fill=getRandomColor())

    # 使用模糊滤镜使图片模糊
    img = img.filter(ImageFilter.BLUR)
    # 保存
    # print(code)
    # print(os.getcwd())
    # base = os.path.join(os.getcwd(), "checkcode")
    # img.save("checkcode/" + ''.join(code)+'.jpg', 'jpeg')
    return img, code


# hash加密
def hash_by_md5(pwd):
    md5 = hashlib.md5(pwd.encode("utf-8"))
    md5.update(settings.MD5_SALT.encode("utf-8"))
    return md5.hexdigest()


# hash加密，这种方法使用了对称加密和hash，安全性更高
def hmac_by_md5(pwd):
    # 参数：加密字符、盐值、加密方式
    return hmac.new(pwd.encode('utf-8'), settings.MD5_SALT.encode("utf-8"), "MD5").hexdigest()


if __name__ == '__main__':
    # print(getRandomChar())
    print(create_code())
