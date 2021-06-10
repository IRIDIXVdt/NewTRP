import sqlite3
import math
conn = sqlite3.connect("term01.db")
c = conn.cursor()
def level_to_day(level):
    if level == 1:
        return 1
    elif level == 2:
        return 1
    elif level == 3:
        return 2
    elif level == 4:
        return 4
    elif level == 5:
        return 6
    elif level == 6:
        return 8
    elif level == 7:
        return 10
    elif level == 8:
        return 13
    elif level == 9:
        return 17
    else:
        return 25
def print_list_programmer():
    print('test code*')
    d = conn.cursor()
    d.execute(""" SELECT * from Term """)
    print(d.fetchall()) 
    d.execute(""" SELECT * from Definition """)
    print(d.fetchall()) 
    d.execute(""" SELECT * from SampleSentence """)
    print(d.fetchall()) 

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
    nextDate = get_date_from_now(0)
    c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",(textself,reading,levelTerm,nextDate))

def insert_def(term_sample, def_sample):
    c.execute("INSERT INTO Definition VALUES (?,?)",(term_sample,def_sample))
    conn.commit()

def insert_sen(term, sen, tran):
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

def update_term(cid,new_level):
    new_day = level_to_day(new_level)
    new_date = get_date_from_now(new_day)
    d = conn.cursor()
    d.execute(""" UPDATE Term SET nextDate = ?, levelTerm = ? WHERE termId = ?""", (new_date,new_level,cid))

# this initializes the database's tables
c.execute("""
    CREATE TABLE Term(
        termId INTEGER PRIMARY KEY,
        termSelf TEXT,
        reading TEXT,
        levelTerm INTEGER,
        nextDate TEXT
    )
""")
c.execute("""
    CREATE TABLE Definition(
        termSelf TEXT,
        definition TEXT
    )""")
c.execute("""
    CREATE TABLE SampleSentence(
        termSelf TEXT,
        sentence TEXT,
        translation TEXT
    )""")

insert_term('向こう','むこう',1)
insert_term('廊下','ろうか',1)
# c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(-1)))
# c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(0)))
# c.execute("INSERT INTO Term(termSelf,reading,levelTerm,nextDate) VALUES (?,?,?,?)",('廊下','ろうか',1,get_date_from_now(2)))

# insert_def('廊下','走廊')
# insert_def('廊下','corridor')

# insert_sen('廊下','随便写test随便写sentence','随便写test')
# insert_sen('廊下','sentence','随便写random sentence')
# insert_sen('廊下','ランドン','随便写ランドン')

# def print_term_condition():
#     d= conn.cursor()
#     print("-----------------")
#     d.execute(""" SELECT definition from Definition where termself = ? """,('廊下',))
#     dlist = d.fetchall()
#     for x in range(len(dlist)):
#         for y in range(len(dlist[x])):
#             print (str(x)+") "+dlist[x][y],sep = ', ')
#     d.execute(""" SELECT sentence,translation from SampleSentence where termself = ? """,('廊下',))
#     dlist = d.fetchall()
#     for x in range(len(dlist)):
#         print("-----------------")
#         for y in range(len(dlist[x])):
#             print (dlist[x][y])

# # now we test get today term

# update_term(2,5)
# list_demo = get_today_list()
# print(list_demo)
# print('----------------')
# print_list_programmer()

conn.commit()
conn.close()