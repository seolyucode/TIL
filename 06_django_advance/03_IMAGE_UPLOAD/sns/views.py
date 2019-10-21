from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm


# @login_required(login_url='/users/login/')  # login 이 X 면 => 무조건 /accounts/login/
# @login_required
@require_GET
def posting_list(request):
    # nickname = request.COOKIES.get('nickname')
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
        # 'nickname': nickname,
    })

@login_required
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set 이 아닌 이유는 Model => related_name
    is_like = True if posting.like_users.get(id=request.user.id).exists() else False
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
        'is_like': is_like,
    })

'''
@require_POST
def create_posting(request):
    posting = Posting()
    posting.content = request.POST.get('content')
    posting.icon = ''
    posting.image = request.FILES.get('image')
    posting.save()
    
    return redirect(posting)  # redirect('sns:posting_detail', posting.id)
'''

@login_required
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 검증 & 저장 준비
    if form.is_valid():  # 검증!
        posting = form.save(commit=False)  # 저장 => Posting 객체 return  /  posting은 변수
        posting.user = request.user  # anonymous
        posting.save()
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page

@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user:
        posting.delete()
    return redirect('sns:posting_list')

@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content 만 값을 확인
    if form.is_valid():  # content 만 값을 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 '척' 만 하고 Comment 객체 return
        # comment.posting_id = posting.id
        comment.posting = posting  # 위 코드와 같음
        comment.user = request.user
        comment.save()
    return redirect(posting)


# 기본적으로 이렇게 되어있음. 안써도 됨
class User():
    def __str__(self):
        return self.username

@login_required
@require_POST
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    # if user in posting.like_users.all():
    if posting.like_users.get(id=user.id).exists():
        posting.like_users.remove(user)  # Delete
        is_like = False
    else:
        posting.like_users.add(user)  # Create
        is_like = True
    # user.like_postings.add(posting)
    # posting.like_users.add(user)  # Create
    return redirect(posting)

@login_required
@require_POST
def dislike(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    posting.like_users.remove(user)  # Delete
    return redirect(posting)