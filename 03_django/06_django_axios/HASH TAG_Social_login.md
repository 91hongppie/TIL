# HASH TAG

'#안녕 #안녕 하세요'

```python
for word in list:
    # #으로 시작하는 애들만 뽑아낸다.
	if word.startswith('#'):
        # 기존에 있다면 True(뽑아옴) 아니면 False(새로 생성)를 준다.
		hashtag, created = Hashtag.objects.get_or_create(content=word) 
        article.hashtags.add(hashtag)
     return redirect('articles:detail', article.pk)
```

#### `get_or_create(defaults=None, **kwargs)`

https://docs.djangoproject.com/en/2.2/ref/models/querysets/#get-or-create

- 주어진 kwargs로 객체를 찾으며 필요한 경우 하나를 만든다.
- `(object, created)` 형태의 튜플을 리턴한다.
- object는 검색 또는 생성된 객체이고, created는 새 객체 생성 여부를 지정하는 boolean 값이다.(새로 만들어진 object 라면 True, 기존에 존재하던 object 라면 False)
- 단, 이 메서드는 db가 키워드 인자의 `unique` 옵션을 강제하고 있다고 가정하고 실행된다. (content가 unique 값(고유값)을 가진다고 가정함. 중복 object 방지하기 위함)

- 이는 요청이 병렬로 작성 될 때 및 중복 코드에 대한 문제 방지로 중복 오브젝트가 작성되는 것을 예방한다.

  #### unique

  - True인 경우 이 필드는 테이블 전체에서 고유한 값이어야 한다.
  - 유효성 검사 단계에서 실행되며 중복 값이 있는 모델을 저장하려고 하면 .save() 메서드로 인해 `IntegrityError`가 발생한다.
  - ManyToManyField 및 OneToOneField 를 제외한 모든 필드 유형에서 유효하다.

<hr>

수정될 때는



- tag escape 현상

https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#safe



# SOCIAL login

https://django-allauth.readthedocs.io/en/latest/installation.html

```python
# settings.py

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'articles.apps.ArticlesConfig',
    'bootstrap4',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
)

# myform/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')), # 우리의 accounts 보다 아래에 있어야 한다!!
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
```

- makemigrations 말고 바로 migrate!



CLIENT ID : **67e903ceb4ba63c406cab930f3782af0**

SECRETE KEY : aLOS9VxVkS1WmBBqrWlogVqYgz8JCA6i

<kakaodeveloper>

https://developers.kakao.com/apps/360438/settings/user

- 로그인 redirect url

http://127.0.0.1:8000/oauth[×](https://developers.kakao.com/apps/360438/settings/user#)

https://127.0.0.1:8000/oauth[×](https://developers.kakao.com/apps/360438/settings/user#)

http://127.0.0.1:8000/accounts/kakao/login/callback/
  