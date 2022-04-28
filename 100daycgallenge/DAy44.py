from pickle import TRUE
from types import coroutine
from typing import Counter


def myfunc():
    import time

    book= "Today I learned aboutwhat coroutine is in python."
    time.sleep(3)
    print("Code with Susmita")
    while TRUE:
        value=(yield)
        if value in book:
            print("Your text is in book")
        else:
            print("Your text is not in book")
        
coroutine= myfunc()
next(coroutine)
coroutine.send("python")
coroutine.send("With Susmita")
coroutine.close()