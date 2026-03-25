import time
import random 

def stream_logs(): # Generator

    logs=[70,20,30,40,10,-10,-20]
    while True:
        yield random.choice(logs)
        time.sleep(1)

def filter_errors(log_stream):     
    for log in log_stream:
        if log < 0:
            yield log

def alert(error_logs):
    for error in error_logs:
        print(f"Alert:{error}")

logs = stream_logs()
error = filter_errors(logs)   
alert(error)     


