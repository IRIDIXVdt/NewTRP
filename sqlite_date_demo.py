import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()


def get_date_from_now(diff = 0):
    # we calculate the new date for a term. 
    # we intend to update it to the database right after the use of this method
    d = conn.cursor()
    date_modifier = "+" + str(diff) + " days"
    # print(date_modifier) the modifer would be, for instance '+1 day'
    d.execute("SELECT DATE(?,?)",('now',date_modifier))
    text1 = d.fetchone()[0]
    return text1

def insert_term(textself,reading,levelTerm,levelReading):
    nextDate = get_date_from_now(1)
    print(nextDate)
    c.execute("INSERT INTO Term(termSelf,reading,levelTerm,levelReading,nextDate) VALUES (?,?,?,?,?)",(textself,reading,levelTerm,levelReading,nextDate))

c.execute("""
    CREATE TABLE Term(
        termId INTEGER PRIMARY KEY,
        termSelf TEXT,
        reading TEXT,
        levelTerm INTEGER,
        levelReading INTEGER,
        nextDate TEXT
    )""")

insert_term('向こう','むこう',1,1)
insert_term('晴れ','はれ',1,1)

c.execute("""
    SELECT * from term
    """)
print(c.fetchall())

# c.execute("""
#     SELECT DATE('now');
#     """)
# print(c.fetchall())

conn.commit()
conn.close()