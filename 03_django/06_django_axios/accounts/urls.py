from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<str:username>/', views.profile, name='profile'), # 이게 맨 위에 있으면 모든 주소에 대해 Page not found 에러 발생! => 문자열만 있는 url은 다른 url들을 먹어버림!! => 가장 아래에 작성!
]
