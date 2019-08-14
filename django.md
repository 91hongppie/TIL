# django

- 다용도의
- 안전한
- 확장성 있는
- 완결성 있는
- 쉬운 유지보수
- 포터블한(많은 플랫폼에서 작동할 수 있다.)

## django의 성격

- 다소 독선적 (간결하다. 유연하지 못한 해결책을 제시할 수 있다. django는 독선적에 더 가까움)

- 관용적(여러가지의 컴포넌트를 붙여서 사용할수있다. 최소한의 도움을 준다. 개발자가 처음부터 끝까지 손볼게 많다. 간결하지 못할수 있다. 개발자의 성격이 드러날수 있다.)

  *최근 개발시장은 생산성이 0순위

# 가상환경을 사용하는 이유

## 의존성

1. 본인의 컴퓨터에서 잘 작동하던 프로그램도, 다른 프로그램에 설치 했을 때 잘 동작하리라는 보장이 없음.
2. 파이썬도 같은 버전, 같은 모듈을 쓴다는 보장이 없다.
3. 특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들어서, 그 환경속에서만 모듈을 관리하고, 앱을 실행 시키기 위해 가상환경을 설정한다.
4. 다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른 환경을 만드는 방식으로 진행한다.

# django 가상환경 만들기

- python -m venv (가상환경 경로+이름)
  - python -m venv python 
- git igonore 설정
  - gitignore.io ->  django visualstudiocode
  - .gitignore 파일에 복사 
  - vscode 에서 /* 지운다.
- source venv/Scripts/activate
- pip list 찍어서 확인 깨끗해야함
- pip 업그레이드
- deactivate (비활성화)
- pip install django
- python -m django --version (버전확인)

## django 프로젝트 생성

- django-admin startproject django_intro . (django-admin startproject 는 정해진 코드 . 을 붙이는 이유는 현재 폴더에 생성 안하면 새폴더를 만들어서 생성)

## page 생성

- python manage.py startapp pages
  - 주의사항: 앱의 이름은 복수형으로 만들기
- admin.py
  - 개발자 페이지를 커스터마이징
- models.py
  - 앱에서 사용하는 모델을 정리
- tests.py
  - 테스트 코드 작동하는 곳
- views.py
  - 중간 관리자의 역할
  - 함수 정의

## django 코드 작성 순서

1. views : 만들고자 하는 view 함수 작성
2. urls : views 에서 만든 함수에 주소를 연결
3. templates : 해당 view 함수가 호출 될 때, 보여질 페이지

## variable  routing

- 동적 라우팅
  - {{ name }}

## Django Template Language(DTL)

- django template 에서 사용하는 내장 template system 이다.
- 조건, 반복, 변수  치환, 필터 등 많은 기능을 제공한다.
- for 문이 열리면 닫아줘야한다
  - {% for menu in menus %}
  - {% endfor %}