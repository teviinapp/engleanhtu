from django.contrib import admin

# Register your models here.
from first_app.models import Topic, Webpage, Content,UserProfileInfo

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Content)
admin.site.register(UserProfileInfo)