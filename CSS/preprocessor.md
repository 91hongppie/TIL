# stylus

- install

  - ```bash
    npm install stylus -g
    ```

  - permission denied 에러가 뜨면 앞에 sudo를 붙여준다.

  - ```bash
    sudo npm install stylus -g
    ```

- Use

  - ```bash
    stylus -w pp.styl -o pp.css
    ```

  - -w : pp.styl 파일을 실시간으로 확인하며 변경사항이 있을 경우 pp.css 파일도 변경된다.

  - pp.css 파일을 한번만 저장하고 싶으면 -w를 빼주면 된다.

