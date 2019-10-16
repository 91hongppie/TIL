# 빈 DATABASE 만들기

```bash
# sqlite3 켜기
sqlite3
# tutorial 이라는 이름의 DB 만들기 
sqlite3 tutorial.sqlite3

.databases
# 테이블 확인
.tables
# csv 모드 변경
.mode csv
# 테이블 생성
.import 파일명.csv 테이블이름
# 테이블 전체 조회
SELECT * FROM examples;
# 테이블 예쁘게 조회
.headers on
.mode column
SELECT * FROM examples;
```

## TABLE 생성

```bash
CREATE TABLE table이름 (
id INTEGER PRIMARY KEY,
name TEXT
);
# 삭제된 id 를 재사용하지 않는다면 (특정한 요구사항이 없다면 사용하지 않는다.)
CREATE TABLE table이름 (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
);
```

### `.` : sqlite3  프로그램의 기능을 실행하는 것

### `;` : 세미콜론 까지가 하나의 명령(Query)으로 간주

-  SQL 문법은 소문자로 작성해도 된다.(단 , 대문자를 권장)
- 하나의 DB에는 여러개의 table 이 존재한다.

## 테이블 조회

- 테이블 목록 조회

  ```bash
  .tables
  ```

- 테이블 및 Schema 조회

  ```bash
  .schema 테이블이름
  ```

  

## TABLE 삭제(DROP)

```bash
# 특정 테이블 삭제
DROP TABLE table이름;
```

## DATA 추가(INSERT)

```bash
INSERT INTO table이름 (column1, column2, ...) 
# 모든 컬럼을 선택하고 싶으면 (column1, column2, ...) 생략 가능
	VALUES (value1, value2, ...);
```

## DATA 조회(SELECT)

### id 보이게 하기

```bash
SELECT rowid, * FROM classmates;
```

- id `INTEGER PRIMARY KEY` : rowid 를 대체 
  - INSERT INTO table이름 (column1, column2, ...)  에서 (column1, column2, ...) 를 생략할 때 id 도 직접 입력해줘야하기 때문에 그냥 rowid 를 쓰는게 좋다.

```bash
# 특정 column 조회
SELECT column1, column2 FROM table이름;
# 원하는 개수만큼 column 가져오기
SELECT column1, column2 FROM table이름
LIMIT 1;
# 특정 위치에서 원하는 개수만큼 가져오기
SELECT column1, column2 FROM table이름
# 세번째 행의 정보를 가져온다.
LIMIT 1 OFFSET 2;
# 특정 값만 가져온다
SELECT column1, column2 FROM table이름
WHERE column=? ; 
# 특정 값을 중복없이 가져온다
SELECT DISTINCT column1 FROM table이름;
```

## DATA 삭제(DELETE)

```bash
DELETE FROM table
WHERE rowid=?;
```

- SQLite 는 기본적으로 일부 행을 삭제하고 새 행을 삽입하면 삭제 된 행의 값을 재사용하려고 시도한다.

## rowid 의 최대값은 64비트 8바이트 실수의 최대값

- 9,223,372,036,854,775,807(922경)
- INSERT INTO 를 한다면
  1. AUTOINCREMENT 가 없을 때 : 중간에 없는 ID 를 재사용하므로 에러가 나지 않을 것.
  2. AUTOINCREMENT 가 있을 때: 최대 레코드를 넘어서기 때문에 에러가 발생.

## DATA 수정(UPDATE)

```bash
UPDATE table
SET column1=value1,column2=value2,...
WHERE condition;
```

# WHERE 문 심화

Q. users에서 age 가 30 이상인 사람만 가져온다면?

```bash
SELECT * FROM users
WHERE age >= 30;
```

Q.users 에서 age 가 30 이상인 사람의 이름만 가져온다면?

```bash
SELECT first_name FROM users WHERE age>=30 ;
```

Q.users 에서 age가 30 이상이고 성이 김인 사람의 성과 나이만 가져온다면?

```bash
SELECT last_name,age FROM users WHERE last_name='김'and age>=30;
```

## Expressions

```bash
# 갯수 세기
SELECT COUNT(column) FROM table;
# 평균 
SELECT AVG(column) FROM table;
# 합
SELECT SUM(column) FROM table;
# 최소값
SELECT MIN(column) FROM table;
# 최대값
SELECT MAX(column) FROM table;
```

## LIKE(wild cards)

- 정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환한다.

  ```bash
  SELECT * FROM table
  WHERE column LIKE '조건';
  ```

### 와일드 카드 2가지 패턴

- `-` : 반드시 이 자리에 한 개의 문자가 존재해야 한다.
- `%` : 이 자리에 문자열이 있을수도, 없을수도 있다.
  - `2%` : 2로 시작하는 값
  - `%2` : 2로 끝나는 값
  - `%2%` : 2가 들어가는 값
  - `_2%` : 아무값이나 들어가고 두번째가 2로 시작하는 값
  - `1___` : 1로 시작하고 4자리인 값
  - `2_%_%/2__%` : 2로 시작하고 적어도 3자리인 값

## ORDER(정렬)

```bash
SELECT column FROM table
ORDER BY column1,column2 ASC|DESC
# ASC : 오름차순(default) , DESC : 내림차순
```



```bash
# users에서 나이를 오름차순으로 상위 10 개만 보여주기
SELECT * FROM users ORDER BY age ASC LIMIT 10;
# users에서 나이순, 성 순으로 오름차순 정렬하여 상위 10개만 뽑아보면?
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
```

## ALTER

## 1. 테이블명 변경

```bash
ALTER TABLE exist_table # 현재 테이블 이름
RENAME TO new_table; # 바꿀 테이블 이름
```



## 2. 새로운 column 추가

```bash
ALTER TABLE table
ADD COLUMN col_name datatype; # datatype = TEXT, INTEGER, DATETIME ...

# 기존 데이터에 NOT NULL 조건으로 인해 NULL 값으로 새로운 컬림이 추가될 수 없으므로 아래와 같은 에러가 발생한다. NOT NULL 조건을 없애거나 기본값(DEFAULT)을 지정해야 한다.
ALTER TABLE news ADD COLUMN updated_at DATETIME NOT NULL;
Cannot add NOT NULL column with default value NULL
```

- NOT NULL 조건을 빼면 정상적으로 추가된다.

  ```bash
   ALTER TABLE news ADD COLUMN created_at DATETIME;
  ```

  

- DEFAULT 값을 준다.

  ```bash
  ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;
  ```

  