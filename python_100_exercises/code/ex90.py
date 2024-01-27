import sqlite3
import pandas

con = sqlite3.connect("database.db")

cur = con.cursor()

res = cur.execute("select * from countries where area > 2000000 order\
                   by area asc")
clist = res.fetchall()
con.close()
print(clist)

df = pandas.DataFrame(clist)
df.columns = ["Rank", "Country", "Area", "Population"]

df.to_csv("output.csv", index=False)
