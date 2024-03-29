#-Imports--------------------------------------------------#
import os, psycopg2, random, hashlib, time, datetime

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
    try:
        pid = (new_pid({}),)
        post_data = (
            arguments['data']['title'],
            arguments['data']['body'],
            arguments['data']['img_url'],
            arguments['data']['author']
        )
        date = (datetime.datetime.now(),)

        arguments['c'].execute (
        "INSERT INTO posts (pid, title, body, img_url, author, curtime) VALUES (%s,%s,%s,%s,%s,%s)",
            pid + post_data + date)

        arguments['conn'].commit()
        return {"code": "success!"}

    except Exception as e:
        return {"code": str(e)}

@use_db
def API_get_posts(arguments):
    limit = arguments['data']['limit']
    arguments['c'].execute("SELECT * FROM posts LIMIT %s", (limit,))
    response = arguments['c'].fetchall()
    print(response)
    return response
