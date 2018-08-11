from django.contrib import admin


from facebook.models import Article
from facebook.models import Comment #추가한 comment 부르기






# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)



