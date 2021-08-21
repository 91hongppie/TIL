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