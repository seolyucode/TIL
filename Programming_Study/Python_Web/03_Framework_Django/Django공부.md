`pip3 install virtualenv`  # 안돼서 

`py -m venv venv`  # venv 폴더 생성됨

`source venv/Scripts/activate`  # venv 활성화

`pip install django`  

`django-admin startproject fc_community`  # 프로젝트 생성

`cd fc_community/`

`django-admin startapp board`  # board app 생성



프로젝트 = 프로그램

앱 단위로 분리해서 코드를 관리



board 앱 안에 templates 폴더 생성

장고의 templates 엔진이 각 앱의 templates 폴더를 바라보고 있음



cf) 정적분석도구

MVC 패턴

MTV



fcuser 앱 만들어보기

`django-admin startapp fcuser`



앱을 프로젝트에 등록하기

fc_community 안에 fc_community 폴더는 프로젝트가 만들어질 때 만들어진 폴더

settings.py 안에 들어가서

INSTALLED_APPS 가보면

기본적인 것들 있는데 좀 전에 만든

board와 fcuser도 등록하기



fcuser  > models.py



models.py의 class가 table로 만들어지는 과정 살펴보기

`python manage.py makemigrations`  # migrations 폴더 안에 initial.py 생성됨

`python manage.py migrate`  # settings에 여러가지 앱들이 사용하는 테이블을 자동으로 생성해줌 + 아까 만든 fcuser도 생성됨



db.sqlite3이 생성된 것 확인(settings.py에 DATABASES 보면 sqlite3 사용한다고 쓰여있음)

잘 만들어져있는지 확인

`sqlite3 db.sqlite3`

`.tables`

`.schema fastcampus_fcuser`



field 수정하면 

`python manage.py makemigrations`

`python manage.py migrate`

지속적으로 데이터베이스에 반영



model 관리할 수 있는 관리자 페이지 설정, 활용하기

fc_community > urls.py 보기

 http://127.0.0.1:8000/admin

아이디 비번 설정해야함

Ctrl + C 종료하고

`python manage.py createsuperuser`

서버 열고 로그인 해보기

Users 들어가면 좀 전에 생성한 superuser 있음



장고 admin에 만든 admin 등록하기 

admin.py - 관리자에 쓸 정보 기입



templates

회원가입 페이지 만들기

https://getbootstrap.com/docs/4.3/getting-started/introduction/

에서 헤더 가져오기



{% csrf_token %} : 크로스 도메인 방지. 암호화 된 키를 숨겨놓아서 키가 없으면 잘못된 요청이라고 서버에서 거절함. 장고가 알아서 form에 필요한 형태로 해시정보(암호화 된 정보)를 넣고 검증해줌. 안쓰면 token 없다고 에러남.



view

2가지 경우 구분 - GET / POST

주소 입력

등록버튼 입력



회원가입 해보고 DB 저장되는지 확인

http://127.0.0.1:8000/admin/



...



이메일 필드 추가하고

모델 바뀌었으니 

`python manage.py makemigrations`

기존 데이터에는 어떤 기본값을 넣을지 선택하는게 나옴

1) 직접 기본값 입력

2) 모델 안에서 기본값 지정

1번 선택해서

'test@gmail.com' 

`python manage.py migrate`



모델 바꿨으니

templates 변경



templates과 연결된 view 가서 수정





static 파일 관리

CDN 서비스 : 외부에 있는 css, javascript 가지고오는 것

글로벌 서비스 할 때 미국, 한국에서도 접속하는데

한국에 서버가 있다면

미국 사용자는 느리니까  각나라에 여러 서버를 두고(에지 서버) 거기로

원본 서버에 있는 데이터 가지고 오는게 아니라

pc에서 가장 가까운 서버에서 가져옴

직접 만든거 제공할 땐..

프로젝트(fc_community) 안에 static 폴더(css, javascript 파일 만들고 관리할 것임) 만든다.

등록해야함

settings.py 맨 아래 가서

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```



bootstrap 4.3 themes free - bootswatch 가서

bootstrap.min.css 다운받고

그 파일을 static 폴더에 넣고

register.html 가서

기본적으로 bootstrap에서 제공하는 CDN에서 css 파일 가져오는거 사용하지 않고(주석처리)

```python
  <link rel="stylesheet" href="/static/bootstrap.min.css" />
```



로그인 배우기 전 세션에 대해 배워보자

| 클라이언트(웹 브라우저)                                      | 요청(without cookie) | 서버                                                         |
| ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ |
| Cookie(저장소) -데이터 유지(할당받은 문자열 쿠키정보 키를 저장) 각 웹사이트별로 나눠서 저장 | 응답(with cookie)    | 헤더에 쿠키 정보를 넣어서 클라이언트에게 줌. 문자열 만들어서 데이터베이스에 등록. 클라이언트에게 알려줌. |
| 모든 요청에 쿠키를 같이 보냄                                 | 요청(with cookie)    | 쿠키 정보를 보고 아까 그 클라이언트임을 알고 원하는 정보를 데이터베이스에서 꺼내서 쓸 수 있게 |
|                                                              | 응답(with cookie)    |                                                              |



..



F12 - Application - Cookies - 현재 사이트

csrftoken :

sessionid : 아이디(value) <- request.session['user'] = fcuser.id  # 클라이언트를 식별하는 식별자

세션을 사용하기 위한 정보가 브라우저에 저장되어 있음 - 쿠키에



login.html, register.html에 대부분의 코드가 비슷하므로

기준이 되는 html 파일인 base.html 만들어서 그걸 상속받자



