import time

print('Print immediatly.')
time.sleep(2.3)
print('Printe after 2.4 second')

while True:
    localtime = time.localtime()
    result = time.strftime('%I:%M:%S %p', localtime)
    print(result)
    time.sleep(5)
