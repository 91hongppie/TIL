# 190814 workshop

```python
# views.py
from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request, 'info.html')

def student(request, name):
    context = {'name': name,}
    return render(request, 'student.html', context)

# urls.py

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('student/<name>/', views.student),
    path('info/', views.info),
    path('admin/', admin.site.urls),
]

# info.html

<h1>우리반 정보</h1>
<h2>Teacher</h2>
<ul>
  <li>NAME</li>
</ul>

<h2>Student</h2>
<ul>
  <li>홍길동</li>
  <li>김길동</li>
  <li>박길동</li>
</ul>

# student.html

<h1>이름 : {{ name }}</h1>
<h3>나이: 28</h3>

```

