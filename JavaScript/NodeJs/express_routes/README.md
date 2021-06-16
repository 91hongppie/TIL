# curl 명령으로 URL로 POST 요청 보내기

```bash
curl --data "firstname=KyuHong&lastname=Jo" http://localhost:3000/signup
```

http://localhost:3000/signup 으로 

```json
{
  "fistname": "KyuHong",
  "lastname": "Jo"
}
```

를 담아 POST 요청으로 보낸다.

