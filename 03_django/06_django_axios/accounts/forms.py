from django.contrib.auth.forms import UserChangeForm, UserCreationForm # 상속받음
from django.contrib.auth import get_user_model

# 회원정보 수정 폼 => email, first_name, last_name 수정.
# 필드 -> user objects 확인 https://docs.djangoproject.com/en/2.2/topics/auth/default/#user-objects
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # return User (User라는 모델 호출함..)
        fields = ('email', 'first_name', 'last_name',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # Meta를 한번에 상속받아온다...
        model = get_user_model() # 현재 active된 모델 받아온다. (accounts.User 를 바라보게 됨... 이전에는 auth.User를 보고있었음...)
        # 필드 한번에 받아옴!!
        fields = UserCreationForm.Meta.fields + ('email',)