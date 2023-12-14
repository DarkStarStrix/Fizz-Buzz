# write fizz buzz in one line
import time
import matplotlib.pyplot as plt
import concurrent.futures
import numba


# use a just in time compiler and multithreading to speed up the code write it in one line
@numba.jit(nopython=True)
def fizz_buzz_jit(i):
    divisible_by_3 = i % 3 == 0
    divisible_by_5 = i % 5 == 0
    return 'FizzBuzz' if divisible_by_3 and divisible_by_5 else 'Fizz' if divisible_by_3 else 'Buzz' if divisible_by_5 else str(i)


def measure_time(func, n):
    start_time = time.time ()
    for i in range (1, n):
        func (i)
    return time.time () - start_time


def compare():
    n = 1000
    times_normal = []
    times_jit_mt = []

    for i in range (1, n, 100):
        time_taken = measure_time (fizz_buzz_jit, i)
        times_normal.append (time_taken)
        with concurrent.futures.ThreadPoolExecutor () as executor:
            start_time = time.time ()
            list (executor.map (fizz_buzz_jit, range (1, i)))
            times_jit_mt.append (time.time () - start_time)

    plt.figure ()
    plt.plot (range (1, n, 100), times_normal, label='Normal')
    plt.plot (range (1, n, 100), times_normal, label='JIT')
    plt.plot (range (1, n, 100), times_jit_mt, label='JIT with multithreading')
    plt.xlabel ('Input size')
    plt.ylabel ('Time (seconds)')
    plt.title ('Execution time of FizzBuzz')
    plt.legend ()
    plt.show ()


compare ()
