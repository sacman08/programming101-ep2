#Logging Application
#Part of PyATL's online series of programming applications.

#! /usr/bin/python
from datetime import date, datetime

def get_daily_input():
    daily_diary = []
    print('Write your log. Press enter twice to escape.')
    while True:
        daily_d = input()
        if daily_d:
            daily_diary.append('\n')
            daily_diary.append(daily_d)
        else:
            break
    return daily_d.join(daily_diary)

def write_daily(diary):
    filename = f'Log_{date.today()}_{datetime.now().strftime("%H%M%S")}.log'
    with open(filename, 'w') as f:
        f.write(diary)

def main():
    diary = get_daily_input()
    write_daily(diary)
    print("File logged for today.")

if __name__ == "__main__":
    main()
