# MongoDB

## 맥 환경

### 설치하기

#### homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

#### MongoDB

```bash
brew tap mongodb/brew
```

```bash
brew install mongodb-community
```

#### MongoDB 실행하기

```bash
brew services start mongodb-community
```

#### 접속하기

[http://localhost:27017](http://localhost:27017/) 에 접속했을 때

```markdown
It looks like you are trying to access MongoDB over HTTP on the native driver port.
```

이 문구가 뜨면 성공