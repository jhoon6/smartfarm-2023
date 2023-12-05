import sqlite3
import random
import datetime as dt

def randf():
    return random.random()

conn = sqlite3.connect("sensor.db")

print("연결완")


conn.execute('''CREATE TABLE IF NOT EXISTS "Measure1" (
    "ID"	INTEGER NOT NULL,
    "HUMID"	REAL NOT NULL,
    "TEMP"	REAL NOT NULL,
    "DISTANCE"	REAL NOT NULL,
    "TIMESTAMP" DATETIME NOT NULL,
    PRIMARY KEY("ID" AUTOINCREMENT)
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS "Measure2" (
    "ID"	INTEGER NOT NULL,
    "HUMID"	REAL NOT NULL,
    "TEMP"	REAL NOT NULL,
    "DISTANCE"	REAL NOT NULL,
    "TIMESTAMP" DATETIME NOT NULL,
    PRIMARY KEY("ID" AUTOINCREMENT)
);''')

# conn.execute("DELETE from Measure1;") #테이블전체삭제
# conn.commit()



for i in range(5):
    now = dt.datetime.now() + dt.timedelta(minutes=i)
    conn.execute(f'''INSERT INTO "Measure1" VALUES (NULL,?,?,?,?)''', (randf()*100, 20+randf()*10, 20+randf()*30, now) )
    #conn.execute(f'''INSERT INTO "Measure2" VALUES (NULL,?,?,?,?)''', (randf()*100, 20+randf()*10, 20+randf()*50, now) )
    
conn.commit()

#print("작성완료")

# measure1_data = conn.execute("SELECT * FROM Measure1").fetchall()
# for rows in measure1_data:
#     print(rows)

# measure2_data = conn.execute("SELECT * FROM Measure2").fetchall()
# for rows in measure2_data:
#     print(rows)

# print(measure1_data)

print("5개 랜덤 레코드 생성 완료")
conn.close()
