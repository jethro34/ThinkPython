import time


def timer():
    input_time = time.time()
    days = int(input_time // 86400)
    hours = str(int(input_time % 86400 // 3600)).zfill(2)
    minutes = str(int(input_time % 3600 // 60)).zfill(2)
    seconds = str(int(input_time % 60)).zfill(2)
    print("The GMT time is: " + hours + ":" + minutes + ":" + seconds)
    print("Days elapsed since 'the epoch':", days)


timer()
