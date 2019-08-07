from django.db import models

# 테이블 생성


class Student(models.Model):
    '''
    name => str
    email => str
    github_id => str
    age => int
    '''
    name = models.CharField(max_length=10)  # CharField는 max_length를 정해줘야함
    email = models.CharField(max_length=50)
    github_id = models.CharField(max_length=50)
    age = models.IntegerField()

class Menu(models.Model):
    name = models.CharField(max_length=100)  # CharField는 max_length를 정해줘야함
    price = models.FloatField()
    category = models.CharField(max_length=50)
 
