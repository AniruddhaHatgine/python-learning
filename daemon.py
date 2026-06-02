import threading # use threading to run blocking code in thread
import time 
def task(): # use a function to simulate a blocking task
    while True: # run an infinite loop to simulate a blocking task
        print("Running")
    time.sleep(1) # sleep for 1 second to simulate blocking

t = threading.Thread(target=task) # create a thread to run the blocking task
t.daemon = True # set the thread as a daemon thread so it will exit when the main thread exits
t.start() # start the thread to run the blocking task    

time.sleep(3)

print("main thread exiting")