drop database brandi;

create database brandi character set utf8mb4 collate utf8mb4_general_ci;
use brandi;

SET GLOBAL time_zone='+09:00';
SET time_zone='+09:00';  

CREATE TABLE seller_properties
(
    `id`    INT            NOT NULL    AUTO_INCREMENT COMMENT '아이디', 
    `name`  VARCHAR(45)    NOT NULL    COMMENT '이름', 
    PRIMARY KEY (id)
);

ALTER TABLE seller_properties COMMENT '쇼핑몰 마켓  로드샵  디자이너브랜드  제너럴브랜드  내셔널브랜드  뷰티';

INSERT INTO seller_properties 
VALUES (
    1,
    '쇼핑몰 · 마켓'
),
(
    2,
    '로드샵'
),
(
    3,
    '디자이너 브랜드'
),
(
    4,
    '제너럴브랜드'
),
(
    5,
    '내셔널 브랜드'
),
(
    6,
    '뷰티'
);

CREATE TABLE seller_statuses
(
    `id`    INT            NOT NULL    AUTO_INCREMENT COMMENT '아이디', 
    `name`  VARCHAR(64)    NOT NULL    COMMENT '이름', 
    PRIMARY KEY (id)
);

ALTER TABLE seller_statuses COMMENT '입점대기, 입점거절, 입점, 휴점, 퇴점 대기, 퇴점';

INSERT INTO seller_statuses
VALUES (
    1,
    '입점대기'
),
(
    2,
    '입점거절'
),
(
    3,
    '입점'
),
(
    4,
    '휴점'
),
(
    5,
    '퇴점 대기'
),
(
    6,
    '퇴점'
);

CREATE TABLE banks
(
    `id`    INT            NOT NULL    AUTO_INCREMENT, 
    `name`  VARCHAR(64)    NOT NULL, 
    PRIMARY KEY (id)
);

ALTER TABLE banks COMMENT '은행 이름 테이블';

INSERT INTO banks
VALUES (
    1,
    '한국은행'
),
(
    2,
    '산업은행'
),
(
    3,
    '기업은행'
),
(
    4,
    '국민은행'
),
(
    5,
    '수협중앙회'
),
(
    6,
    '수출입은행'
),
(
    7,
    '농협중앙회'
),
(
    8,
    '지역 농축협'
),
(
    9,
    '우리은행'
),
(
    10,
    'SC은행'
),
(
    11,
    '한국씨티은행'
),
(
    12,
    '대구은행'
),
(
    13,
    '부산은행'
),
(
    14,
    '광주은행'
),
(
    15,
    '제주은행'
),
(
    16,
    '전북은행'
),
(
    17,
    '경남은행'
),
(
    18,
    '새마을금고중앙회'
),
(
    19,
    '신협중앙회'
),
(
    20,
    '상호저축은행'
);

CREATE TABLE sellers
(
    `id`                           INT              NOT NULL    AUTO_INCREMENT COMMENT '셀러번호', 
    `register_date`                DATETIME         NOT NULL    COMMENT '등록일시', 
    `seller_status_id`             INT              NOT NULL    COMMENT '셀러 상태 아이디', 
    `is_master`                    TINYINT          NOT NULL    DEFAULT 0 COMMENT '마스터', 
    `is_deleted`                   TINYINT          NOT NULL    DEFAULT 0 COMMENT '삭제 여부', 
    `seller_id`                    INT              NOT NULL    COMMENT '셀러 아이디', 
    `seller_account_id`            VARCHAR(128)     NOT NULL    COMMENT '셀러 계정', 
    `english_name`                 VARCHAR(128)     NOT NULL    COMMENT '영문이름', 
    `korean_name`                  VARCHAR(128)     NOT NULL    COMMENT '한글 이름', 
    `cs_phone`                     VARCHAR(64)      NOT NULL    COMMENT '고객센터 전화번호', 
    `seller_property_id`           INT              NOT NULL    COMMENT '셀러 속성 아이디', 
    `profile_image`                VARCHAR(2048)    NULL        COMMENT '프로필이미지URL', 
    `password`                     BIT              NULL        COMMENT '패스워드', 
    `background_image`             VARCHAR(2048)    NOT NULL    COMMENT '셀러페이지배경이미지URL', 
    `simple_description`           TEXT             NOT NULL    COMMENT '한줄소개', 
    `detail_description`           TEXT             NOT NULL    COMMENT '상세소개', 
    `zip_code`                     VARCHAR(32)      NOT NULL    COMMENT '우편번호', 
    `address`                      VARCHAR(256)     NOT NULL    COMMENT '주소', 
    `detail_address`               VARCHAR(512)     NOT NULL    COMMENT '상세주소', 
    `open_time`                    TIME             NOT NULL    COMMENT '운영시작시간', 
    `close_time`                   TIME             NOT NULL    COMMENT '운영마감시간', 
    `bank_id`                      INT              NOT NULL    COMMENT '은행 아이디', 
    `account_number`               VARCHAR(128)     NOT NULL    COMMENT '계좌번호', 
    `account_name`                 VARCHAR(128)     NOT NULL    COMMENT '계좌주인이름', 
    `shipping_information`         TEXT             NOT NULL    COMMENT '배송정보', 
    `exchange_refund_information`  TEXT             NOT NULL    COMMENT '교환/환불정보', 
    `model_height`                 VARCHAR(32)      NULL        COMMENT '모델키', 
    `model_top_size`               VARCHAR(32)      NULL        COMMENT '모델상의사이즈', 
    `model_bottom_size`            VARCHAR(32)      NULL        COMMENT '모델하의사이즈', 
    `model_feet_size`              VARCHAR(32)      NULL        COMMENT '모델신발사이즈', 
    `shopping_feedtext`            TEXT             NULL        COMMENT '쇼핑피드텍스트', 
    `registered_product_count`     INT              NOT NULL    COMMENT '등록상품개수', 
    `created_at`                   TIMESTAMP        NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력시작일자',
    `expired_at`                   DATETIME         NOT NULL    DEFAULT '9999-12-31 00:00:00' COMMENT 'default=9999-12-31', 
    `modifier_id`                  INT              NOT NULL    COMMENT '수정자아이디', 
    PRIMARY KEY (id)
);

ALTER TABLE sellers COMMENT '셀러 유저 테이블';

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_seller_status_id_seller_statuses_id FOREIGN KEY (seller_status_id)
        REFERENCES seller_statuses (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_seller_property_id_seller_properties_id FOREIGN KEY (seller_property_id)
        REFERENCES seller_properties (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_bank_id_banks_id FOREIGN KEY (bank_id)
        REFERENCES banks (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE sellers
    ADD CONSTRAINT FK_sellers_modifier_id_sellers_id FOREIGN KEY (modifier_id)
        REFERENCES sellers (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE seller_manager_tables
(
    `id`            INT             NOT NULL    AUTO_INCREMENT, 
    `name`          VARCHAR(64)     NOT NULL    COMMENT '이름', 
    `phone_number`  VARCHAR(64)     NOT NULL    COMMENT '전화번호', 
    `email`         VARCHAR(128)    NOT NULL    COMMENT '이메일', 
    `seller_id`     INT             NOT NULL    COMMENT '셀러아이디', 
    PRIMARY KEY (id)
);

ALTER TABLE seller_manager_tables COMMENT '셀러 담당자 테이블';

ALTER TABLE seller_manager_tables
    ADD CONSTRAINT FK_seller_manager_tables_seller_id_sellers_id FOREIGN KEY (seller_id)
        REFERENCES sellers (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO seller_manager_tables
VALUES (
    1,
    '이충희',
    '010-1111-2222',
    'star1@naver.com',
    1
),
(
    2,
    '김태수',
    '010-2222-2222',
    'star2@naver.com',
    2
),
(
    3,
    '김기욱',
    '010-1111-2112',
    'star3@naver.com',
    3
),
(
    4,
    '김태하',
    '010-1111-2122',
    'star4@naver.com',
    4
),
(
    5,
    '이지연',
    '010-1111-1111',
    'star5@naver.com',
    5
),
(
    6,
    '이지원',
    '010-1111-1112',
    'star6@naver.com',
    6
),
(
    7,
    '이지연',
    '010-1111-1113',
    'star7@naver.com',
    7
),
(
    8,
    '이지황',
    '010-1111-1114',
    'star8@naver.com',
    8
),
(
    9,
    '이지웅',
    '010-1111-1115',
    'star9@naver.com',
    9
),
(
    10,
    '이지형',
    '010-1111-1116',
    'star10@naver.com',
    10
),
(
    11,
    '이지훈',
    '010-1111-1117',
    'star11@naver.com',
    11
),
(
    12,
    '이치훤',
    '010-1111-1118',
    'star12@naver.com',
    12
),
(
    13,
    '이치훤',
    '010-1111-1119',
    'star13@naver.com',
    13
),
(
    14,
    '이치연',
    '010-1111-1120',
    'star14@naver.com',
    14
),
(
    15,
    '이치훙',
    '010-1111-1121',
    'star15@naver.com',
    15
),
(
    16,
    '이자돈',
    '010-1111-1122',
    'star16@naver.com',
    16
),
(
    17,
    '이환',
    '010-1111-1123',
    'star17@naver.com',
    17
),
(
    18,
    '이형일',
    '010-1111-1124',
    'star18@naver.com',
    18
),
(
    19,
    '이군',
    '010-1111-1125',
    'star19@naver.com',
    19
),
(
    20,
    '이양',
    '010-1111-1126',
    'star20@naver.com',
    20
);

CREATE TABLE seller_status_modification_histories
(
    `id`                INT         NOT NULL    AUTO_INCREMENT, 
    `seller_id`         INT         NOT NULL    COMMENT '셀러 아이디', 
    `updated_at`        DATETIME    NOT NULL    COMMENT '셀러 상태에 따라 사용하기', 
    `seller_status_id`  INT         NOT NULL    COMMENT '셀러 상태 아이디', 
    `modifier_id`       INT         NOT NULL    COMMENT '수정자 아이디', 
    PRIMARY KEY (id)
);

ALTER TABLE seller_status_modification_histories  COMMENT '셀러상태 변경이력';

ALTER TABLE seller_status_modification_histories
    ADD CONSTRAINT seller_status_modification_histories_seller_status_id FOREIGN KEY (seller_status_id)
        REFERENCES seller_statuses (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE seller_status_modification_histories
    ADD CONSTRAINT seller_status_modification_histories_seller_id FOREIGN KEY (seller_id)
        REFERENCES sellers (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE seller_status_modification_histories
    ADD CONSTRAINT seller_status_modification_histories_modifier_id FOREIGN KEY (modifier_id)
        REFERENCES sellers (id) ON DELETE RESTRICT ON UPDATE RESTRICT;