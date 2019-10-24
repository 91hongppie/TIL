# HASH TAG



## 수정 될 때는 게시글의 hashtag 전체를 삭제한 후 다시 등록하는 과정.

```python
words = ['#안녕', '하세요', '#저는', '#누구', '입니다']
for word in words:
    if word.startwith('#'):
        hashtag, created = Hashtag.objects.get_or_create(content=word)
        article.hashtags.add(hashtag)
return redirect(detail)
```

## get_or_create(defaults=None, **kwargs)

- 주어진 kwargs 로 객체를 찾으며 필요한 경우 하나를 만든다.
- `(object, created)` 형태의 튜플을 리턴한다
- object 는 검색 또는 생성된 객체이고, created 는 새 객체 생성 여부를 지정하는 boolean 값이다.(새로 만들어진 object 라면 True, 기존에 존재하던 object 라면 False)
- 단, 이 메서드는 DB 가 키워드 인자의 `unique` 옵션을 강제하고 있다고 가정하고 실행된다.
- 이는 요청이 병렬로 작성될 때 및 중복 코드에 대한  문제 방지로 중복 오브젝트가 작성되는 것을 예방한다.



## unique

- True 인 경우 이 필드는 테이블 전체에서 고유한 값이어야 한다.
- 유효성 검사 단계에서 실행되며 중복 값이 있는 모델을 저장하려고 하면 .save() 메서드로 인해 `IntegrityError`가 발생한다.
- ManytoManyField 및 OneToOneField 를 제외한 모든 필드 유형에서 유효하다.



## #스타벅스

->`<a href="/articles/{hashtag.pk}/hashtage/">{hashtag.content}</a>`





CLIENT ID = d97643eee0735a9bd5f41100c6387730 

SECRET KEY =  Cv2WGnBCoZtOP7XdTnO6KZl1JiXjQtbj 