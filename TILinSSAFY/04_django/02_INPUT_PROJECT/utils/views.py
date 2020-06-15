# from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from art import *


# Create your views here.


def index(request):
    return render(request, 'utils/index.html')


def art(request):
    fonts = ['3d_diagnoal', 'acrobatic', 'alpha', 'avatar', 'cards']
    return render(request, 'utils/art.html', {
        'fonts': fonts,
    })


def output(request):
    # print(request.POST)
    # request.GET.get('')
    # print(request.GET.get('user-input'))
    user_input = request.GET.get('user-input')
    user_font = request.GET.get('user-font')
    # print(request.GET, user_input)
    '''
    if not user_input:  # user_input이 있다면
        user_input = 'NO EMPTY'

    result = text2art(user_input, font=user_font)
        # print(request.GET)


    return render(request, 'utils/output.html', {
            'result': result,
        })
    # return HttpResponse(user_input)
    '''

    if user_input:  # user_input이 있다면
        result = text2art(user_input, font=user_font)
        return render(request, 'utils/output.html', {
            'result': result,
        })
    else:
        return redirect('/utils/art/')


def throw(request):
    return render(request, 'utils/throw.html')


def catch(request):
    return render(request, 'utils/catch.html')
