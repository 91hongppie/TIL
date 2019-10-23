# User - Article

## 1 : N (Article: Comment)

- Article 에서 User 에 대한 외래키 를 가지고 있어야한다.- 

## django 가 서버가 켜질 때 초기화 순서(시험이랑 관련없음)

1. `INSTALLED_APPS`의 각 항목을 imports 합니다. (위에서 아래로)
   - 이 과정에서 직간접적으로 모델을 import 해선 안된다.
   - 1번 단계에서 app 을 import 하는 동안에 불필요한 제약들을 피하기위해 이 단계에서는 모델을 가져오지 않는다.
2. 각 어플리케이션의 models 를 import 한다.
   - **2단계가 완료가 되면**, `get_model()`과 같은 모델에서 작동하는  APIs 를 사용할 수 있게 된다.
3. `AppConfig`의 ready() 메서드를 실행한다.

### get_user_model() 을 사용할 때 과정

1. 1단계에서 articles 부터 import 시작
2. 2단계에서 articles 부터 model 을 import 시작
3. 2단계에서 accounts 부터 models 를 import 시작 ??
   - 2단계가 완료된 후에야 get_user_model() 을 사용할 수 있는데 아직 accounts app 이 INSTALLED APP 의 작성 순서 때문에 아직 IMPORT 가 완료되지 않은 상황이라 get_user_model() 이 어떤 User model 을 return  해야 하는지 django 가 알 수 없는 상태이다.

`get_user_model()`

- return 값이 `class`



`settings.AUTH_USER_MODEL`

- return 값이 `str`



결론

- 모든 곳에서 User model 을 호출할 때는 `get_user_model()` 사용
- 단 models.py 에서만 `settings.AUTH_USER_MODEL` 사용



## gravatar: 프로필 이미지 

 https://en.gravatar.com/ 

- ModelForm Custom
- Custom template tags and filters

### Model relationships

1. Many-to-one
2. Many-to-many



#### User Article (1:N)

- article에서 user를 불러올 때  : article.user
- user 에서 article 을 불러올 때 : user.article_set()

#### User : Article = M : N

- User 는 여러 개의 Article 에 LIKE 할 수 있고
- Article 은 여러 User 로 부터 LIKE 받을 수 있다.



### **모델링은 현실 세계를 최대한 유사하게 반영하기 위해서 해야한다.**`

#### 환자와 의사의 예약 시스템을 구축하라는 프로젝트

# M : N

## 1. 1:N의 한계

## 2. 중개모델 생성

## 3. 중개 모델을 직접 거치지 않고 바로 가져올 수는 없을까?

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- `through` option
- MTOM(many to many) 필드는 실제 물리적인 필드가 db에 생기는 것이 아니다.

## 4. Doctor 도 patients로 참조할 수 없을까?

- `related_name` 
  - 참조되는 대상이 참조하는 대상을 찾을 때(역참조), 어떻게 불러올지에 대해 정의한다.
  - 필수적으로 사용하는건 아니지만, 필수적인 상황이 발생할 수 있다.

## 중개모델은 필요 없는가? 아니다

- 예약한 시간 정보를 담는다거나 하는 경우(==추가적인 필드가 필요한 경우) 에는 반드시 중개모델을 만들어서 진행을 해야되는 상황도 있다. 다만 그럴 필요가 없는 경우 위와 같이 해결할 수 있다.



# LIKE

- user 는 여러 article 에 좋아요를 누를 수 있고
- article 은 여러 user 로부터 좋아요를 받을 수 있다.

`article.user` => 게시글을 작성한 유저 - 1:N 

`aritcle.like_users` => 게시글에 좋아요 한 유저 - M:N

`user.like_articles` => 유저가 좋아요를 누른 게시글(역참조, related_name) - M:N

`user.article_set` => 유저가 작성한 게시글(역참조) - 1:N