from django.urls import path
from . import views

app_name = 'board'  #  네임 스페이스(소속)

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path('', views.question_list, name='question_list'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('answer/create/<int:question_id>/', views.answer_create,
         name='answer_create'),
]