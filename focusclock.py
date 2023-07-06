import time

def countdown(minutes):
    seconds = minutes
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

# 设置专注时间为1440分钟
focus_time = 1440

countdown(focus_time)
