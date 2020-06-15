from django.shortcuts import render, HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse('Hi django! :)')

def cube(request, num):
    # 기본 자료형은 return 안됨!
    r = num ** 3
    context = {'result': r}
    return render(request, 'cube.html', context)

def about(request):
    me = {
        'name': '이설유',
        'role': 'Student',
        'email': 'seolyu.90@gmail.com',
    }

    return HttpResponse(json.dumps(me))


# HTML 을 내보내고 싶다.
def portfolio(request):

    return render(request, 'portfolio.html')


# pages/help/ => help() view 함수 실행 => help.html (내용 무관)
def help(request):

    return render(request, 'help.html')