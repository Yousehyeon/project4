from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from review.forms import ReviewForm, AnswerForm
from review.models import Review



def index(request):
    return render(request, 'review/index.html')
    # return HttpResponse("kang 인덱스") - 테스트용 text

# review 후기/댓글 게시판
def review_list(request):
    # review_list = Review.objects.all() # 모든 데이터 조회하기
    # 작성일을 기준으로 내림차순 정렬
    review_list = Review.objects.order_by('create_date')
    context = {'review_list': review_list}
    return render(request, 'review/review_list.html', context)

# review 상세페이지
def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    context = {'review': review}
    return render(request, 'review/review_detail.html', context)

# review 등록
def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)    #가저장
            review.create_date = timezone.now()
            review.save()   #실제 저장
            return redirect('review:review_list') #index 경로로 이동
    else:   #request.method == "GET"
        form = ReviewForm()
    context = {'form':form} # context 변수에 딕셔너리 자료 저장
    return render(request, 'review/review_form.html', context)

# review 댓글 달기
def answer_create(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == "POST":
        form = AnswerForm(request.POST) #폼에 입력된 데이터 전달받음
        if form.is_valid():
            answer = form.save(commit=False)    #가저장
            answer.review = review              #외래키 저장
            answer.create_date = timezone.now()
            answer.save()   #실제 저장
            return redirect('review:review_detail', review_id=review_id)
            #해당 id 경로로 이동
        else:
            form = AnswerForm()
        context = {'review':review, 'form':form}
        return redirect(request, 'review/review_detail.html', context)






