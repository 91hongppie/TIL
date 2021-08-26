# fontello

- 폰트를 통해서 아이콘을 표시할 수 있다.

- [사이트](fontello.com)에서 사용하고 싶은 아이콘을 클릭한 뒤에 다운로드 받는다.

- 다운 받은 파일의 압축을 풀고 demo.html 파일을 브라우저에서 작동시킨다.

- show codes 체크박스를 선택하면 아이콘의 unicode가 나온다.

- fontello 를 적용하고 싶은 html 파일에 fontello.css를 링크로 추가하고 꼭 font-family를 "fontello"로 설정한다.

  - ```html
    <link rel="stylesheet" href="css/fontello.css">
    <style>
      body {
        font-family: "fontello";
      }
    </style>
    ```

- body에 아이콘의 코드를 앞의 0을 제거한 뒤에 &#을 붙여서 추가한다.

  - ```html
    <body>
    	&#xe802
    </body>
    ```

- 아이콘처럼 보이지만 폰트로 인식되기 때문에 폰트 사이즈, 컬러를 변경함으로써 변경할 수 있다.

- 모든 태그의 클래스에 이름을 입력하는 것으로도 사용할 수 있다.

  - ```html
    <i class="icon-emo-wink"></i>
    ```

  - 태그의 클래스로 사용하면 font-family를 지정할 필요가 없다.

- animation을 사용하고 싶을 때

  - html 파일에 css 폴더의 animation.css 파일을 로드하고 사용하고 싶은 애니메이션의 클래스를 태그에 추가한다.

- font 만들기
  - svg 파일이 필요하다.
    - [사이트](https://thenounproject.com/)
- fontello.com에서 이전에 다운 받았던 아이콘 보기
  - 사이트 우측 상단에 스패너 모양의 아이콘에서 import 클릭
  - 이전에 다운 받았던 fontello 폴더에서 config.json 파일 열기
  - css 클래스명의 prefix를 변경하고 싶으면 사이트 우측 상단의 스패너 모양 클릭하여 CSS prefix에서 변경하기 





# CSS로 내용물 변경하기

```css
#test:before {
  content: "A"
}
```

- 아이디가 test인 태그의 맨 앞에 A 가 추가된다.

