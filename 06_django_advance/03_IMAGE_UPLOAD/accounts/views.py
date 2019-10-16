from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm

@require_http_methods(['GET', 'POST'])
def signup(request):  # new_user
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

def login(request):
    pass

def logout(request):
    pass
