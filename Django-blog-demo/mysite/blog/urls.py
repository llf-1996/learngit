from django.conf.urls import url

from . import views

# app_name = "blog"

urlpatterns = [
    url(r"^$", views.index, name="index1"),
    url(r"^index/$", views.index, name="index"),
    # url(r"^add_user/$", views.add_user, name="add_user"),
    # RESTFUL参数，位置参数，关键字参数，参数名字和方法的形参名字一致
    # url(r"^delete_user/$", views.delete_user, name="delete_user"),
    # url(r"^(\d+)/delete_user/$", views.delete_user, name="delete_user"),
    url(r"^delete_user/(?P<user_id>\d+)/$", views.delete_user, name="delete_user"),
    url(r"^list_user/$", views.list_user, name="list_user"),
    url(r"^reg/$", views.reg, name="reg"),
    url(r"^login/$", views.login, name="login"),
    url(r"^logout/$", views.logout, name="logout"),
    url(r"^show/(\d+)/$", views.show, name="show"),
    url(r"^(?P<u_id>\d+)/update/$", views.update, name="update"),
    url(r"^code/$", views.code, name="code"),
    url(r"^(\w+)/checkusername/$", views.checkusername, name="checkusername"),

    # 文章路由
    url(r'^add_article/$', views.add_article, name="add_article"),
    url('^(?P<a_id>\d+)/delete_article/$', views.delete_article, name='delete_article'),
    url('^(?P<a_id>\d+)/update_article/$', views.update_article, name='update_article'),
    url('^(?P<a_id>\d+)/show_article/$', views.show_article, name='show_article'),
    url('^show_articles/$', views.show_articles, name='show_articles'),
    url('^(?P<a_id>\d+)/show_p_articles/$', views.show_p_articles, name='show_p_articles'),
    url(r"^delete_article/(?P<article_id>\d+)/$", views.delete_article, name="delete_article"),
    url('^(?P<a_id>\d+)/update_article/$', views.update_article, name='update_article'),

]