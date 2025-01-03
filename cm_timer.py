import time
from contextlib import contextmanager

# Реализация с использованием класса
class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f'time: {elapsed_time:.1f}')

# Реализация с использованием contextlib
@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    elapsed_time = time.time() - start_time
    print(f'time: {elapsed_time:.1f}')

# Пример использования
if __name__ == '__main__':
    from time import sleep

    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)
