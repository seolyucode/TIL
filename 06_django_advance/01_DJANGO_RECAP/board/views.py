from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Article, Comment
from .forms import ArticleModelForm, CommentModelForm, ArticleForm
from IPython import embed

'''
# Create Article with Form
def new_article_with_form(request):
# def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            # article.title = request.POST.get('title')  # 검증되지 않은 데이터
            article.title = form.cleaned_data.get('title')  # 검증된 데이터
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect(article)
    else:
        form = ArticleForm()
    return render(request, 'board/new.html', {
        'form': form,
    })
'''

# # CRUD
@require_http_methods(['GET', 'POST'])
def new_article(request):
    # 요청이 GET/POST 인지 확인한다.
    # 만약 POST 라면
    if request.method == 'POST':
        # ArticleModelForm 의 인스턴스를 생성하고 Data 를 채운다(binding).
        form = ArticleModelForm(request.POST)
        # embed()  # 디버깅용
        # binding 된 form 이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 form 을 저장한다.
            article = form.save()
            # 저장한 article detail 로 redirect 한다.
            return redirect(article)
            # return redirect('board:article_detail', article.id)를 많이 써서
            # models.py에 Article 클래스에 get_absolute_url 메서드가 있어서 줄일 수 있음
        # form 이 유효하지 않다면,
        # else:
        #     # 유효하지 않은 입력데이터를 담은 HTML과 에러메세지를 사용자한테 보여준다.
        #     return render(request, 'board/new.html', {
        #         'form': form,
        #     })

    # GET 이라면
    else: 
        # 비어있는 form(HTML 생성기) 을 만든다.
        form = ArticleModelForm()
    # embed()
        # form 과 html 을 사용자에게 보여준다.
    return render(request, 'board/new.html', {
        'form': form,
    })

@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })

@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    # 게시글 찾기
    article = get_object_or_404(Article, id=article_id)
    # 제출할께요
    if request.method == 'POST':  # 데이터가 날라왔다면
        # 데이터 넘어온거 받는거
        form = ArticleModelForm(request.POST, instance=article)  # 데이터를 넣은 다음에
        if form.is_valid():  # 저장할만하면
            article = form.save()  # 저장(작성)
            return redirect(article)  # detail 페이지로 가기
        '''    
        else:  # 유효하지 않다면(form은 존재함)
            return render(request, 'board/edit.html', {
                'form': form,
            })
        '''
    # 수정할께요 종이주세요
    else:
        # article = get_object_or_404(Article, id=id)
        # embed()
        form = ArticleModelForm(instance=article)
    return render(request, 'board/edit.html', {
        'form': form,
    })        

@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # .order_by('-id') 나중에 쓴게 먼저 나옴. 거꾸로 나옴
    comments = article.comment_set.all().order_by('-id')  # Comment.objects.filter(article_id=article.id)
    comment_form = CommentModelForm()

    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })

@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('board:article_list')

@require_POST
def new_comment(request, article_id):  # /board/articles/N/comments/new/  |  /board/articles/1/comments/3/delete
    article = get_object_or_404(Article, id=article_id)  # 사용자의 요청 검증
    form = CommentModelForm(request.POST)
    # embed()
    if form.is_valid():
        # comment = Comment()
        # comment.content = request.POST.get('content')
        comment = form.save(commit=False)  # comment = 는 필요가 없음  # 저장하는 척
        comment.article_id = article.id
        comment.save()

    # comment = Comment()
    # comment.content = request.POST.get('comment_content')
    # comment.article_id = article.id
    # comment.save()
    return redirect(article)


@require_POST
def delete_comment(request, article_id, comment_id):
    from time import time
    start = time.time()

    # article = get_object_or_404(Article, id=article_id)
    # comment = get_object_or_404(Comment, id=comment_id)
    # if comment in article.comment_set.all():
    #     comment.delete()
    # return redirect(article)

    # comment = get_object_or_404(Comment, id=comment_id)
    comment = get_object_or_404(Comment, id=comment_id, article_id=article_id)

    comment.delete()

    end = time.time()
    print(end-start)
    return redirect(comment.article)
    
"""
c = Comment()
c.content = request.POST.get('content')
c.article_id = 1
c.save()
"""