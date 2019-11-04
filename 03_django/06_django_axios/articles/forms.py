from django import forms
from django.forms import ModelForm
from .models import Article, Comment
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': 'Enter the title',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content',
#                 'rows': 5,
#                 'cols': 50,

#             }
#         )
#     ) # forms에는 textfield 없음..charfield에서 max_length 설정 안하면 됨.

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,

            }
        )
    ) 
    class Meta:
        model = Article # model은 article에서 가져온다.
        # fields = ('title', 'content',)
        fields = ('title', 'content',) # field는 전체를 다 쓸 것이다...
        # exclude = ('title',)
        # Meta 태그 위에 쓰는 것을 권장.
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'
        #     })
        # }

class CommentForm(forms.ModelForm):
    # content = forms.CharField(max_length=50)
    class Meta:
        model = Comment
        fields = ['content']