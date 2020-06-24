#Diary Application
#TODO Create escape keystroke to allow multiple lines with enter key. Currently only allows typing until you hit enter 

#! /usr/bin/python
from datetime import datetime

def get_daily_input():
    daily_diary = input("Write you daily thoughts:\n")
    return daily_diary

def write_daily(diary):
    filename = f'Day_{datetime.now().strftime("%j")}.diary'
    with open(filename, 'w') as f:
        f.write(diary)

def main():
    diary = get_daily_input()
    write_daily(diary)
    print("Diary logged for today.")

if __name__ == "__main__":
    main()