from django.shortcuts import render, redirect
from .models import Article


# Create
def new(request):  # 새로운 게시글을 작성할 화면(을 주는 view)
    return render(request, 'board/new.html')


def create(request):  # 입력 데이터를 DB에 저장
    # request.GET => {'input_title': 제목제목, 'input_content': 내용내용}
    # print(request.GET)
    article = Article()
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    
    return redirect(f'/board/articles/{article.id}/')

# Read
def index(request):  # 모든 게시글 목록을 보여주는 view
    # return HttpResponse('hi :)')
    articles = Article.objects.all()  # [] 들어가서 복수형
    return render(request, 'board/index.html', {
        'articles': articles,
    })


def show(request, article_id):  # 특정 게시글을 보여주는 veiw
    article = Article.objects.get(id=article_id)
    return render(request, 'board/show.html',{
    'article': article,
    })


# Update
def edit(request):  # 특정 게시글을 수정할 화면
    return render(request, 'board/edit.html')


# Delete
def delete(request, article_id):  # 특정 게시글을 삭제하는 view(일)
    a = Article.objects.get(id=article_id)  # 특정
    a.delete()
    return redirect('/board/articles')