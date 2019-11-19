## DRF

## DRF-jwt

## cors

```bash
pip install djangorestframework
pip install djangorestframework-jwt
pip install django-cors-headers
```

```python
INSTALLED_APPS = [
    'todos',
    'rest_framework',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```python
# 리퀘스트가 순차적으로 검열을 받는 곳
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

```python
# settings.py
CORS_ORIGIN_WHITELIST = [
]
```

##  this.$session.start() 

- session-id 초기화. 만약 세션이 없이 저장하려고 하면 vue-session 플러그인이 자동으로 새로운 세션을 시작

##  this.$session.set(key,value) 

- session 에 해당 key 에 맞는 값을 저장

##  this.$session.has(key) 

- key(JWT) 가 존재하는지 여부를 확인

##  this.$session.destroy() 

- session 을 삭제

---

## 0. Django

- 회원가입

## 1. Vue -> django

- 로그인 정보(credentials)를 django 서버로 보냄

## 2.  Django

- Vue 에서 온 유저정보에 해당하는 고유한 Web Token 발급

## 3. Django -> Vue

- 해당 유저에 대한 토큰을 Vue 로 보냄

## 4. Vue

- Django 에서 받은 토큰을 vue-session 을 통해 저장 (이 시점부터 vue 에서는 로그인 성공 상태)

## 5. Vue -> Django

- vue-session 에 저장된 토큰을 가지고 django 에 로그인 요청

## 6. Django

- 최초로 보낸 토큰과 일치하는지 여부를 확인(장고 세션에 저장된 토큰 == 요청자의 토큰)
- 일치하면 로그인

---

.start() 를 통해 `session-id`:`sess`+`Date.now()` 가 만들어짐

`.set()` 을 통해 `jwt:jwt 값` 이 만들어짐

---

## 1. Vue instance 생성 (create)

## 2. DOM 에 부착(mounted)

## 3. 업데이트

## 4. 사라짐 (destroy)

## 

### FormData

- 기존 키에 새로운 값을 추가하거나 키가 없는 경우 새로운 키를 추가.(`FormData.append()`)
- `FormData.append(name, value)`
- name : value 에 포함되는 데이터 필드 이름
  - value : 필드 값