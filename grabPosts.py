import mariadb as db
import dbcreds

def grab_posts():
    conn = db.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()

    cursor.execute(
        f"select count(*) as wins from fight_result fr where fr.win = 1")
    win_count = cursor.fetchone()

    cursor.execute(
        f"select count(*) as wins from fight_result fr where fr.win = 0")
    loss_count = cursor.fetchone()

    cursor.close()
    conn.close()

    print(f"Your record: {win_count[0]} wins --- {loss_count[0]} losses")