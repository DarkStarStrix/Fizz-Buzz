# FizzBuzz JIT

FizzBuzz JIT is a Python project that solves the FizzBuzz problem using a just-in-time compiler and multithreading to speed up the code.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/DarkStarStrix/FizzBuzz_JIT.git
cd FizzBuzz_JIT

pip install -r requirements.txt

python -m unittest

The provided code is a Python script that uses the FizzBuzz problem to compare the execution time of a function when run normally and when run with multithreading.
The FizzBuzz problem is a common programming task, often used in coding interviews, that involves printing the numbers from 1 to a given number, but for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

The function `fizz_buzz_jit(i)` is a just-in-time compiled version of the FizzBuzz problem. It uses the `numba.jit` decorator to compile the function at runtime, which can significantly speed up the execution of the function. The function takes an integer `i` as input and returns 'FizzBuzz' if `i` is divisible by both 3 and 5, 'Fizz' if `i` is divisible by 3, 'Buzz' if `i` is divisible by 5, and the string representation of `i` otherwise.

```python
@numba.jit(nopython=True)
def fizz_buzz_jit(i):
    ...
```

The function `measure_time(func, n)` measures the execution time of a function `func` called with each integer from 1 to `n` (exclusive). It does this by recording the current time before and after the execution of the function and then subtracting the start time from the end time to get the total execution time.

```python
def measure_time(func, n):
    ...
```
The function `compare()` compares the execution time of the `fizz_buzz_jit` function when run normally and when run with multithreading. It does this by calling `measure_time` with `fizz_buzz_jit` and each integer from 1 to 1000 (exclusive) with a step of 100, both normally and with a ThreadPoolExecutor. The ThreadPoolExecutor is a high-level interface for asynchronously executing callables. 
It spins up multiple threads and allows `fizz_buzz_jit` to be executed concurrently, which can lead to a significant speedup if the function is CPU-bound and the machine has multiple cores.

```python
def compare():
    ...
```

Finally, the `compare()` function is called to start the comparison. The results are plotted using matplotlib, a popular data visualization library in Python. The x-axis represents the input size and the y-axis represents the execution time in seconds. There are three lines on the plot, one for the normal execution time, one for the just-in-time compiled execution time, and one for the just-in-time compiled execution time with multithreading.

```python
compare()
```
