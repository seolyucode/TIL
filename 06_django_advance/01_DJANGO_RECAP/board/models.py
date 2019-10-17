from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 인스턴스 메서드. 디테일 페이지가 있을 경우 유용
    def get_absolute_url(self):  # detail page 가 있을 때 쓰는거임
        return reverse("board:article_detail", kwargs={"article_id": self.id})

# Article은 변수라서 Article 클래스와 Comment 클래스 자리 못 바꿈
class Comment(models.Model):
    content = models.CharField(max_length=200)  # max_length는 잘라버림. 200 넘어가면 절삭
    # article_id는 외부에 어떤 것을 가져오는 거라서 ForeignKey
    # Article을 참조하겠다
    # CASCADE 원주인이 날라가면 (댓글들) 다 지우겠다
    # on_delete=models.CASCADE 꼭 써야함
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)