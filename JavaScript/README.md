# JavaScript

## this

- 그냥 쓰거나 함수 안에서 쓰면 {window} <- 기본 함수들 수납공간

  - js 파일 최상단에 'use strict' 를 작성하면 js를 엄격하게 실행한다.
    - 변수를 선언하지 않고 값을 할당할 수없다.
    - use strict 모드에서 일반함수 내에서 this를 쓰면 undefined

- 오브젝트 내 함수(메소드)안에서 쓰면 this는 그 함수를 갖고있는 오브젝트를 가리킨다.

- 오브젝트 내의 오브젝트 내에 함수를 넣었을 때 this는 함수를 가지고 있는 오브젝트를 뜻한다.

  - ```javascript
    var object = {
      data : {
        함수 : function() {
          console.log(this)
        }
      }
    }
    ```

  - ```javascript
    이렇게도 쓸 수 있다.
    var object = {
      data : {
        함수() {
          console.log(this)
        }
      }
    }
    ```

  - data가 출력된다.

- 화살표 함수로 하면 this 값을 새로 만들지 않는다. 그냥 상위 요소의 this 값을 물려 받아서 쓴다.

  - ```javascript
    var object = {
      data : {
        함수 : () => {
          console.log(this)
        }
      }
    }
    ```

  - window가 출력된다.

- 함수나 변수를 전역공간에서 만들면 { window } 에 보관한다.

