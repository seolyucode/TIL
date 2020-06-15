### Django란? 

웹 프레임워크에 대한 이해

* 자주 사용되는 코드를 체계화하여 쉽게 사용할 수 있도록 도와주는 코드 집합
* 라이브러리와 혼동될 수 있지만 좀 더 규모가 크고 프로젝트의 기반이 됨
* 건축에 비유하면 구조를 만드는 골조가 프레임워크라면 그 외 자재들이 라이브러리가 됨



* 웹 개발에 필요한 기본적인 구조와 코드(클래스, 함수 등)가 만들어져있음

  웹 개발 - URL 파싱, 요청 파싱, 응답 생성, 세션 관리, 관리자 페이지, 데이터베이스 연동(웹 프레임워크) (+비즈니스 로직, 데이터정의(개발 영역))



### Django

https://docs.djangoproject.com/ko/2.1/

MPV (모델, 템플릿, 뷰), 폼

모델 계층 - 데이터베이스와 연관. 모델 계층에 파이썬으로 클래스 만들고 연결해주면 sql 생성됨. 데이터를 구조화하고 조작

뷰 계층 - url 파싱, 비즈니스 로직(요청, 응답) ..

템플릿 계층 - html 코드



`py -m venv venv`

` source venv/Scripts/activate`

`pip install django`

`django-admin startproject fc_community`

`cd fc_community/`

`django-admin startapp board`



board 앱 안에 templates 폴더 만들기

정적분석도구?



`django-admin startapp fcuser`

fcuser에 templates 폴더 만들기



fc_community - fc_community <- 프로젝트가 만들어질 때 만들어진 폴더

settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'fcuser',
]
```



fcuser - models.py

```python
from django.db import models

class Fcuser(models.Model):  # 장고에서 제공하는 models.Model 상속
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name ='등록시간')
    class Meta:
        db_table = 'fastcampus_fcuser'
```



model을 관리할 수 있는 관리자 페이지 설정, 활용

`ls`

`python manage.py makemigrations`

fcuser - migrations 폴더 안에 initial.py 파일 생김

`python manage.py migrate`

settings.py에 있던 앱들이 사용하는 테이블 자동으로 생성

새로고침하면 db.sqlite3이 생성됨

db.sqlite3은 setting에 이미 설정되어있음 DATABASES에

`sqlite3 db.sqlite3`

.tables

.schema fastcampus_fcuser

.q



필드가 추가 .. 수정하면

`python manage.py makemigrations`

`python manage.py migrate`



settings.py - admin 기본적으로 설정되어 있음

urls.py에도 admin 기본으로 들어가있음

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]  # admin 하위에 있는 것들
```

`python manage.py runserver`

127.0.0.1:8000/admin

아이디 로그인 설정해야함

Ctrl + C 눌러서 종료하고

`python manage.py createsuperuser`

계정 생성하기

`python manage.py runserver`

127.0.0.1:8000/admin

로그인하기

Users 들어가보면 아까 생성한 superuser 있음



django admin에 만든 모델 등록하기

fcuser - admin.py

```python
from django.contrib import admin
from .models import Fcuser

class FcuserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fcuser, FcuserAdmin)
```



fcuser - models.py

```python
from django.db import models

class Fcuser(models.Model):  # 장고에서 제공하는 models.Model 상속
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name ='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
```



fcuser - admin.py

```python
from django.contrib import admin
from .models import Fcuser

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Fcuser, FcuserAdmin)
```



fcuser - models.py

```python
from django.db import models

class Fcuser(models.Model):  # 장고에서 제공하는 models.Model 상속
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name ='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
```



templates 회원가입 페이지 생성

fcuser - templates - register.html

 https://getbootstrap.com/docs/4.3/getting-started/introduction/ 

 https://getbootstrap.com/docs/4.3/components/forms/ 

```html
<html>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
</head>

<body>
    <div class="container">
        <div class="row mt-5">
            <div class="col-12 text-center">
                <h1>회원가입</h1>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col-12">
                <form>
                    <div class="form-group">
                        <label for="exampleInputEmail1">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                            placeholder="Enter email">
                        <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone
                            else.</small>
                    </div>
                    <div class="form-group">
                        <label for="exampleInputPassword1">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                    </div>
                    <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                        <label class="form-check-label" for="exampleCheck1">Check me out</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        </div>
    </div>
</body>

</html>
```



fcuser - views.py

```python
from django.shortcuts import render

def register(request):
    # 기본적으로 templates 폴더를 바라보고 있어서 register.html이라 쓰면 되고 
    # 그 안에 폴더 안에 있으면 'folder/register.html' 이런 식으로
    return render(request, 'register.html')  
```



url 설정

fc_community - urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcuser/', include('fcuser.urls')),
]
```



fcuser에 urls.py 만들기

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
]
```

 http://127.0.0.1:8000/fcuser/register/ 



register.html

```html
<html>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
</head>

<body>
    <div class="container">
        <div class="row mt-5">
            <div class="col-12 text-center">
                <h1>회원가입</h1>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col-12">
                <form>
                    <div class="form-group">
                        {% comment %} <label for="exampleInputEmail1">Email address</label> {% endcomment %}
                        <label for="username">사용자 이름</label>
                        <input type="text`" class="form-control" id="username" placeholder="사용자 이름">
                    </div>
                    <div class="form-group">
                        <label for="password">비밀번호</label>
                        <input type="password" class="form-control" id="password" placeholder="비밀번호">
                    </div>
                    <div class="form-group">
                        <label for="re-password">비밀번호 확인</label>
                        <input type="password" class="form-control" id="re-password" placeholder="비밀번호 확인">
                    </div>
                    <button type="submit" class="btn btn-primary">등록</button>
                </form>
            </div>
        </div>
    </div>
</body>

</html>
```

{% csrf_token %} 

암호화된 키를 숨겨놈, 크로스 도메인 방지

```html
<html>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
</head>

<body>
    <div class="container">
        <div class="row mt-5">
            <div class="col-12 text-center">
                <h1>회원가입</h1>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col-12">
                <form method="POST" action=".">
                    {% csrf_token %}
                    <div class="form-group">
                        {% comment %} <label for="exampleInputEmail1">Email address</label> {% endcomment %}
                        <label for="username">사용자 이름</label>
                        <input type="text`" class="form-control" id="username" placeholder="사용자 이름">
                    </div>
                    <div class="form-group">
                        <label for="password">비밀번호</label>
                        <input type="password" class="form-control" id="password" placeholder="비밀번호">
                    </div>
                    <div class="form-group">
                        <label for="re-password">비밀번호 확인</label>
                        <input type="password" class="form-control" id="re-password" placeholder="비밀번호 확인">
                    </div>
                    <button type="submit" class="btn btn-primary">등록</button>
                </form>
            </div>
        </div>
    </div>
</body>

</html>
```



register.html

```html
<html>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
</head>

<body>
    <div class="container">
        <div class="row mt-5">
            <div class="col-12 text-center">
                <h1>회원가입</h1>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col-12">
                <form method="POST" action=".">
                    {% csrf_token %}
                    <div class="form-group">
                        {% comment %} <label for="exampleInputEmail1">Email address</label> {% endcomment %}
                        <label for="username">사용자 이름</label>
                        <input 
                        type="text" 
                        class="form-control" 
                        id="username" 
                        placeholder="사용자 이름"
                        name="username"
                        />
                    </div>
                    <div class="form-group">
                        <label for="password">비밀번호</label>
                        <input 
                        type="password"
                        class="form-control"
                        id="password"
                        placeholder="비밀번호"
                        name="password"
                        />
                    </div>
                    <div class="form-group">
                        <label for="re-password">비밀번호 확인</label>
                        <input 
                        type="password" 
                        class="form-control" 
                        id="re-password" 
                        placeholder="비밀번호 확인"
                        name="re-password"
                        />
                    </div>
                    <button type="submit" class="btn btn-primary">등록</button>
                </form>
            </div>
        </div>
    </div>
</body>

</html>
```



fcuser-views.py

```python
from django.shortcuts import render
from .models import Fcuser

def register(request):
    # 기본적으로 templates 폴더를 바라보고 있어서 register.html이라 쓰면 되고 
    # 그 안에 폴더 안에 있으면 'folder/register.html' 이런 식으로
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        fcuser = Fcuser(
            username=username,
            password=password
        )

        fcuser.save()

        return render(request, 'register.html')
```

회원가입 하고  http://127.0.0.1:8000/admin/ 에서 확인해보기

views.py

```python
from django.http import HttpResponse
from django.shortcuts import render
from .models import Fcuser

def register(request):
    # 기본적으로 templates 폴더를 바라보고 있어서 register.html이라 쓰면 되고 
    # 그 안에 폴더 안에 있으면 'folder/register.html' 이런 식으로
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        if password != re_password:
            return HttpResponse('비밀번호가 다릅니다!')

        fcuser = Fcuser(
            username=username,
            password=password
        )

        fcuser.save()

        return render(request, 'register.html')
```

원래 입력하던 폼에서 나오게 하기

```python
from django.http import HttpResponse
from django.shortcuts import render
from .models import Fcuser

def register(request):
    # 기본적으로 templates 폴더를 바라보고 있어서 register.html이라 쓰면 되고 
    # 그 안에 폴더 안에 있으면 'folder/register.html' 이런 식으로
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                password=password
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
```

비밀번호 암호화해서 저장하기

```python
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Fcuser

def register(request):
    # 기본적으로 templates 폴더를 바라보고 있어서 register.html이라 쓰면 되고 
    # 그 안에 폴더 안에 있으면 'folder/register.html' 이런 식으로
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password)
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
```

