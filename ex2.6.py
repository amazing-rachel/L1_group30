import timeit

def pow2(n):
    return pow(2, n)
elapsed_time = timeit.timeit(lambda: pow2(10000), number=10000)
print('Elapsed time for regular pow2:', elapsed_time, 'seconds.')

def pow2_loop(n):
    result = 1
    for i in range(n):
        result *= 2
    return result
elapsed_time2 = timeit.timeit(lambda: pow2_loop(1000), number=1000)
print('Elapsed time for the pow2 with a for loop:', elapsed_time2, 'seconds.')

def pow2_list(n):
    result = [2**i for i in range(n+1)]
    return result[n]
elapsed_time3 = timeit.timeit(lambda: pow2_list(1000), number=1000)
print('Elapsed time for the pow2 with list comprehension:', elapsed_time3, 'seconds.')

