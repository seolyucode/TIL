from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser  # 모델 안에 있는 Fcuser 클래스를 가지고 옴
from .forms import LoginForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')
    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            # session
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')  # 'folder/folder2/register.html'
    elif request.method == "POST":
        username = request.POST.get('username', None)  # request.POST 딕셔너리 형태였는데 key 없으면 에러나므로 get 함수 사용해서 기본값 지정함
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}  # 에러메세지를 담을 변수 만들기

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.' 
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            # 클래스 변수 객체 생성
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)  # make_password 함수를 사용해서 암호화
            )

            # 저장
            fcuser.save()

        return render(request, 'register.html', res_data)