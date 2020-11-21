import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    # Some task taking time
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Running now some work.....")
    some_work(3)
    print("Done......calling again")
    print("done")
    some_work(3)
    print("Called again")