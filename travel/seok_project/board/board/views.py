from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from board.forms import QuestionForm, AnswerForm
from board.models import Question


def index(request):
    # 질문 답변 게시판
    # question_list = Question.objects.all()
    # return HttpResponse("welcome 안녕")
    # 작성일 기준으로 내림차순 정렬 - -create_date : 작성한 날짜의 역순으로 정렬
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)

@login_required(login_url='common2:signin')  # 로그인 필수(세션)
def question_create(request):
    # 질문 등록
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 가저장
            question.author = request.user      # 4장 41쪽 수정함
            question.create_date = timezone.now()
            question.save() # 실제 저장
            return redirect('board:index')  # index 경로로 이동
    else:   # request.method == "GET"
        form = QuestionForm()
    context = {'form': form}    # context 변수에 딕셔너리 자료 저장
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common2:signin')  # 로그인 필수(세션)
def answer_create(request, question_id):
    # 답변 등록
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST) # 폼에 입력된 데이터 전달 받음
        if form.is_valid():
            answer = form.save(commit=False)    # 가저장
            answer.author = request.user        # 4장 41쪽 수정
            answer.question = question          # 외래키 저장
            answer.create_date = timezone.now()
            answer.save()   # 실제 저장
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'board/detail.html', context)

