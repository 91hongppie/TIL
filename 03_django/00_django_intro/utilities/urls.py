from django.urls import path
from . import views

urlpatterns = [
    # 원래는 app url 은 아래로 작성해 나간다.
    path('index/', views.index),

]
