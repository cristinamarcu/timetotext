import num2word
import datetime


def validate_input(mytime: str) -> bool:
    try:
        mylist = mytime.split(':')
        hour = int(mylist[0])
        minute = int(mylist[1])
        if hour < 0 or hour > 24:
            raise Exception()
        if minute < 0 or minute > 59:
            raise Exception()
    except:
        return False
    return True


def convert_time_to_text(mytime: str) -> str:
    if not validate_input(mytime):
        return 'Time is not in a valid format'
    mylist = mytime.split(':')
    hour = int(mylist[0])
    minute = int(mylist[1])
    if hour == 0:
        hour = 12
    elif 12 < hour <= 24:
        hour = hour - 12
    if minute == 0:
        time = num2word.word(hour) + " o'clock"
    elif minute == 30:
        time = 'Half past ' + num2word.word(hour)
    elif minute < 30:
        if minute == 15:
            time = 'Quarter past ' + num2word.word(hour)
        else:
            time = num2word.word(minute) + ' past ' + num2word.word(hour)
    else:
        if hour == 12:
            hour = 0
        if minute == 45:
            time = 'Quarter to ' + num2word.word(hour + 1)
        else:
            time = num2word.word(60 - minute) + ' to ' + num2word.word(hour + 1)
    return time[0].upper() + time[1:].lower()


def get_current_time() -> str:
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    return str(hour) + ':' + str(minute)
