import sqlite3
import math
conn = sqlite3.connect(":memory:")
c = conn.cursor()


def get_date_from_now(diff = 0):
    # we calculate the new date for a term. 
    # we intend to update it to the database right after the use of this method
    d = conn.cursor()

    # date_modifier = "+" + str(diff) + " days"

    if(diff>=0):
        date_modifier = "+" + str(diff) + " days"
    else:
        date_modifier = str(diff) + " days"

    # print(date_modifier) the modifer would be, for instance '+1 day'
    d.execute("SELECT DATE(?,?)",('now',date_modifier))
    text1 = d.fetchone()[0]
    return text1

def insert_term(textself,reading,levelTerm):
    nextDate = get_date_from_now(1)
    c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",(textself,reading,levelTerm,nextDate))

def get_date_diff(day_term,day_target):
    d = conn.cursor()
    print(day_term,day_target)
    d.execute("SELECT julianday(?) - julianday(?)",(day_term,day_target))
    day = math.floor(d.fetchone()[0])
    return day

def get_today_list():
    d = conn.cursor()
    # d.execute(""" SELECT * from Term where julianday('now') >= julianday(nextDate); """)
    
    d.execute(""" SELECT * from Term where Date('now') >= nextDate; """)
    return d.fetchall()


c.execute("""
    CREATE TABLE Term(
        termId INTEGER PRIMARY KEY,
        termSelf TEXT,
        reading TEXT,
        levelTerm INTEGER,
        nextDate TEXT
    )
    CREATE TABLE Definition(
    termId INTEGER,
    definition TEXT
    )
    CREATE TABLE SampleSentence(
    termId INTEGER,
    sentence TEXT,
    translation TEXT
    )
""")

insert_term('向こう','むこう',1)
c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(-1)))
c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(0)))
c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(2)))
# insert_term('晴れ','はれ',1)

c.execute("""SELECT * from Term""")
print(c.fetchall())

# test date difference calculations
# day_diff = get_date_diff(get_date_from_now(1),get_date_from_now(5))
# print(day_diff)

# c.execute("""
#     SELECT DATE('now');
#     """)
# print(c.fetchall())

# now we test get today term
list_demo = get_today_list()
print(list_demo)

conn.commit()
conn.close()