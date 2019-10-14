from django import forms
from .models import Article, Comment

# forms.Form => Data 입력 및 검증 + HTML 생성 => Model 정보 모름
# forms.ModelForm => Data 입력/검증 + HTML 생성 => Model 정보를 알고있음

class ArticleForm(forms.Form):
    title = forms.CharField(
        min_length=20, max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter title plz',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-class',
                'placeholder': 'Content is required',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    

# ArticleModelForm은 유효성 검사
class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    # title = forms.CharField(min_length=3, required=False)  # 주석처리해도 상관없음
    title = forms.CharField(min_length=2, max_length=100)
    # 핵심인 데이터 저장
    class Meta:
        model = Article  # 핵심
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # 200 을 검증

    class Meta:
        model = Comment
        # fields = '__all__'  
        fields = ('content',)  # Data 입력/검증 + HTML 생성 - content만 보겠다