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

def insert_def(term,def):
    c.execute("INSERT INTO Definition VALUES (?,?,?)",(term,def))
    conn.commit()

def insert_sen(term,sen,tran):
    c.execute("INSERT INTO SampleSentence VALUES (?,?,?)",(term,sen,tran))
    conn.commit()

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

insert_term('向こう','むこう',1)
c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(-1)))
c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(0)))
c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(2)))

insert_def('廊下','走廊')
insert_def('廊下','corridor')

insert_sen('廊下','随便写test随便写sentence','随便写test')
insert_sen('廊下','sentence','随便写random sentence')
insert_sen('廊下','ランドン','随便写ランドン')

conn.commit()
conn.close()