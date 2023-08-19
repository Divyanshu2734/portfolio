from django.contrib import admin
from .models import reachme,blog,msg


# Register your models here.





class intern(admin.ModelAdmin):
    list_display=('name',
    'email',
    'subject',
    'mssages',)
    search_fields=('name',)




class blog2(admin.ModelAdmin):
    list_display=(  'title',
    'discription',
    'author_name',
    'image',
    'timestamp',)
    search_fields=('title',)
    list_filter=['title','author_name','timestamp']

class reach(admin.ModelAdmin):
    list_display=('name',
    'last_name',
    'email',
    'mobile',
    'discription',

    )
    search_fields=('name','mobile',)
    list_filter=['email','mobile']

admin.site.register(msg,intern)
admin.site.register(blog,blog2)
admin.site.register(reachme,reach)
