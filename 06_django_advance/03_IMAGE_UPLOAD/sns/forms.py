from django import forms
from .models import Posting

class PostingModelForm(forms.ModelForm):  # 이름 짓기 나름
    content = forms.CharField(min_length=2)
    class Meta:  # Meta는 예약어
        model = Posting
        fields = ('content', 'image')