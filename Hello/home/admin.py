from django.contrib import admin
from home.models import Contact
from home.models import Video
from home.models import Like
from home.models import Dislike
from home.models import Comment
from home.models import News
# Register your models here.
admin.site.register(Contact)
admin.site.register(Video)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)
admin.site.register(News)