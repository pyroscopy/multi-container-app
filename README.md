# 멀티 컨테이너 앱

Flask 웹 애플리케이션과 MySQL 데이터베이스로 구성된 멀티 컨테이너 애플리케이션입니다.

## 시작하기

### 필수 조건
- Docker
- Docker Compose
- Git

### 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/[사용자명]/multi-container-app.git
cd multi-container-app
```

2. 애플리케이션 실행
```bash
docker compose up --build
```

3. 웹 브라우저에서 접속
```
http://localhost:5000
```

4. 컨테이너 실행 & 중지
```bash
# 컨테이너 중지
docker-compose down

# 볼륨 삭제 (기존 데이터 초기화)
docker-compose down -v

# 컨테이너 재시작
docker-compose up -d
```

5. 로그 확인
```bash
# MySQL 컨테이너 로그 확인
docker-compose logs db

# 웹 컨테이너 로그 확인
docker-compose logs web
```

6. DB 접속
```bash
# MySQL 컨테이너에 접속
docker compose exec db mysql -u root -p
# 비밀번호 입력: password
```


## 구성 요소

- **웹 애플리케이션 (Flask)**
  - Python 3.9
  - Flask 웹 프레임워크
  - MySQL 커넥터

- **데이터베이스 (MySQL)**
  - MySQL 8.0
  - 초기 데이터 포함

## 주요 기능

- 메시지 목록 표시
- 데이터베이스 연동
- 컨테이너 간 통신

## 디렉토리 구조

```
multi-container-app/
├── web/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── db/
│   └── init.sql
└── docker-compose.yml
```

## 환경 변수

- **웹 애플리케이션**
  - DB_HOST: 데이터베이스 호스트
  - DB_USER: 데이터베이스 사용자
  - DB_PASSWORD: 데이터베이스 비밀번호
  - DB_NAME: 데이터베이스 이름

- **데이터베이스**
  - MYSQL_ROOT_PASSWORD: 루트 비밀번호
  - MYSQL_DATABASE: 데이터베이스 이름

## 추가 변경 사항

MySQL 컨테이너의 root 사용자 권한을 수정하기 위해 init.sql 파일에 다음 내용을 추가합니다:

```sql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
``` 