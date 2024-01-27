import sqlite3

con = sqlite3.connect("database.db")

cur = con.cursor()

res = cur.execute("select country from countries where area > 2000000")
clist = res.fetchall()
con.close()
clist = [x[0] for x in clist]
for country in clist:
    print(country)
