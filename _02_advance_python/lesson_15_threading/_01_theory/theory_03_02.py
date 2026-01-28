"""race condition (гонка данных) пример 2"""
import threading

counter = 0


def increment(lock):
    global counter

    for i in range(100000):
        with lock:
            counter += 1


if __name__ == '__main__':
    threads = []
    lock_obj = threading.Lock()
    for _ in range(5):
        threads.append(threading.Thread(target=increment, args=(lock_obj,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Counter value: {counter}')

