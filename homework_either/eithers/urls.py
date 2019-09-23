from django.urls import path
from . import views


app_name = 'question'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:question_pk>/', views.detail, name='detail'),  
    path('<int:question_pk>/answers_create/', views.answers_create, name='answers_create'),
    path('<int:question_pk>/answers_delete/<int:answer_pk>', views.answers_delete, name='answers_delete'),
    
] 