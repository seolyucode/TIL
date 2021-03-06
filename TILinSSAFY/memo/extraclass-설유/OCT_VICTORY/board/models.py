from django.db import models

# models.Model 을 상속받는 Class 에서 class 멤버변수는 테이블의 컬럼이 됨.
class Article(models.Model):
    # id(pk) = INTEGER AUTO INCREMNT UNIQUE
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 처음 저장(.save())될 때의 시간만 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # 저장(.save())될 때의 시간을 저장
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at',]

class Comment(models.Model):
    # id(pk) = INTEGER AUTO INCREMNT UNIQUE
    content = models.CharField(max_length=200)
    # 처음 저장(.save())될 때의 시간만 저장
    created_at = models.DateTimeField(auto_now_add=True)
    # 저장(.save())될 때의 시간을 저장
    updated_at = models.DateTimeField(auto_now=True)


"""
0. DB 를 다루고 싶다.. 근데 SQL 은 쓰기 싫다.
1. DB 를 다루다.
    1. 테이블을 만들고 싶다..
        1. 테이블의 Schema 는 이렇게 됐으면 좋겠다.. => models.py 에 class/멤버변수 정의
        2. DB 전문가(ORM)에게 내 소원이 적절한지 물어보자. => $ makemigrations
        3. (소원이 적절하면)전문가가 견적서를 만들어 준다. => APP/migrations/000N_... 파일
        4. 소원이 바뀌면, 소원을 다시 적는다.
        5. 소원이 바뀜 => 다시 견적 받기.
        ....
        6. OK! 견적서대로 갑시다. => $ migrate
        7. 전문가(ORM)가 DB 에 반영.
"""