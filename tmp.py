import _sqlite3

con = _sqlite3.connect('my_db.sqlite')
cur = con.cursor()

result = cur.execute("""SELECT * FROM phrases""").fetchall()
print(len(result))