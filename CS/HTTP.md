

# HTTP

- 세션 계층 프로토콜(www)
- HTML을 기본 프레젠테이션 계층으로 사용
- 목적
  - 전세계 인터넷에 있는 정보를 탐색
- 발명
  - Tim Berners-Lee가 CERN에서 1980년대 말 ~ 1990년대 초

## 동작

- web 자료를 가져와서(GET) 보여주기 
- web에 자료를 Posting 하기(POST)

## URL(Universal Resource Locator)

- http://formal.kau.ac.kr/comnet/index.html
  - http:
    - 프로토콜 이름
  - //formal.kau.ac.kr
    - 호스트 이름
  - /comnet/
    - 디렉토리 이름
  - index.html
    - 파일 이름
- http://formal.kau.ac.kr:8080
  - //formal.kau.ac.kr:8080
    - 호스트 이름
  - :8080/
    - 포트 번호
    - 생략할 수 있다. (포트번호를 입력하지않고 http를 사용하면 기본적으로 80번 포트를 사용)

## HTTP

/-----------------------------------/ 

​				TCP 연결

/-----------------------------------/ 

클라이언트 ----요청 ---> 서버 

클라이언트 <---응답 ---- 서버

/-----------------------------------/ 

​			TCP 연결 종류

/-----------------------------------/ 

- HTTP Transaction  =  Stateless Protocol - 요청하고 응답을 받으면 끝
- FTP = Statefull Protocol - 요청, 응답 작용을 하면서 서버에서 클라이언트의 정보를 따라간다(자유도가 떨어진다.)



## GET 요청

- 원하는 자원을 가져오는 목적
- 형식 : HTTP 요청 헤더
  - /------------ 헤더--------------/ 
  - GET  /comnet/  HTTP/1.1
    - /comnet/ = 서버상의 자원의 위치
    - 1.1 = HTTP 버전
  - /--------- 헤더의 끝----------/ 
  - host: formal.kau.ac.kr
  - User-agent: Mozila/5.0 (Macintosh: Intel Mac ......)
  - 마지막에 한 줄을 띄우면 헤더의 끝
- 서버의 응답 
  - /------------ 헤더--------------/ 
  - HTTP/1.1 200 ok
  - Last-modified: 날짜
  - Content-length: 487
  - /--------- 헤더의 끝----------/ 
  - 한 줄을 띄고 바디가 들어간다.
  - /------------ 바디--------------/ 
  - 실제 자원 (파일)
  - /--------- 바디의 끝----------/ 
- GET 방식으로 로그인
  - URI (Universal Resource Identifier)
  - http://formal.kau.ac.kr:8080/comnet?id=kau&pwd=kau

## POST 요청

- 자원을 서버에 게시하고 싶을때
  - 게시판에 글 올리기
  - 사진 올리기
  - 웹 브라우저를 이용해 email 보내기
  - 로그인
- 형식 : 
  - /------------ 헤더--------------/ 
  - POST  /comnet/  HTTP/1.1
  - Host: formal.kau.ac.kr
  - User-agent: Mozila/5.0
  - /--------- 헤더의 끝----------/ 
  - 한 줄을 띄고 바디가 들어간다.
  - /------------ 바디--------------/ 
  - 요청 보내는 내용
  - /--------- 바디의 끝----------/ 

