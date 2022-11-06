from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import WebUser,WebConsume,WebSaving,WebCard,StockInteg #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

admin.site.register(WebUser)
admin.site.register(WebConsume)
admin.site.register(WebSaving)
admin.site.register(WebCard)
admin.site.register(StockInteg)