from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

@require_http_methods(['GET', 'POST'])
def signup(request):  # new_user
    if request.user.is_authenticated: # 사용자가 login 한 상태라면, 무시
        return redirect('sns:posting_list')

    # 사용자가 회원가입 할 데이터를 보냈다면,
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 함수 실행.. form이 잘못되면 form에 든 것이 채점됨
            user = form.save()  # 없어도 됨
            return redirect('sns:posting_list')
        # else:
            # return render(request, 'accounts/signup.html', {
            #     'form': form,  # 채점된 것. 망한 시험지
            # })

    else:  # 사용자가 회원가입 HTML 을 달라는 뜻
        form = UserCreationForm()  # 새 시험지
        # return render(request, 'accounts/signup.html', {
        #     'form': form,  # 새 시험지
        # })
    return render(request, 'accounts/signup.html', {
            'form': form,  # 새 시험지
        })

@require_http_methods(['GET', 'POST'])
def login(request):
    # from IPython import embed; embed()
    # # if  # 사용자가 login 한 상태라면, 무시
    # from IPython import embed; embed()
    # # if request.user.is_authenticated:
    # from IPython import embed; embed()
    if request.user.is_authenticated: # 사용자가 login 한 상태라면, 무시
        return redirect('sns:posting_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  # form <- 입국신청서
        if form.is_valid():
            auth_login(request, form.get_user())
            # response = redirect('sns:posting_list')
            # response.set_cookie(key='nickname', value='idiot', max_age=5)
            # response.set_cookie(key='nickname', value='idiot')  
            # return response
            return redirect('sns:posting_list')
            # return redirect('sns':posting_list).set_cookie(asdf)  # 이렇게 X 원본파괴
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })

def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')