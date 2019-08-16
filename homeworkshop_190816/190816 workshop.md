# 190816 workshop

```python
# views.py

from django.shortcuts import render

# Create your views here.
def push(request):
    return render(request, 'pages/push.html')


def pull(request):
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'pages/pull.html', context)

# project urls.py

from pages import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]

# pages urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('pull/', views.pull),
    path('push/', views.push),
]

# templates
# push.html

<form action="/pages/pull/" method="GET">
  <label for="message">
    <h1>Push Number</h1>
  </label>
  <br>
  <input type="text" name="message">
  <input type="submit" value="push!">
</form>

# pull.html

<h1>Pull Number</h1>
<h2>Pull 해보니 {{ message }} 입니다!!</h2>
```

