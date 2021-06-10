import os
clear = lambda: os.system('cls') #on Windows System
clear()
print('for help, type in h')

def insert_term():
    while 1:
        term = input("The term is: ")
        reading = input("The reading of the term is: ")

def main():
    while 1:
        x = input(">>> ")
        if x == 'exit':
            break
        elif x == 'h':
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
        elif x == 'insert':
            exit
        elif x == 'start':
            exit
        elif x == 'sample':
            exit
        elif x == 'defi':
            exit
        elif x == 'clear':
            clear()
        elif x == 'print list':
            print('test code*')

if __name__ == '__main__':
    main()
    
    