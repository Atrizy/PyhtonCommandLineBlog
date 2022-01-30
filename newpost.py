import dbcreds
import mariadb as db

def add_new_post(post_content, username):
    conn = db.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO blog_post(content, username) VALUES('{post_content}', '{username}')")
    conn.commit()

    cursor.close()
    conn.close()
