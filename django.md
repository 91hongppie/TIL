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

## 의존성

1. 본인의 컴퓨터에서 잘 작동하던 프로그램도, 다른 프로그램에 설치 했을 때 잘 동작하리라는 보장이 없음.
2. 파이썬도 같은 버전, 같은 모듈을 쓴다는 보장이 없다.
3. 특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들어서, 그 환경속에서만 모듈을 관리하고, 앱을 실행 시키기 위해 가상환경을 설정한다.
4. 다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른 환경을 만드는 방식으로 진행한다.

## django 가상환경 만들기

- python -m venv (가상환경 경로+이름)
  - python -m venv python 
- vscode python interpreter 설정
- git igonore 설정
  - gitignore.io ->  django visualstudiocode
  - .gitignore 파일에 복사 
  - vscode 에서 /* 지운다.
- source venv/Scripts/activate
- pip list 찍어서 확인 깨끗해야함
- pip 업그레이드
- pip install django
- python -m django --version (버전확인)

## settings.json

```python
{
  "terminal.integrated.cwd": "${workspaceFolder}",
  "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
  "window.zoomLevel": 4,
  "editor.fontFamily": "Hack, Fira Code, Consolas, 'Courier New', monospace",
  "editor.suggestLineHeight": 24,
  "editor.fontLigatures": true,
  "files.insertFinalNewline": true,
  "[html]": {
    "editor.tabSize": 2
  },
  "[css]": {
    "editor.tabSize": 2
  },
  "[django-html]": {
    "editor.tabSize": 2
  },
  // beautify
  "beautify.language": {
    "js": {
      "type": ["javascript", "json"],
      "filename": [".jshintrc", ".jsbeautifyrc"]
      // "ext": ["js", "json"]
      // ^^ to set extensions to be beautified using the javascript beautifier
    },
    "css": ["css", "scss"],
    "html": ["htm", "html", "django-html"]
    // ^^ providing just an array sets the VS Code file type
  },
  // django
  "files.associations": {
    "**/*.html": "html",
    "**/templates/**/*.html": "django-html",
    "**/templates/**/*": "django-txt",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
  },
  "emmet.includeLanguages": {"django-html": "html"},
}
```



## django 프로젝트 생성

- django-admin startproject django_intro . (django-admin startproject 는 정해진 코드 . 을 붙이는 이유는 현재 폴더에 생성 안하면 새폴더를 만들어서 생성)

## page 생성

- python manage.py startapp pages
  - 주의사항: 앱의 이름은 복수형으로 만들기
- app 등록
  - settings 의 INSTALLED_APPS 에 pages의 apps에 클래스 이름 추가
- urls.py 에 from pages import views
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
- if 문도 마찬가지
  - {% if 조건식 %}
  - {% endif %}

## django 서버 열기

- python manage.py runserver



## csrf 사이트간 요청 위조

- 웹 어플리케이션 취약점 중 하나로 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹페이지의 보안을 무력화 시키거나, 수정,삭제 등의 강제적인 작업을 하게하는 공격 방법
- django 는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash 값을 token 으로 부여한다. 이 token 값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다.(403 error)

# static 정적 파일

- image / css/ js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리 없이 그대로 보여주면 되는 파일들

# URL 로직 분리

- 주소/앱/파일명 으로 접근
- 장고의 namespace 오류 : pages 와 utilities 에 동일한 이름의 html 파일이 있을 경우 발생
  - settings.py의 INSTALLED_APPS 의 가장 상단에서 부터 읽는다.

# Django namespace

- templates / static 을 바꿔나감
  - pages 라는 앱의 templates 에 앱 이름과 동일한 폴더 하나 더 만들어 html 파일들 넣기

# Template Inheritance(상속)

- project 에 templates 폴더 생성

- settings.py -> TEMPLATES -> 'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')]

  # 1. Form(GET/POST)

  # 2. POST - csrf_token

  # 3. static (load,{% static %})

  # 4. URL로직 (프로젝트&앱)

  # 5. Namespace(template, static)

  # 6. 상속(block )

# 가상 환경을 집에서 사용하고 싶을 때

- 의존성 기록(구성환경 리스트 만들기)
- pip freeze > requirements.txt
- 의존성 설치
- pip install -r requirements.txt