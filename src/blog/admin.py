from django.contrib import admin
import models

import handler_src_model
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    exclude=('html',)
    list_display=('title','category','order')
    ordering =('order',)
    class Media:
        js=("http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js",
            'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.6/angular.min.js',
            'ckeditor/ckeditor.js',
            'ckeditor/adapters/jquery.js',
            'js/blog_ck.pack.js?t=20160520',)
admin.site.register(models.ArticleModel,ArticleAdmin)
#admin.site.register(models.HtmlArt)
admin.site.register(models.Tag)
admin.site.register(models.CatModel)