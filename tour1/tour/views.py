from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime


from tour.forms import QuestionForm, AnswerForm
from tour.models import Question, Answer


# 홈
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("kang 인덱스") - 테스트용 text

# 정보페이지로 이동 - 수도권
def detail_ca(request):
    return render(request, 'tour/detail_ca.html')

# 정보페이지로 이동 - 충청/전라도
def detail_cj(request):
    return render(request, 'tour/detail_cj.html')

# 정보페이지로 이동 - 강원/제주도
def detail_gj(request):
    return render(request, 'tour/detail_gj.html')

# 정보페이지로 이동 - 경상도
def detail_gs(request):
    return render(request, 'tour/detail_gs.html')

# 정보페이지로 이동 - 수도권

# 리뷰 게시판
def question_list(request):
    # question_list = Question.objects.all()
    # return HttpResponse("welcome 안녕")
    # 작성일 기준으로 내림차순 정렬 - -create_date : 작성한 날짜의 역순으로 정렬
    question_list = Question.objects.order_by('-create_date')

    # 페이지 처리
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)    #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'tour/question_list.html', context)


def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'tour/detail.html', context)


# 리뷰 등록
@login_required(login_url='common2:login')  # 로그인 필수(세션)
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)  # 가저장
            question.author = request.user
            question.create_date = timezone.now()
            question.save() # 실제 저장
            return redirect('tour:question_list')  # index 경로로 이동
    else:   # request.method == "GET"
        form = QuestionForm()
    context = {'form': form}    # context 변수에 딕셔너리 자료 저장
    return render(request, 'tour/question_form.html', context)



# 답변 등록
@login_required(login_url='common2:login')  # 로그인 필수(세션)
def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST) # 폼에 입력된 데이터 전달 받음
        if form.is_valid():
            answer = form.save(commit=False)    # 가저장
            answer.author = request.user        # 4장 41쪽 수정
            answer.question = question          # 외래키 저장
            answer.create_date = timezone.now()
            form.save()   # 실제 저장
            return redirect('tour:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'tour/detail.html', context)


# 질문 수정
@login_required(login_url='common2:login') # 오류 나면 login부터 확인 -----------------------
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.author = request.user
            form.save()
            return redirect('tour:detail', question_id=question_id)    # 오류 나면 여기도 확인 -----------------------------------
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'tour/question_form2.html', context)


# 답변 수정
@login_required(login_url='common2:login') # 오류 나면 login부터 확인 -----------------------
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.author = request.user
            form.save()
            return redirect('tour:detail', question_id=answer.question.id)    # 오류 나면 여기도 확인 -----------------------------------
    else:
        form = AnswerForm(instance=answer)
    context = {'form': form}
    return render(request, 'tour/answer_form.html', context)


# 질문 삭제
@login_required(login_url='common2:login')  # 오류 나면 여기 확인 -----------------------------------
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()   # 삭제
    return redirect('tour:question_list')


# 답변 삭제
@login_required(login_url='common2:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return redirect('tour:detail', question_id=answer.question.id)

