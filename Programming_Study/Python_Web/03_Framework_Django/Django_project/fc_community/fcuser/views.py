from django.shortcuts import render

def register(request):
    # 기본적으로 templates 폴더를 바라보고 있어서 register.html이라 쓰면 되고 
    # 그 안에 폴더 안에 있으면 'folder/register.html' 이런 식으로
    return render(request, 'register.html')