# commerce_project(가제) 초기 셋팅

### 1. Python 설치

- python 3.9 버전으로 설치합니다.

### 2. 가상환경 생성 및 활성화

- 해당 프로젝트 루트에서 터미널 커맨드로 venv로 가상환경을 생성합니다.
```shell
$ python -m venv venv
```

- 가상환경을 활성화 합니다.
```shell
# Window 기준
$ venv\Scripts\activate

# macos 기준
$ source venv/bin/activate
```

### 3. 패키지를 설치합니다.
- 패키지 설치를 위해 requirements.txt를 설치합니다.
```shell
$ pip install -r requirements.txt
```

### 4. Docker MySQL로 DB를 연결합니다.
- DataBase 연결은 docker를 사용하여 mysql 이미지를 컨테이너로 사용합니다.
- 먼저, Docker를 설치하고 실행합니다.

   링크 : https://www.docker.com/get-started/

- MySQL docker container 생성 명령어를 실행합니다.
```shell
$ docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -d -p 3306:3306 mysql
```
- docker로 실행한 MySQL은 아래 명령어로 접속합니다.
```shell
$ docker exec -it mysql-container mysql --password=<password>
```
- 접속 후 user 생성 및 권한 부여를 합니다.

예시)
```shell
mysql > create user 'test'@'%' IDENTIFIED BY 'test1234';
Query OK, 0 rows affected (0.01 sec)

mysql > GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.01 sec)

mysql > FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.01 sec)

mysql> exit
```
- ```select host,user from mysql.user;```를 통해 계정 생성 여부를 확인합니다.


- table과 row를 test로 생성하여 데이터가 잘 넘어오는지 확인합니다.

예시)
```mysql
CREATE TABLE IF NOT EXISTS `users` (
  id int(6) AUTO_INCREMENT,
  name varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  PRIMARY KEY(id)
);

INSERT INTO `users` (`name',`email`) VALUES
('john','john@example.com');

```

- 프로젝트에서 MySQL 접속은 config.py를 생성하여 아래와 같이 작성 후 접속 상태를 프로젝트 실행시 접속 상태를 확인합니다.
```python
import pymysql

connection = pymysql.connect(
    host='0.0.0.0',
    port=3306,
    user='test',
    password='test1234',
    db='dbname',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
```

### 5. 프로젝트를 실행합니다.
- 로컬 환경에서 프로젝트 실행은 해당 명령어를 입력합니다.
```shell
$ uvicorn app.hello:app --reload
```
DB 연결과 관련된 에러가 없다면
http://127.0.0.1:8000 url로 브라우저 접속시
```{"message": "Hello!"}```
가 정상적으로 응답됩니다.

