## http의 특성

1. 비연결지향(connectionless)

2. 상태정보 유지 안함(stateless, 무상태) : 연결이 끊어지는 순간 클라이언트와 서버간의 통신이 끝남(각각 완벽하게 독립적으로 돌아간다.)

때문에 쿠키와 세션 ( 저장매체 )이 생김



## 쿠키(cookie)

- 클라이언트의 로컬에 저장되는 키-값의 작은 데이터파일(유저정보, 날짜 ,.....) -> 아무나 접근할 수 있음..(보안에 취약 -> 중요정보들 세션에 저장)
- 웹페이지에 접속하면 요청한 웹페이지를 서버로부터 받고 쿠키를 로컬에 저장하고, 클라이언트가 재요청시에 웹페이지 요청과 함께 쿠키 값도 함께 전송
- 아이디 자동완성 / 공지 메세지 하루 안보기(하루동안 쿠키 저장 안됨) / 팝업 안보기 체크 / 비로그인 장바구니에 담기 (서버 끄면 지워짐..) 등 지워지거나 유출되도 큰 일은 없을 정보들을 저장

## 세션(session)

- 사이트와 특정 브라우저(클라이언트) 사이의 상태를 유지시키는 것
- 중요정보에 접근하기 위한 인증 키(세션에서 부여한 임시 키_session id)는 쿠키에서 저장
- 일정 시간동안 같은 브라우저로부터 들어오는 일련의 요구를 하나의 상태를 유지하는 기술
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키를 사용해 저장. 클라이언트가 다시 서버에 접속하면 해당 쿠키(session id가 담긴)를 이용해 서버에 session id를 전달한다.
- Django 는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아낸다. 실질적인 session의 database에 기본 설정 값으로 저장된다. (이는 쿠키 안에 데이터를 저장하는 것보다 더 보안에 유리하고, 쿠키는 악의적인 사용자들에게 취약하기 때문 )
- 세션을 남발하면 사용자가 많은 서버일 경우 서버 부하가 발생합니다.
- 쿠키를 지우면 로그아웃은 왜????
  - 서버에서는 session에 사용자 로그인 정보를 가지고 있지만, 그것이 내거라는것을 증명할 session id가 쿠키에서 사라졌기 때문 (쿠키가 임시키를 가지고있지 않기 때문)

## 차이

- 쿠키 : 클라이언트 로컬에 파일로 저장
- 세션 : 서버에 저장(이때 session id는 쿠키의 형태로 클라이언트의 로컬에 저장)

<hr>

### 캐시(cache)

- 가져오는데 비용이 드는 데이터를 한 번 가져온 뒤에는 임시로 저장.
- 사용자의 컴퓨터 또는 중간 역할을 하는 서버에 저장.



# Authentication

https://docs.djangoproject.com/en/2.2/topics/auth/default/#using-the-django-authentication-system

## SIGN-UP

### Authentication(인증) - 신원 확인

- 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

### Authorization(권한, 허가) - 권한 부여

- 가고 싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정



django 에 이미 user관련 form이 만들어져 있음

https://docs.djangoproject.com/en/2.2/topics/auth/default/#module-django.contrib.auth.forms

- user를 create

```python
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)
```



## LOGIN

https://docs.djangoproject.com/en/2.2/topics/auth/default/#how-to-log-a-user-in

- session을 create

```python
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # request먼저 넣고 data넣기(request.POST)
        if form.is_valid():
            # embed()
            auth_login(request, form.get_user()) # form에 login정보 들어있음 => form.get_user()로 로그인정보만 가져오기
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)
```





## LOGOUUT

https://docs.djangoproject.com/en/2.2/topics/auth/default/#how-to-log-a-user-out

- session 삭제

```python
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

### 로그인 사용자에 대한 접근 제한(인증)

https://docs.djangoproject.com/en/2.2/topics/auth/default/#auth-web-requests

- django는 세션과 미들웨어를 통해 인증시스템을 request 객체에 연결한다.
- request는 현재 사용자를 나타내는 모든 요청에서 `request.user`를 제공한다.

`is_authenticated`

- User model 의 속성(attributes)들 중 하나.
- 사용자가 인증되었는지 알 수 있는 방법
- User에는 항상 True / AnonymousUser 에 대해서만 항상 False
- 단, 이것은 권한(permission)과는 관련이 없으며 사용자가 활동중(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않는다.

- `django.contrib.auth.middleware.AuthenticationMiddleware`를 통과했는지 확인한다.

```python
def signup(request):
    # 로그인된 상태로 회원가입 창 들어가지 못하게 막아야함!
    if request.user.is_authenticated: # 인증된 user면 들어오면 안됨...홈으로 돌리기
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            # form.save() 를 통해 반환된 User 클래스의 인스턴스를 auth_login 의 인자로 전달
            # 회원가입과 동시에 로그인상태 유지하기!
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/signup.html', context)

def login(request):
    # 로그인된 상태로 로그인 창 들어가지 못하게 막아야함!
    if request.user.is_authenticated: # 인증된 user면 들어오면 안됨...홈으로 돌리기
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # request먼저 넣고 data넣기(request.POST)
        if form.is_valid():
            # embed()
            auth_login(request, form.get_user()) # form에 login정보 들어있음 => form.get_user()로 로그인정보만 가져오기
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)
```



`next` query string parameter

- @login_required 데코레이터가 기본적으로 인증 성공 후 사용자를 리다이렉트 할 경로를 next 라는 문자열 매개 변수에 저장한다.
- 우리가 url로 접근하려고 했던 그 주소가 로그인하지 않으면 볼 수 없는 곳이라서, django 가 로그인 페이지로 강제로 리다이렉트 했는데, 로그인을 다시 정상적으로 하고 나면 원래 요청했던 주소로 보내주기 위해 keep 해주는 것.



@required_POST 가 있는 함수에 @login_required 가 설정된다면 로그인 이후 "next" 매개변수를 따라 해당 함수로 다시 redirect 되면서 @required_POST 때문에 405 에러가 발생. 



## 회원탈퇴

- user를 db에서 날림
- request.user.delete()

```python
@require_POST # post요청만 받는다.
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```



## 회원수정

`get_user_model()`

- User 를 직접 참조하는 대신 `django.contrib.auth.get_user_model()`를 사용하여 User model을 참조해야 한다.
- 이 함수는 현재 활성화(active) 된 User model을 return 한다.

## 비번변경

- 비밀번호 변경 후 로그아웃 되어버림.
- 비밀번호가 변경되면서 기본 세션과의 회원 인증정보가 일치하지 않게 되어버렸기 때문.

**update_session_auth_hash**

https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.update_session_auth_hash

- 현재 사용자의 인증 세션이 무효화 되는것을 막고, 세션을 유지한 상태로 업데이트.
- 현재 request 와 새로운 session hash 가 생긴 업데이트 된 user 객체를 적절히 업데이트.

## template 정리

