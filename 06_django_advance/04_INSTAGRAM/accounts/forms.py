from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User

# 정보 저장
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

# 인증
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User