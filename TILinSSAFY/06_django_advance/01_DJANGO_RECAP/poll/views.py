from django.shortcuts import render

# 2개 함수

'''
def new_choice(request):
    form = ...Form(request.POST)
    if form.is_valid():
        choice = form.save(commitFalse)
        if choice.content == '???':
            choice.vote += 1
'''
'''
def new_choice(request):
    form = ...Form(request.POST)
    if form.is_valid():
        choice = form.save(commitFalse)
        choice.question_id = ??
        choice.save()
'''

def question_detail(request, question_id):
    # 
    return render(request, 'poll/question_detail.html', {
        #
    })

def upvote(request, # ?? ):

    return redirect(???)
