from django.core.cache import cache

from . import models


def get_articles(ischange=False):
    '''
    缓存所有文章
    :return: 返回所有文章
    '''
    print("查询缓存")
    articles = cache.get("allArticle")
    if articles is None or ischange:
        print("查询数据库")
        articles = models.Article.objects.all()
        cache.set("allArticle", articles)
    return articles

