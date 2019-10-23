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
    # 문자열만 있는 주소는 모든 조건을 포함하고 있다. 그래서 최하단으로 내려야한다.
    path('<username>/', views.profile, name='profile'),
]
