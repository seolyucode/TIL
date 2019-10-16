from django import forms
from .models import Question, Choice

class ChoiceModelForm(forms.ModelForm):
    CHOICES = [
        ('한식', '한식이요'),  # 진짜 넘어오는 데이터 / 사용자가 보는 데이터
        ('중식', '중식이요'),
        ('양식', '양식이요'),
        ]
    content = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = Choice
        fields = ('content',)