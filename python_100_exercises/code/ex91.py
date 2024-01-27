import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()


with open("ten_more_countries.txt") as file:
    data = file.readlines()

data = [x.strip() for x in data]
for row in data:
    id, country, area = row.split(",")
    if id == "ID":
        continue
    else:
        query = f"INSERT INTO countries (country,area) VALUES ({country},{area})"
        print(query)
        cur.execute(query)
        #cur.execute("INSERT INTO countries (country,area) VALUES (?,?)", (country,area))
conn.commit()
conn.close()
