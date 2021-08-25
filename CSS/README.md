# box-sizing

## box

- 태그가 차지하는 영역

- ```css
  border: 1px solid gray;
  ```

- 위의 문법으로 확인할 수 있다.

## box-sizing

- ```css
  * {
    box-sizing: border-box
  }
  ```

- \* = 전체 태그

- box-sizing

  - border-box = 객체의 너비나 높이를 지정할 때 border 까지 포함한 너비나 높이를 지정한다.
  - content-box = 객체의 너비나 높이를 지정할 때 내부 content의 크기를 지정하며 border가 있을 경우 지정한 너비나 높이에 border의 크기가 추가된다.



# Flex

- Flex를 사용하기 위해서는 태그가 두 단계가 필요하다

  ```html
  <container>
  	<item></item>
    <item></item>
  </container>
  ```

  

| container       | item        |
| --------------- | ----------- |
| display         | order       |
| flex-direction  | flex-grow   |
| flex-wrap       | flex-shrink |
| flex-flow       | flex-basis  |
| justify-content | flex        |
| align-items     | align-self  |
| align-content   |             |

## flex-wrap

1. nowrap = item이 부모요소를 벗어나더라도 한줄에 배치한다.
2. wrap = container의 크기보다 item의 크기가 크면 줄바꿈 된다.
3. wrap-reverse = wrap 반대로(위에 있는 객체들이 밑으로 내려간다.)



## align-items (위 아래 위치 조정)

1. flex-start = 각각의 아이템들이 자신의 컨텐트 크기에 맞는 크기를 갖고 처음부분에 정렬
2. flex-end = 각각의 아이템들이 자신의 컨텐트 크기에 맞는 크기를 갖고 끝부분에 정렬
3. center = 각각의 아이템들이 자신의 컨텐트 크기에 맞는 크기를 갖고 가운데 부분에 정렬
4. baseline = 아이템들의 컨텐트의 밑줄을 한 줄에 맞춰서 정렬
5. stretch =



## justify-content (오른쪽 왼쪽 위치 조정)

1. flex-start = 아이템들을 왼쪽으로 배치
2. flex-end = 아이템들을 오른쪽으로 배치
3. space-between = 
4. center = 아이템들을 가운데 배치
5. space-around



## align-content

#### 같은 행에 있는 아이템들을 하나의 그룹으로 인식하고 그룹과 그룹 사이의 정렬을 결정한다.

1. flex-start
2. flex-end
3. center
4. space-between
5. space-around
6. stretch

# Properties for the flex items

## align-self

### 특정한 아이템만 예외적으로 다르게 값을 주고 싶을 때 사용

1. auto
2. flex-start
3. flex-end
4. center
5. baseline
6. stretch



## flex

```css
.item { flex: flex-grow [flex-shrink] [flex-basis]; }
```

## flex-grow

- container의 크기에 맞게 1/n하여 item을 채운다.
- flex-grow: 1 = container의 안에 요소를 꽉 채운다.
- flex-grow: 0 = container의 안에 요소들을 요소의 크기에 따라 맞추지 않고 채운다.

## flex-basis

- item요소의 최대 크기
- flex-grow를 같이 쓰면 무시되는거 같다.

## flex-shrink

- flex-shrink: 0 = 아이템의 크기가 브라우저의 크기에 따라 변하지 않는다.
- flex-shrink: 1 = 아이템의 크기가 브라우저의 크기에 따라 변한다.
- flex-shrink: 1,  flex-shrink: 2 가 있으면 1과 2의 비율로 변형된다.

## order

#### flex 내의 아이템 순서 배치를 바꿀 수 있다.





# mediaquery

- 최대 너비 500px 까지 적용

```css
@media (max- width:500px) {
      body {
        background-color: red;
      }
    }
```

- 최소 너비 500px 이상일 때

```css
    @media (min-width:500px) {
      body {
        background-color: red;
      }
    }
```

- Cascading - 순서를 생각해서 작성해야한다.
- 최대값이 더 작은 것을 뒤에 작성한다.

```css
    @media (max-width:600px) {
      body {
        background-color: green;
      }
    }
    @media (max-width:500px) {
      body {
        background-color: red;
      }
    }
```



- mediaquery 모바일에 적용하기
- head에 아래의 meta 태그를 추가한다.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```







# float

- 이미지를 본문 내에 자연스럽게 삽입하기 위해서 사용한다.
- 레이아웃을 잡을 때 많이 사용한다. (flex에 의해서 사용빈도가 감소)

```html
<!DOCTYPE html>
<html>

<head>
  <style>
    img {
      width: 300px;
      float: right;
      margin: 20px;
    }
    p {
      border: 1px solid gray;
    }
  </style>
</head>

<body>
  <img src="sample.jpg" alt="">
  <p>
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ab quis omnis quibusdam excepturi consectetur illum soluta
    expedita non, animi placeat saepe nemo. Illum sint alias quod assumenda nulla obcaecati laborum nostrum quaerat rem
    enim quasi sunt, dolores nemo, dolore,
  </p>
  <p style="clear:right">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus molestias dolorem eaque cumque voluptate vitae
    et? Ad, esse laborum aliquid blanditiis asperiores officia, quod ipsum harum, obcaecati autem quis qui.
  </p>
</body>

</html>
```

- float를 right로 하면 본문의 오른쪽에 삽입한다.

  - ```css
    float: right;
    ```

  - 본문은 이미지를 피하여 왼쪽에 나타난다.

- clear를 right로 하면 float를 right로 한 것을 무시한다. 자신의 오른쪽에 이미지가 들어오지 못하게 한다.

  - ```css
    clear: right:
    ```

  - float: right한 객체가 있을때 float를 무시한다.





# background

- background-color
  - 백그라운드 컬러를 설정한다.
- background-image
  - background-img: url(이미지 주소)
  - 위의 형식으로 입력하여 배경 이미지를 넣어준다.
- background-repeat
  - no-repeat - 이미지를 반복하여 보여주지 않는다.
  - repeat : 이미지를 반복하여 보여준다.
  - repeat-x - 이미지를 x 축으로만 반복한다.
  - repeat-y - 이미지를 y 축으로만 반복한다.

- background-attachment
  - fixed  - 스크롤을 이동해도 이미지는 그 자리에 고정
  - scroll - 스크롤을 이동하면 이미지가 같이 움직인다.
- background-size
  - cover - 해당 영역을 이미지가 꽉 채우게 한다.
  - contain - 해당 영역에 이미지가 모두 표시되게 한다.
- background-position
  - left top - 왼쪽 위에 정렬
  - left bottom - 왼쪽 아래 정렬
  - right top - 오른쪽 위에 정렬
  - right bottom - 오른쪽 아래 정렬
- background
  - background: [color] [image] [repeat] [attachment] [position] / [size]



# filter

```css
-webkit-filter: 크롬이나 사파리의 브라우저에서 적용되는 필터
-o-filter: 오페라 브라우저에서 적용되는 필터
filter: 위의 것을 제외한 모든 것에 적용되는 필터
```



- blur()
  - 블러 효과를 적용
- brightness()
  - 밝기 조절
- contrast()
  - 이미지의 대비 조정
- drop-shadow()
  - 이미지에 그림자 효과 적용
  - filter: drop-shadow([offset-x] [offset-y] [blur-radius] [color]
    - [offset-x] [offset-y] (필수)
      - 그림자 오프셋 설정 offset-x는 가로 길이 음수일 경우 그림자가 왼쪽에 배치, offset-y는 세로길이 음수일 경우 그림자가 위에 배치
    - [blur-radius] (선택)
      - 그림자가 흐려지는 반경 클수록 흐려지는 반경이 커지고 그림자가 옅어진다.
    - [color] (선택)
      - 값을 지정하지 않았을 때의 색상은 브라우저마다 다르다. *사파리는 기본으로 투명한 그림자를 사용한다.
- grayscale()
  - 이미지를 흑백으로 전환
- hue-rotate(0~360deg)
  - 이미지의 색조 회전, 0deg일 경우 이미지가 그대로 유지
- invert()
  - 이미지의 색을 반전, 100%일 경우 색을 정반대로 반전
- opacity()
  - 이미지의 불투명도 설정, 0%일 경우 완전 투명
- saturate()
  - 이미지의 채도를 변경, 0%일 경우 완전 무채색
- sepia()
  - 이미지를 세피아로 변경, 100%일 경우 완전한 세피아



# transform

- 엘리먼트가 block이거나 inline-block에만 동작한다.

- [참고 자료](https://codepen.io/vineethtrv/full/XKKEgM)



# transition

```css
transition-property: transition을 적용할 범위 [all, transform, font-size ...] - all이면 모든 변화에 transition이 적용
transition-duration: 0.1s - 변화가 완료되는데 0.1초가 걸린다.
```

```css
transition: all 1s 위의 두개를 한번에 작성
transition: transform 1s, font-size 0.1s - transform 변형이 완료되는데 1초가 걸리고 font-size가 변형이 완료되는데는 0.1초가 걸린다.
```

- transition-property
  - transition을 적용할 범위
- transition-duration
  - 트랜지션을 수행하는데 걸리는 시간
- transition-delay
  - 주어진 시간 후에 트랜지션을 수행한다.
- transition-timing-function
  - 트랜지션을 수행하는 시간에 다양한 옵션 부여
  - [참고자료](https://matthewlein.com/tools/ceaser)







# link

```html
<link rel="stylesheet" href="style.css">
```

- html 태그에서 css 파일을 불러온다



# import

```css
@import url("style.css")
```

- html 파일에서 head 태그 안의 style 태그 안에서 import를 하여 css 파일을 불러올 수 있다.
- css 파일에서도 다른 css 파일을 import 할 수 있다.
- import 는 css 안에서 다른 css를 로드할 때 사용하는 것 그렇기 때문에 html 파일에서 꼭 style 태그안에 작성해야한다.





# minify

- css코드를 압축하는 것
- vscode 익스텐션을 설치하여 사용한다.
- clean-css를 터미널에서 설치하여 명령어로 사용한다.





# Preprocessor - stylus

- CSS를 더욱 편리하게 사용하기위해 preprocessor을 사용한다.

- stylus install

  - ```bash
    npm install stylus -g
    ```

  - permission denied 에러가 뜨면 앞에 sudo를 붙여준다.

  - ```bash
    sudo npm install stylus -g
    ```

- stylus Use

  - ```bash
    stylus -w pp.styl -o pp.css
    ```

  - -w : pp.styl 파일을 실시간으로 확인하며 변경사항이 있을 경우 pp.css 파일도 변경된다.

  - pp.css 파일을 한번만 저장하고 싶으면 -w를 빼주면 된다.

