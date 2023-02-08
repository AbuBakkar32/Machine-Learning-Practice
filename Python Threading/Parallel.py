import concurrent.futures
import time


# START - Parallel programming
def do_something(sec):
    print(f'Sleeping {sec} second(s)...')
    time.sleep(sec)
    return f'Done Sleeping...{sec}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


# END - Parallel programming

# START - Sequential programming
def do_something(sec):
    print(f'Sleeping {sec} second(s)...')
    time.sleep(sec)
    return f'Done Sleeping...{sec}'


secs = [5, 4, 3, 2, 1]
for sec in secs:
    print(do_something(sec))

# END - Sequential programming
