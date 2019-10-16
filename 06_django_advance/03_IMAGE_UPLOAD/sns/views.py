from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Posting
from .forms import PostingModelForm

@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
    })

@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
    })

@require_POST
def create_posting(request):
    posting = Posting()
    posting.content = request.POST.get('content')
    posting.icon = ''
    posting.image = request.FILES.get('image')
    posting.save()
    
    return redirect(posting)  # redirect('sns:posting_detail', posting.id)


@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 검증 & 저장 준비
    if form.is_valid():  # 검증!
        posting = form.save()  # 저장 => Posting 객체 return  /  posting은 변수
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page