/*Posts****************************/
CREATE TABLE posts (
    pid TEXT NOT NULL,
    title VARCHAR(200) NOT NULL,
    body VARCHAR(2000),
    img_url VARCHAR(500),
    author VARCHAR(30) NOT NULL,
    curtime DATE NOT NULL
);
CREATE TABLE post_ids (
    curr_num BIGINT NOT NULL
);
INSERT INTO post_ids VALUES (1);

/*Users****************************/
CREATE TABLE users (
    user_id TEXT NOT NULL,
    username VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL,
    pass VARCHAR(60) NOT NULL,
    bio VARCHAR(500),
    pfp_url VARCHAR(500),
    join_date DATE NOT NULL
);