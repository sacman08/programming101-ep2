#Diary Application
#TODO Entery daily information and save it to a file through the command line.
from datetime import datetime

def get_daily_input():
    daily_diary = input("Write you daily thoughts:\n")
    return daily_diary

def write_daily(diary):
    filename = f'{datetime.now().strftime("%c")}.diary'
    with open(filename, 'w') as f:
        f.write(diary)

def main():
    diary = get_daily_input()
    write_daily(diary)
    print("Diary logged for today.")

if __name__ == "__main__":
    main()