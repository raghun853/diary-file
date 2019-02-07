import sys
import diaryFile.diaryMaster as diary


def getInput():
    if sys.argv[1:]:
        message = " ".join(sys.argv[1:])
    else:
        message = input("please enter your message to diary : ").strip()
    return message

def main():
    message = getInput()
    diaryobj = diary.diaryMaster("DailyDiary.txt")
    diaryobj.diaryWrite(message)


if __name__ == '__main__':
    main()
