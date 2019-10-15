from django.db import models
from django.urls import reverse

"""
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*
"""

class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # $ pip install pillow 이미지는 비울 수도 있다
    created_at = models.DateTimeField(auto_now_add=True)  # 추가될 때만 / add 될 때 / 고정 
    updated_at = models.DateTimeField(auto_now=True)  # 수정, save 할 때마다

    # Detail 페이지를 쓸 거라면 만들어요.
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})  # id랑 pk 같은 말

    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'