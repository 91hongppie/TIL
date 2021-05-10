# 190801 workshop

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>workshop</title>
</head>
<body>
  <style>
    #ssafy > p:nth-child(2) {
      color: red;
    }
  </style>
  <div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
</body>
</html>
```

![result](C:\Users\student\Desktop\TIL\homeworkshop_190801\result.PNG)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>workshop</title>
</head>
<body>
  <style>
    #ssafy > p:nth-of-type(2) {
      color: blue;
    }
  </style>
  <div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>
  </div>
</body>
</html>
```

![result_2](C:\Users\student\Desktop\TIL\homeworkshop_190801\result_2.PNG)

## :nth-child(n)

- el 태그의 부모의 자식들 중, n번째 자식이 el 이라면 선택!
- 아닌 경우 선택하지 않음

## :nth-of-type(n)

- el 태그의 부모의 자식들 중 el 인 것들 중에서 n 번째를 선택