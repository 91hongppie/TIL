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

