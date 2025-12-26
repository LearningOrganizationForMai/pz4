import time
import logging
from functools import lru_cache

logging.basicConfig(
    level=logging.INFO,
    filename="phibanachi.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(levelname)s %(message)s"
)

def fib_int(n):
    if n < 0: raise ValueError("Число должно быть неотрицальным")
    elif n == 0: return 0
    elif n < 3: return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@lru_cache
def fib_rec(n):
    if n < 0:
        raise ValueError("Число должно быть неотрицальным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

a = 50
timeStart = time.time()
fib_int(a)
timeFinish = time.time()
logging.info(f"Интерактивный способ занимает: {timeFinish-timeStart}")
timeStart = time.time()
fib_rec(a)
timeFinish = time.time()
logging.info(f"Рекурсивный способ занимает: {timeFinish-timeStart}")


