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