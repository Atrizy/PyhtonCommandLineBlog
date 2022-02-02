import mariadb as db
import dbcreds

def grab_posts():
    content = None

    conn = db.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()

    cursor.execute(
        f"select username, content from blog_post")
    posts = content = cursor.fetchall()

    cursor.close()
    conn.close()

    print(content)
    for post in posts:
        print("")
        print(f"{post[0]}: {post[1]}")
        print("")