from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder' : 'Enter the title',
#             }
#         )
#     )
#     content = forms.CharField(
#         label = '내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder' : 'Enter the content',
#                 'rows': 5,
#                 'cols': 50,
#             }

#         )
#     ) # textfield 를 쓰지 않고 charfield 에 max_length 를 지정하지 않으면 된다.
#     # widget


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
        model = Article
        # fields = ('title', 'content',)
        fields = '__all__'
        # exclude = ('title',)
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'
        #     })
        # }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
