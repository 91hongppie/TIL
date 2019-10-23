from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()  # return User
        fields = ('first_name', 'last_name', 'email',)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserChangeForm.Meta):
        # model = get_user_model() # UserChangoForm.Meta 를 상속받으면 쓰면 지워도된다.
        # Meta(UserChangoForm.Meta) 를 쓰면 이렇게 쓴다.
        model = get_user_model()  # accounts.User 를 바라보게 된다.
        fields = UserCreationForm.Meta.fields + ('email',)
        # fields = ('username', 'password1', 'password2', 'email',)
