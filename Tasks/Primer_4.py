#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread, Lock
from time import sleep

lock = Lock()
stop_thread = False


def infinit_worker():
    print("Start infinit_worker()")
    while True:
        print("--> thread work")
        lock.acquire()

        if stop_thread is True:
            break

        lock.release()
        sleep(0.1)

    print("Stop infinit_worker()")


if __name__ == '__main__':
    # Create and start thread
    th = Thread(target=infinit_worker)
    th.start()
    sleep(2)
    # Stop thread
    lock.acquire()
    stop_thread = True
    lock.release()
