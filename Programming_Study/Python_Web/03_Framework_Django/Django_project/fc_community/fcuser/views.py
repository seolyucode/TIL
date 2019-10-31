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