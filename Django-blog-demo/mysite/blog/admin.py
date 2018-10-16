# from django.contrib import admin
#
# # Register your models here.
# from .models import User
# from .models import Article
#
#
# class UserAdmin(admin.ModelAdmin):
#     '''
#     后台展示
#     '''
#
#     # 修改 BooleanField 类型的内容展示
#     def is_delete_label(self):
#         if self.is_delete:
#             return "删除"
#         else:
#             return "不删除"
#
#     # 用于表头展示
#     is_delete_label.short_description = "是否删除"
#     # 列表页面要显示属性
#     # list_display = ["name", "nickname", "age", "birthday", "is_delete" ]
#     # 使用上面定义的方法来代替显示是否删除项
#     list_display = ["name", "nickname", "age", "birthday"]
#
#
#     # 过滤的属性
#     list_filter = ["age", "birthday"]
#     # 分页的每页数量
#     list_per_page = 8
#
#     # 增加和修改的属性
#     # fields = ["name", "nickname"]
#     # 注意，fields 和 fieldsets 不能同时出现
#     fieldsets = [
#         ("base", {"fields": ["age"]}),
#         ("other", {"fields": ["name", "nickname"]}),
#     ]
#
#     # 设置搜索的选项
#     search_fields = ["name", "nickname"]
#
#     # # ordering 设置默认排序字段，负号表示降序排序
#     # ordering = ('-publishTime',)
#
#     # list_editable 设置默认可编辑字段
#     list_editable = ['age']
#
#     # 设置可以点击进入编辑界面，默认是第一个选项
#     list_display_links = ["name", 'birthday']
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ["title"]
#
#
# # 注册
# admin.site.register(Article, ArticleAdmin)
# admin.site.register(User, UserAdmin)
#
