import os
import sqlite3
import math

# initializations
conn = sqlite3.connect("term01.db")
c = conn.cursor()
clear = lambda: os.system('cls') #on Windows System
print('for help, type in h')




def print_list_programmer():
    print('test code*')
    d = conn.cursor()
    d.execute(""" SELECT * from Term """)
    print(d.fetchall()) 
    d.execute(""" SELECT * from Definition """)
    print(d.fetchall()) 
    d.execute(""" SELECT * from SampleSentence """)
    print(d.fetchall()) 
def help_message():
    clear()
    print("""
            ====================================
            * to insert, type "insert"
            * to start with todays' list, type "start"
            * to add sample sentences, type "sample"
            * to add definitions, type "defi"
            * to clear the console, type "clear"
            * to exit, type "exit"
            ====================================
    """)

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
    conn.commit()
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
def level_to_day(level):
    if level == 1:
        return 1
    elif level == 2:
        return 2
    elif level == 3:
        return 3
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
# the following methods are for prompting user inputs

def start_test_user():
    exit
def insert_term_user():
    d = conn.cursor()
    while 1:
        term = input("The term is: ")
        if term == "exit":
            break
        reading = input("The reading of the term is: ")
        if reading == "exit":
            break
        insert_term(term,reading,1)
        conn.commit()
        print("""
        Thank you! 
        To insert another term, hit enter. 
        To go back to the menu, enter "exit"
        If you would like to add one* definition for this term right now, you can type it below
        """)
        z = input(">>> ")
        if z == "exit":
            help_message()
            break
        elif z != None:
            insert_def(term, z)
            conn.commit()
def add_sample_user():
    d = conn.cursor()
    while 1:
        term = input("The term is: ")
        if term == "exit":
            break
        sentence = input("The sentence is: ")
        if sentence == "exit":
            break
        translation = input("The translation and/or explanation is: ")
        if translation == "exit":
            break
        insert_sen(term,sentence,translation)
        
        print("""
        Thank you! 
        To insert another sentence, hit enter. 
        To go back to the menu, enter "exit"
        """)
        z = input(">>> ")
        if z == "exit":
            help_message()
            break
def add_definition_user():
    d = conn.cursor()
    while 1:
        term = input("The term is: ")
        if term == "exit":
            break
        definition = input("The definition of the term is: ")
        if definition == "exit":
            break
        insert_def(term,definition)
        conn.commit()
        print("""
        Thank you! 
        To insert another definition, hit enter. 
        To go back to the menu, enter "exit"
        """)
        z = input(">>> ")
        if z == "exit":
            help_message()
            break
def print_list_programmer():
    print('test code*')
    d = conn.cursor()
    d.execute(""" SELECT * from Term """)
    print(d.fetchall()) 
    d.execute(""" SELECT * from Definition """)
    print(d.fetchall()) 
    d.execute(""" SELECT * from SampleSentence """)
    print(d.fetchall()) 
def print_test_term_user(spelling):
    clear()
    d = conn.cursor()
    print("===================================\n")
    print(spelling)
    
    print("----------------------------------")
    d.execute(""" SELECT definition from Definition where termself = ? """,(spelling,))
    dlist = d.fetchall()
    for x in range(len(dlist)):
        for y in range(len(dlist[x])):
            print (str(x)+") "+dlist[x][y],sep = ', ')
    d.execute(""" SELECT sentence,translation from SampleSentence where termself = ? """,(spelling,))
    dlist = d.fetchall()
    for x in range(len(dlist)):
        print("----------------------------------")
        for y in range(len(dlist[x])):
            print (dlist[x][y])
    print("\n===================================")
    # return list_def,list_sen
    # not completed

def display_programmer():
    spelling = input("term is: ")
    print_test_term_user(spelling)



def main():
    help_message()
    while 1:
        x = input(">>> ")
        if x == 'exit':
            break
        elif x == 'h':
            help_message()
        elif x == 'insert':
            insert_term_user()
        elif x == 'start':
            start_test_user()
        elif x == 'sample':
            add_sample_user()
        elif x == 'defi':
            add_definition_user()
        elif x == 'clear':
            clear()
        elif x == 'print list':
            print_list_programmer()
        elif x == 'print todays list':
            print(get_today_list())
        elif x == 'display term':
            display_programmer()
    conn.close()

if __name__ == '__main__':
    main()
    
    