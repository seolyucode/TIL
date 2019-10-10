from django import forms
from .models import Article

# forms.Form => Data 입력 및 검증
# forms.ModelForm => Data 입력/검증 + HTML 생성

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