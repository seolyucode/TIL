from django.contrib import admin
from .models import Fcuser  # model 안에 있는 Fcuser 클래스 가져오기

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # 이렇게 명시하면 클래스 객체가 listup되는게 아니라 모델 클래스 아래 Field들이 listup됨

admin.site.register(Fcuser, FcuserAdmin)