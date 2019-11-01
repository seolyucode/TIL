from django.db import models

# Create your models here.
class Fcuser(models.Model):  # 클래스 만들기. 장고에서 제공하는 models.Model 상속 받아야 함
    # username이라는 필드를 만듦
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,  # auto_now_add=True => Fcuser 클래스가 저장되는 시점 시간 자동으로 들어감
                                            verbose_name='등록시간')

    # 테이블명 지정 => 아까 settings.py에 있던, 기본적으로 생성되는 앱들과 구분해서 테이블명 만들기 위해 이렇게 직접 쓰는 경우가 있음
    class Meta:
        db_table = 'fastcampus_fcuser'