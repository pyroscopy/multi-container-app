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
docker-compose up --build
```

3. 웹 브라우저에서 접속
```
http://localhost:5000
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

## 기여 방법

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요. 