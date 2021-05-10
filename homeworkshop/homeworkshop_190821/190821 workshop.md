# 190821 workshop

```python
# base.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
<h1>Base is everywhere!</h1>
{% block content %}
{% endblock  %}
</body>
</html>

# one.html
{% extends 'pages/base.html' %}
{% block content %}
  <h1>I am ONE!</h1>
{% endblock  %}

# two.html
{% extends 'pages/base.html' %}
{% block content %}
  <h1>I am TWO!</h1>
{% endblock  %}

# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 원래는 app url 은 아래로 작성해 나간다.
    path('one/', views.one), # url 경로 마지막에 / 를 붙이는 습관
    path('two/', views.two),
]

# project/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]

# views.py

from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'pages/one.html')

def two(request):
    return render(request, 'pages/two.html')
```

