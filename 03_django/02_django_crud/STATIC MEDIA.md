# STATIC / MEDIA

app_name /templates/app_name/index.html

app_name/static/app_name/sample.png



## image upload

## NULL

- 기본 값 : False

- DB 와 관련되어 있다.(Databased-related)
- 주어진 컬럼이 NULL 값을 가질 것인지를 결정.

## BLANK

- 기본 값 : False

- **데이터 유효성**과 관련되어 있다.(Validation-related)
- `full_clean()` / `is_valid()` 처럼 유효성 검사 메서드가 호출될 때 유효성 검사에 사용된다.



`null=True, blank=False`

- DB 내에서는 해당필드가 NULL 을 사용하지만, 웹 사이트에서는 HTML INPUT 태그에 `required` 속성이 필요하다라는 것을 의미한다.

**주의사항**

- **문자열 기반 필드(CharField, TextField ..)에는 `null=True` 금지**
- 이렇게 정의하게 되면 문자열 기반 필드는 `데이터 없음` 에 대한 값이 2가지가 된다. None 과 빈 문자열을 갖게 된다. 
- 데이터 없음에 대한 조건이 2가지면 중복이기 때문에 문자열 기반 필드는 NULL 이 아닌 빈 문자열을 사용하는게 장고의 컨벤션이다.

```python
class Person(models.Model):
    name = models.TextField(black=True) # null=True 는 금지
    birth = models.DateField(null=True, black=True)
    # 문자열 기반 필드가 아닌 숫자 필드이기 때문에 가능.
```

# pillow

- image 필드를 사용할 때 필수로 필요한 패키지



## media 파일 경로

### `article.image.url` == `/media/sample.jpg`

이미지도 edit 을 통해 새로운 이미지로 수정할 수는 있지만, text 와는 다르게 수정할 때 이미지를 무조건 업로드 하지 않으면 에러가 발생한다.(글만 수정하는 건 안된다는 의미)

- 이미지는 바이너리 데이터(하나의 덩어리)라서 텍스트처럼 **일부만 수정하는게 불가능**. 그렇기 때문에 html input 태그에 value 속성으로 수정하는 방식이 아니고, 새로운 사진으로 덮어 씌우는 방법을 사용.
- `<input type=file>`가 `value=""`를 지원하지 않는다.
- 정말 글만 수정하고 싶다면 이전과 똑같은 이미지를 업로드하면 된다.



# 문제 : 이미지 필드 설정 이전에 작성했던 게시글의 detail 페이지가 동작하지 않는다. (article.image.url 을 불러오지 못하기 때문)

### 해결 1 : static 파일로 이미지가 없을 때 대신 사용할 이미지를 미리 넣어둠.

### 해결 2 : 템플릿에서 {% if %} 문으로 article.image 가 존재하는 경우만 이미지를 출력하도록.



## image resizing

- pillow - 제일 먼저 설치
- pilkit : pillow 를 쉽게 쓸 수 있도록 도와주는 라이브러리 - 두번째 설치
- django-imagekit : 이미지 helper 를 제공하는 django app - 세번째 설치
- **설치순서가 중요**



## 1. html 태그로 직접 사이즈 조정

- 원본은 그대로 저장되어 있고 보여지는 사이즈만 조정하는 것이기 때문에 근본적인 해결책이 아니다.

## 2. 업로드 할 때 이미지 자체를 resizing 해서 저장

#### 2.1 원본 x / 썸네일 o

#### 2.2 원본 o / 썸네일 o



# 이미지 업로드 경로 커스텀

`instance.pk`는 처음 레코드가 작성되는 순간에는 PK 값이 없기 때문.

`media/articles/None/images` 로 저장이 되버린다.

- 실제 개발에선 로그인을 통해 유저 정보를 받고, `instance.user.pk` 또는 `instance.user.username`처럼 업로드한 유저의 정보로 폴더를 구조화하는 경우가 많다.