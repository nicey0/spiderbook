#-Imports--------------------------------------------------#
import os, psycopg2, random, hashlib

#-Database-connector---------------------------------------#
def use_db(func):
    def user(data):
        arguments = {}
        arguments['conn'] = psycopg2.connect(
            "dbname=spiderbook user=postgres password=postgres"
        )
        arguments['c'] = arguments['conn'].cursor()
        arguments['data'] = data
        return func(arguments)
        arguments['conn'].close()
    return user

#-Functions------------------------------------------------#
@use_db
def new_pid(arguments):
    arguments['c'].execute("SELECT * FROM post_ids ORDER BY curr_num DESC LIMIT 1")
    latest_id = arguments['c'].fetchone()[0]

    new_id = latest_id + random.randint(1, 9)
    arguments['c'].execute(f"INSERT INTO post_ids VALUES ({new_id})")
    arguments['conn'].commit()

    return hashlib.sha1(bytes(new_id)).hexdigest()


@use_db
def API_create_post(arguments):
    pid = (new_pid({}),)
    arguments['c'].execute("INSERT INTO posts (pid, title, body, img) VALUES (%s, %s, %s, %s)",
    pid + tuple( arguments['data'].values() ))
    arguments['conn'].commit()
    return {"code": "success!"}


@use_db
def API_get_posts(arguments):
    limit = arguments['data']['limit']
    arguments['c'].execute("SELECT * FROM posts ORDER BY pid LIMIT %s", (limit,))
    response = arguments['c'].fetchall()
    print(response)
    return response
