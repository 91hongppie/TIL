from IPython import embed
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

# 회원가입 폼 가져오기
# Create your views here.

def signup(request):
    # 로그인된 상태로 회원가입 창 들어가지 못하게 막아야함!
    if request.user.is_authenticated: # 인증된 user면 들어오면 안됨...홈으로 돌리기
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            # form.save() 를 통해 반환된 User 클래스의 인스턴스를 auth_login 의 인자로 전달
            # 회원가입과 동시에 로그인상태 유지하기!
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    # 로그인된 상태로 로그인 창 들어가지 못하게 막아야함!
    if request.user.is_authenticated: # 인증된 user면 들어오면 안됨...홈으로 돌리기
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # request먼저 넣고 data넣기(request.POST)
        if form.is_valid():
            # embed()
            auth_login(request, form.get_user()) # form에 login정보 들어있음 => form.get_user()로 로그인정보만 가져오기
            return redirect(request.GET.get('next') or 'articles:index')    # 로그인 성공 후 next query가 있다면 next이후로 넘어가고 아니면 index로 간다..
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_POST # post요청만 받는다.
def delete(request):
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user) # request.user : 유저정보
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)

@login_required # 비로그인 상태로 접근할 수 없게 만든다.
def change_password(request):
    if request.method == 'POST': # 비밀번호 수정
        form = PasswordChangeForm(request.user, request.POST) # 유저정보(request.user), 데이터(request.POST) 순으로 들어감
        if form.is_valid():
            user = form.save() # user로 안받으면 form.user로 해줘야한다!
            update_session_auth_hash(request, user) # 비번 변경 후 로그아웃되지 않고 로그인 상태 유지
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user) # user 정보(request.user) 필요함!
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)

# 프로필 작성 (Detail과 유사)
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username) # 유저 정보 가져오기
    context = {'person': person,}
    return render(request, 'accounts/profile.html', context)