# 멀티 컨테이너 앱

Flask 웹 애플리케이션과 MySQL 데이터베이스로 구성된 멀티 컨테이너 애플리케이션입니다.

## 목차
1. [시작하기](#시작하기)
   - [필수 조건](#필수-조건)
   - [설치 방법](#설치-방법)
2. [구성 요소](#구성-요소)
3. [주요 기능](#주요-기능)
4. [디렉토리 구조](#디렉토리-구조)
5. [환경 변수](#환경-변수)
6. [Docker 관련 문서](#docker-관련-문서)
   - [Docker 설치 및 기본 사용법](./docs/1.%20Docker%20설치%20및%20기본%20사용법.md)
   - [간단한 애플리케이션 컨테이너화](./docs/2.%20간단한%20애플리케이션%20컨테이너화.md)
   - [Docker Compose로 여러 컨테이너 관리하기](./docs/3.%20Docker%20Compose로%20여러%20컨테이너%20관리하기.md)
   - [Docker Hub에 이미지 푸시하기](./docs/4.%20Docker%20Hub에%20이미지%20푸시하기.md)
   - [Docker 사설 레지스트리 설정 및 활용](./docs/5.%20Docker%20사설%20레지스트리%20설정%20및%20활용.md)

## 시작하기

### 필수 조건
- Docker (버전 20.10.0 이상)
- Docker Compose (버전 2.0.0 이상)
- Git
- Python 3.9 이상 (로컬 개발용)

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

4. 컨테이너 관리
```bash
# 컨테이너 중지
docker compose down

# 볼륨 삭제 (기존 데이터 초기화)
docker compose down -v

# 컨테이너 재시작
docker compose up -d
```

5. 로그 확인
```bash
# MySQL 컨테이너 로그 확인
docker compose logs db

# 웹 컨테이너 로그 확인
docker compose logs web
```

6. DB 접속
```bash
# MySQL 컨테이너에 접속
docker compose exec db mysql -u root -p
# 비밀번호 입력: password
```

## 구성 요소

### 웹 애플리케이션 (Flask)
- Python 3.9
- Flask 웹 프레임워크
- MySQL 커넥터
- RESTful API 지원
- 템플릿 엔진 (Jinja2)

### 데이터베이스 (MySQL)
- MySQL 8.0
- 초기 데이터 포함
- 자동 백업 설정
- 데이터 지속성 보장

## 주요 기능

- 메시지 목록 표시 및 관리
- RESTful API 엔드포인트 제공
- 데이터베이스 CRUD 작업
- 컨테이너 간 통신
- 로깅 및 모니터링
- 데이터 백업 및 복구

## 디렉토리 구조

```
multi-container-app/
├── web/                    # 웹 애플리케이션 디렉토리
│   ├── app.py             # Flask 애플리케이션 메인 파일
│   ├── Dockerfile         # 웹 애플리케이션 Dockerfile
│   ├── requirements.txt   # Python 패키지 의존성
│   └── templates/         # HTML 템플릿
│       └── index.html     # 메인 페이지 템플릿
├── db/                    # 데이터베이스 관련 파일
│   └── init.sql          # 초기 데이터베이스 설정
├── docker-compose.yml     # Docker Compose 설정 파일
└── docs/                  # 문서 디렉토리
    ├── 1. Docker 설치 및 기본 사용법.md
    ├── 2. 간단한 애플리케이션 컨테이너화.md
    ├── 3. Docker Compose로 여러 컨테이너 관리하기.md
    ├── 4. Docker Hub에 이미지 푸시하기.md
    └── 5. Docker 사설 레지스트리 설정 및 활용.md
```

## 환경 변수

### 웹 애플리케이션
- `DB_HOST`: 데이터베이스 호스트 (기본값: db)
- `DB_USER`: 데이터베이스 사용자 (기본값: root)
- `DB_PASSWORD`: 데이터베이스 비밀번호 (기본값: password)
- `DB_NAME`: 데이터베이스 이름 (기본값: app)
- `FLASK_ENV`: Flask 환경 (기본값: development)
- `FLASK_APP`: Flask 애플리케이션 파일 (기본값: app.py)

### 데이터베이스
- `MYSQL_ROOT_PASSWORD`: 루트 비밀번호 (필수)
- `MYSQL_DATABASE`: 데이터베이스 이름 (기본값: app)
- `MYSQL_USER`: 데이터베이스 사용자 (선택)
- `MYSQL_PASSWORD`: 데이터베이스 사용자 비밀번호 (선택)

## Docker 관련 문서

각 문서는 `docs` 디렉토리에서 확인할 수 있습니다:

1. [Docker 설치 및 기본 사용법](./docs/1.%20Docker%20설치%20및%20기본%20사용법.md)
   - Docker 설치 방법
   - 기본 명령어 사용법
   - 이미지 관리

2. [간단한 애플리케이션 컨테이너화](./docs/2.%20간단한%20애플리케이션%20컨테이너화.md)
   - Dockerfile 작성
   - 이미지 빌드
   - 컨테이너 실행

3. [Docker Compose로 여러 컨테이너 관리하기](./docs/3.%20Docker%20Compose로%20여러%20컨테이너%20관리하기.md)
   - docker-compose.yml 작성
   - 서비스 정의
   - 네트워크 설정

4. [Docker Hub에 이미지 푸시하기](./docs/4.%20Docker%20Hub에%20이미지%20푸시하기.md)
   - Docker Hub 계정 생성
   - 이미지 태그 지정
   - 이미지 푸시 및 풀

5. [Docker 사설 레지스트리 설정 및 활용](./docs/5.%20Docker%20사설%20레지스트리%20설정%20및%20활용.md)
   - 사설 레지스트리 설정
   - 이미지 관리
   - 보안 설정