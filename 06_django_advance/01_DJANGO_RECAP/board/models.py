from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()

    # 인스턴스 메서드. 디테일 페이지가 있을 경우 유용
    def get_absolute_url(self):
        return reverse("board:detail", kwargs={"id": self.id})  