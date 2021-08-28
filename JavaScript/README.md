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

- 기계 안에서 쓰면 새로 생성되는 오브젝트를 뜻함

  - 기계란? - 오브젝트 생성 기계(Constructor)

  - ```javascript
    var 어쩌구 = {}
    
    function 기계() {
      this.이름 = 'Kim'
    }
    ```

  - this.이름 = 기계로부터 새로 생성되는 오브젝트(Instance)

  - 사용 방법

    - ```javascript
      var 오브젝트 = new 기계();
      ```

    - console에 찍어보면 기계가 나온다.

- 이벤트 리스너

  - ```html
    <div>
    </div>
    <button id="버튼">버튼</button>
    <script>
      document.getElementById('버튼').addEventListener('click', function (e) {
        console.log(this);
        console.log(e.currentTarget)
      })
    </script>
    ```

  - 이벤트리스너 안에서 this를 쓰면 e.currentTarget이다.

  - e.currentTarget = 지금 이벤트가 동작하는 html 태그, 여기서는 document.getElementById('버튼')

  - Case study 1

    - ```html
      <div>
      </div>
      <button id="버튼">버튼</button>
      <script>
        document.getElementById('버튼').addEventListener('click', function (e) {
          var 어레이 = [1, 2, 3];
          어레이.forEach(function(a) {
            console.log(a);
            console.log(this)
          })
        })
      </script>
      ```

    - functions(a) = 콜백 함수

    - console.log(a) = 1, 2, 3 이 출력된다.

    - console.log(this) = window가 출력된다.

      - 함수가 쓰인 위치에 따라 this값이 변한다.
      - forEach내의 함수는 그냥 일반 함수(전역 함수)기 때문에 window가 출력된다.

  - Case study 2

    - 오브젝트 내에서 콜백함수를 쓴다면 this 는?

    - ```html
      <div>
      </div>
      <script>
      
      var 오브젝트 = {
        이름들 : ['김', '이', '박'],
        함수 : function() {
          오브젝트.이름들.forEach(function() {
            console.log(this)
          })
        }
      }
      
      오브젝트.함수()
      </script>
      ```

    - console.log(this) = window

    - forEach 내의 함수는 근본없는 일반 함수이기 때문에 this는 window가 된다.

    - ```html
      <div>
      </div>
      <script>
      
      var 오브젝트 = {
        이름들 : ['김', '이', '박'],
        함수 : function() {
          오브젝트.이름들.forEach(() => {
            console.log(this)
          })
        }
      }
      
      오브젝트.함수()
      </script>
      ```

    - forEach 내에 화살표 함수로 하면 내부의 this 값을 변화시키지 않고 외부 this 값 그대로 재사용 가능하다.

    - 이전에는 화살표 함수를 사용할 수 없었기 때문에 bind, call을 썼다.
