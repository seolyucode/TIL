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



templates

view