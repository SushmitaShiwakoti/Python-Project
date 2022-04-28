import time

start_time = time.time()
last_time = start_time
lap_num = 1


print("Press ENTER to coount laps. \nPress CTRL + C to stop")

try:
     while True:
            input()

            lap_time = round((time.time() - last_time), 2)

            total_time = round((time.time() - start_time), 2)

            print("Lap No. " + str(lap_num))
            print("Total Time: " + str(total_time))
            print("Lap Time: " + str(lap_time))

            print("*"*20)

            last_time = time.time()
            lap_num+=1
except KeyboardInterrupt:
    print("Done")