import psycopg2, random, hashlib

# Database Connector
def use_db(func):
    def user(*args):
        conn = psycopg2.connect("dbname=spiderbook user=postgres password=postgres")
        c = conn.cursor()
        return func(conn, c, args)
        conn.close()
    return user

# Database Functions
@use_db
def new_pid(conn, c):
    c.execute("SELECT * FROM post_ids ORDER BY curr_num DESC LIMIT 1")
    latest_id = c.fetchone()[0]

    new_id = latest_id + random.randint(1, 9)
    c.execute(f"INSERT INTO post_ids VALUES ({new_id})")
    conn.commit()

    return hashlib.sha1(bytes(new_id)).hexdigest()

@use_db
def create_post(conn, c, data):
    c.execute("INSERT INTO posts (pid, title, body, img) VALUES (%s, %s, %s)", tuple(
        data.values()))

@use_db
def get_posts(conn, c, limit):
    c.execute("SELECT * FROM posts ORDER BY pid LIMIT %s", (limit,))
    response = c.fetchall()
    return response