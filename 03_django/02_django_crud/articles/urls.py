from django.urls import path
from . import views

app_name = 'articles' # 반드시 이 이름으로
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), # NEW(GET) + CREATE(POST)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'), # EDIT(GET) + UPDATE(POST)
]