# import threading
#
#
# def gfg():
#     print("GeeksforGeeks\n")
#
#
# timer = threading.Timer(5.0,gfg)
# timer.start()
# timer.run()
# while True:
#     if timer.run()==False:
#         print("I love me")

#
import time
import sys

time_start = time.time()
seconds = 0
minutes = 0

while True:
    try:
        # sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
        # sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start)
        print(seconds)
        if seconds == 1*10:
            print("hellow")
    except KeyboardInterrupt as e:
        break



#      # Timer
# import time
# print("This is the timer")
# # Ask to Begin
# start = input("Would you like to begin Timing? (y/n): ")
# if start == "y":
#     timeLoop = True
#
# # Variables to keep track and display
# Sec = 0
# Min = 0
# # Begin Process
# timeLoop = start
# while timeLoop:
#     Sec += 1
#     print(str(Min) + " Mins " + str(Sec) + " Sec ")
#     time.sleep(1)
#     if Sec == 60:
#         Sec = 0
#         Min += 1
#         print(str(Min) + " Minute")
# # Program will cancel when user presses X button