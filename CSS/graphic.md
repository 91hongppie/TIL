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