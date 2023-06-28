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
    # 5장 - 질문 수정 url 매핑 추가
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # 질문 삭제 url 매핑 추가
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # 답변 수정/ 삭제 url 매핑
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

]