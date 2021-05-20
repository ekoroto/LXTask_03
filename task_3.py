from threading import Thread, RLock

a = 0
lock_a = RLock()


def function(arg):
    global a
    for _ in range(arg):
        with lock_a:
            a += 1


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)


main()