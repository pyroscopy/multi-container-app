ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO messages (message) VALUES
    ('안녕하세요!'),
    ('멀티 컨테이너 앱입니다.'),
    ('Docker Compose로 실행됩니다.');