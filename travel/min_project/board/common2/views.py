from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from common2.forms import UserForm


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #로그인
        user = authenticate(username=username, password=password)

        if user is not None:        # user가 있으면
            login(request, user)    # 로그인
            return redirect('/')
        else:
            error = "아이디와 비밀번호를 확인해 주세요"
            context = {'error': error}
            return render(request, 'common2/signin.html', context)
    else:
        return render(request, 'common2/signin.html')

def signout(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() # 회원 가입 저장
            # 가입 후 자동 로그인
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common2/signup.html', context)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #회원 가입 저장
            # 가입후 자동 로그인
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'common2/signup.html', context)