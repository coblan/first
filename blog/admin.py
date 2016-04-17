from django.contrib import admin
import models

import handler_src_model
# Register your models here.
class SrcAdmin(admin.ModelAdmin):
    class Media:
        js=("http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js",
            'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.6/angular.min.js',
            'js/blog_ck.pack.js',
            'ckeditor/ckeditor.js',
            'ckeditor/adapters/jquery.js')
admin.site.register(models.SrcModel,SrcAdmin)
admin.site.register(models.HtmlArt)
admin.site.register(models.Tag)