from io import BytesIO  # 字节流
import math
import logging

# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
# 重定向反解析
# from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.http import JsonResponse
# redis缓存
# from django.core.cache import cache
from django.conf import settings
# 分页器
from django.core.paginator import Paginator

from . import utils
from . import models
from . import cacheutils
from .utils import require_login


def index(request):
    '''
    博客首页
    :param request:
    :return:
    '''
    # 输出日志
    logger = logging.getLogger("django")
    logger.warning('首页开始运行了...')

    articles = cacheutils.get_articles()
    '''
    # 第二种分页：Django内置分页
    '''
    pageSize = int(request.GET.get("pageSize", settings.PAGE_SIZE))  # 每页文章数
    pageNow = int(request.GET.get("pageNow", 1))  # 当前页
    # 构建Paginator对象
    paginator = Paginator(articles, pageSize)
    page = paginator.page(pageNow)
    return render(request, "blog/index.html", {"page": page, "pageSize": pageSize})


    '''
    # 第一种分页实现，手动实现
    pageSize = int(request.GET.get("pageSize", settings.PAGE_SIZE))
    pageNow = int(request.GET.get("pageNow", 1))

    allCount = len(articles)
    pageCount = math.ceil(allCount/pageSize)
    # queryset 有延迟加载的效果
    page = articles[(pageNow - 1)*pageSize:pageNow*pageSize]
    # 构造一个循环器，目的为了页面上循环连接
    pageRange = range(1, pageCount+1)

    return render(request, "blog/index1.html", {"articles": page, "page_range": pageRange,
                                               "pageNow": pageNow, "pageSize": pageSize,
                                               "allCount": allCount, "pageCount": pageCount})

    '''


# def add_user(request):
#     return render(request, "blog/add_user.html", {})


def delete_user(request, user_id):
    '''
    删除用户
    :param request:
    :param user_id:
    :return:
    '''
    # u_id = request.GET["id"]
    user = models.User.objects.get(pk=user_id)
    user.delete()
    # users = models.User.objects.all()
    # return render(request, "blog/user_list.html", {"msg": "删除用户成功！！", "users": users})
    # 重定向
    # return HttpResponseRedirect("/blog/list_user/")
    # return redirect("/blog/list_user/")
    return redirect(reverse("blog:list_user"))


@require_login
def list_user(request):
    '''
    展示所有用户
    :param request:
    :return:
    '''
    users = models.User.objects.all()
    return render(request, "blog/user_list.html", {"users": users})


def reg(request):
    '''
    注册
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, "blog/add_user.html", {"msg": "请认真填写注册信息"})
    elif request.method == "POST":
        # 接受参数
        mycode = request.POST.get("code", None)
        check_code = request.session["check_code"]
        # 清除验证码
        del request.session["check_code"]
        if mycode == None or check_code.upper() != mycode.strip().upper():
            return render(request, "blog/add_user.html", {"msg": "验证码错误"})
        try:
            username = request.POST["username"].strip()
            password = request.POST.get("password").strip()  # .getlist()
            confirmpwd = request.POST.get("confirmpwd").strip()
            nickname = request.POST.get("nickname", None)
            avatar = request.FILES.get("avatar", 'static/img/default.png')

            # 数据校验
            if len(username) < 1:
                return render(request, "blog/add_user.html", {"msg": "用户名称不能为空！！"})
            if len(password) < 6:
                return render(request, "blog/add_user.html", {"msg": "密码长度不能小于6位！！"})
            if password != confirmpwd:
                return render(request, "blog/add_user.html", {"msg": "两次密码不一致！！"})

            # 用户名称是否重复
            if models.User.objects.filter(name=username):
                return render(request, "blog/add_user.html", {"msg": "已注册"})
            else:
                # 先对密码加密，之后在保存
                password = utils.hmac_by_md5(password)
                # 保存数据
                user = models.User(name=username, password=password, nickname=nickname, header=avatar)
                user.save()
                return render(request, "blog/login.html", {"msg": "恭喜您，注册成功！！"})
        except:
            return render(request, "blog/add_user.html", {"msg": "注册失败"})


def checkusername(request, username):
    '''
    登录ajax验证用户名是否注册
    :param request:
    :return:
    '''
    users = models.User.objects.filter(name=username)
    if len(users):
        return JsonResponse({"msg": "用户名已注册", "success": False})
    else:
        return JsonResponse({"msg": "用户名可用", "success": True})


def login(request):
    '''
    登录
    :param request:
    :return:
    '''
    if request.method == "GET":  # GET必须大写
        print("get+++++++++++++++++++++++++++++")
        response = render(request, "blog/login.html", {})
        try:
            if request.COOKIES['count']:
        # counter = int(request.COOKIES['count']) + 1
        # print("%%%%%%%%%%%%%%%%%%%")
        # print(counter)
        # response.set_cookie("count", counter)
        # print(request.COOKIES['count'])
        # if int(request.COOKIES['count']) > 3:
        #     response.set_cookie('count', 'on')
        #     print("6666666666666666666666")
        #     print(request.COOKIES['count'])
                return response
        except:
            print(")))))))))))))))))))))))))")
            response.set_cookie('count', 1)
            return response
    elif request.method == "POST":
        print("post+++++++++++++++++++++++++++++")

        if request.COOKIES['count'] == "on":
            print("#################$$$$$$$$$$$$$$$$$$$$$$$$$$$$#")
            mycode = request.POST.get("code", None)
            check_code = request.session["check_code"]
            # 清除验证码
            del request.session["check_code"]
            if mycode == None or check_code.upper() != mycode.strip().upper():
                return render(request, "blog/login.html", {"msg": "验证码错误"})

        name = request.POST["name"].strip()
        password = request.POST["password"].strip()
        try:
            # 数据校验
            if len(name) < 1:
                # print("######################")
                # print(request.COOKIES["count"])
                # request.COOKIES["count"] = count + 1
                print("######################")
                # print(request.COOKIES["count"])
                return render(request, "blog/login.html", {"msg": "用户名不能为空"})
            if len(password) < 6:
                # request.COOKIES["count"] = count + 1
                return render(request, "blog/login.html", {"msg": "密码长度不能小于6位"})
            # 用户是否存在
            user = models.User.objects.filter(name=name).first()
            if user:
                # 对用户输入的密码加密并比较
                password = utils.hmac_by_md5(password)
                if password == user.password:
                    # print('###############################')
                    # print(username.nickname)
                    request.session["loginuser"] = user

                    response = redirect(reverse("blog:index"))
                    # 记住密码
                    status = request.POST.get("status")
                    # print(status, type(status))
                    if status == '1':
                        # print('###############################')
                        response.set_cookie("loginuser", user.id, max_age=3600*24*7)
                    else:
                        response.set_cookie("loginuser", user.id)
                    # return redirect('/blog/index/', )
                    return response
                else:
                    counter = int(request.COOKIES['count']) + 1
                    # del request.COOKIES['count']  # 删除服务器COOKIES
                    if counter > 3:
                        counter = 'on'
                    # print("%%%%%%%%%%%%%%%%%%%")
                    # print(counter)
                    # print(request.COOKIES['count'])
                    request.COOKIES['count'] = counter
                    # print(request.COOKIES['count'])
                    response = render(request, "blog/login.html", {"msg": "密码错误"})
                    response.set_cookie("count", counter)
                    # 必须重新设置response中cookie值，request中的COOKIE值也要更新，否则前端页面显示的COOKIE值与浏览器存的COOKIE值不一致，为上一次的。
                    return response
            else:
                # request.COOKIES["count"] = count + 1
                return render(request, "blog/login.html", {"msg": "用户名不存在"})
        except Exception as e:
            print("++++++++++++++++++++++++++++++++++++++++")
            print(e)
            # request.COOKIES["count"] = count + 1
            return HttpResponse("<h1>登录失败</h1><a href='/blog/login/'>返回</a>")


@require_login
def logout(request):
    '''
    用户退出
    :param request:
    :return:
    '''
    try:
        del request.session['loginuser']
    except:
        pass
    finally:
        return redirect(reverse("blog:index"))


@require_login
def show(request, u_id):
    '''
    展示个人具体信息
    :param request:
    :param u_id: restful参数，URI拼接
    :return:
    '''
    print('##########################################')
    print(request.GET)
    user = models.User.objects.get(pk=u_id)
    return render(request, "blog/show.html", {"user": user})


@require_login
def update(request, u_id):
    '''
    更新用户信息
    :param request:
    :param u_id:
    :return:
    '''
    if request.method == "GET":
        user = models.User.objects.filter(id=u_id).first()
        return render(request, "blog/update.html", {"user": user})
    else:
        nickname = request.POST['nickname']
        age = request.POST['age']

        user = models.User.objects.get(pk=u_id)
        user.age = age
        user.nickname = nickname
        user.save()

        # return redirect('/blog/show/'+u_id+'/')
        return redirect(reverse('blog:show', args=(u_id, )))


###########################################################################
# 文章视图函数
def add_article(request):
    '''
    添加文章
    :param request:
    :return:
    '''
    if request.method == "GET":
        try:
            if request.session['loginuser']:
                print("##############################")
                return render(request, "blog/article_publish_markdown.html")
        except Exception as e:
            return render(request, "blog/login.html", {"msg": "发表文章请先登录"})
    else:
        title = request.POST['title']
        content = request.POST['content']
        author = request.session['loginuser']
        remark = utils.clear_html_re(content)[:50]

        # 保存文章
        article = models.Article(title=title, content=content, author=author, remark=remark)
        article.save()
        # 更新文章缓存
        cacheutils.get_articles(ischange=True)

        # return redirect(reverse("blog:show_article", kwargs={"a_id": article.id}))

        # ajax 添加文章
        return JsonResponse({"msg": "文章添加成功", "success": True})


@require_login
def delete_article(request, article_id):
    '''
    删除文章
    :param request:
    :param a_id:
    :return:
    '''
    at = models.Article.objects.get(pk=article_id)
    at.delete()
    return redirect(reverse("blog:show_p_articles", kwargs={"a_id": request.session['loginuser'].id}))


@require_login
def update_article(request, a_id):
    '''
    修改文章
    :param request:
    :param a_id:
    :return:
    '''
    print("#######################################")
    print(a_id)
    at = models.Article.objects.get(pk=a_id)
    print(at)
    print("*************************************")
    if request.method == "GET":
        # 进入修改页
        return render(request, "blog/update_article.html", {"article": at})
    else:
        # 修改
        title = request.POST['title']
        content = request.POST['content']
        remark = utils.clear_html_re(content)[:50]
        at.title = title
        at.content = content
        at.remark = remark
        at.save()
        # 更新文章缓存
        cacheutils.get_articles(ischange=True)
        return redirect(reverse("blog:show_article", kwargs={"a_id": a_id}))


def show_article(request, a_id):
    '''
    展示文章详情
    :param request:
    :param a_id:
    :return:
    '''

    at = models.Article.objects.get(pk=a_id)
    return render(request, 'blog/show_article.html', {"article": at})


def show_articles(request):
    '''
    展示所有文章
    :param request:
    :param a_id:
    :return:
    '''
    articles = cacheutils.get_articles()
    # articles = models.Article.objects.all()
    return render(request, "blog/show_articles.html", {"articles": articles})


@require_login
def show_p_articles(request, a_id):
    '''
    展示个人所有文章
    :param request:
    :param a_id:
    :return:
    '''
    # author = request.session['loginuser']
    # articles = models.Article.objects.filter(author_id=a_id)
    user = models.User.objects.get(pk=a_id)
    # print("###############################################")
    # print(user)
    # print(user.nickname)
    # print("###############################################")

    articles = user.article_set.all()  # 获取用户的所有文章
    # 获取文章的作者昵称可以用
    print("###############################################")
    # print(articles)
    # print(articles.first().title)
    print("###############################################")
    return render(request, "blog/show_p_articles.html", {"articles": articles})


# def update_article(request, a_id):
#     '''
#     展示文章详情
#     :param request:
#     :param a_id:
#     :return:
#     '''
#     if request.method == "GET":
#         at = models.Article.objects.get(pk=a_id)
#         return render(request, 'blog/update_article.html', {"article": at})
#     else:
#         title = request.POST['title']
#         content = request.POST['content']
#
#         article = models.Article.objects.get(pk=a_id)
#         article.title = title.strip()
#         article.content = content.strip()
#         article.save()
#
#         # return redirect('/blog/show/'+u_id+'/')
#         return redirect(reverse('blog:show_article', args=(a_id,)))


def code(request):
    '''
    验证码
    :param request:
    :return:
    '''
    # 在内存中开辟空间用以生成临时的图片
    f = BytesIO()
    img, mycode = utils.create_code()
    # 保存验证码信息到 session 中，方便下次表单提交时进行验证操作
    request.session['check_code'] = mycode
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())


