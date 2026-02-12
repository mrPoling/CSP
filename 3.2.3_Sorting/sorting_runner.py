import random
import time
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
import merge_sort
from quick_sort import quick_sort

#Generate array of unique integers, sampled from a range;
#DON'T CHANGE THESE VALUES

#Change the array_doublings value when you call this function, to process longer arrays
def measure_sorting_function(func, array_length=6400):
    """
    Increase array length by doubling it array_doublings times:
    TIP: Start at 6 and ramp up by slowly
    """
    array = [random.randint(-array_length, array_length) for _ in range(array_length)]
    # print(array)
    print("\nSort algorithm:", func.__name__)
    print("  Array length:", len(array))

    start_time = time.perf_counter()
    result = func(array)
    end_time = time.perf_counter()
    
    if ("merge" in func.__name__):
        # seems like simplest way to get counter from merge_sort, due to recursion
        comparisons = merge_sort.get_counter()
    else:
        comparisons = result[1]
    print(" # comparisons:", comparisons)
    elapsed_time = round(end_time - start_time, 1)
    print(f"  Elapsed time: {elapsed_time} seconds\n")

#TIP: Good start value for array_length is 2^13, or 8192 (which you can write as 2**13 in Python)
# Then double it & run again, then again . . . 
# You'll want to COMMENT OUT insertion and bubble sort lines after about 2**16 or so
array_length = 2**13
measure_sorting_function(insertion_sort, array_length)
measure_sorting_function(bubble_sort, array_length)
measure_sorting_function(merge_sort.merge_sort, array_length)
measure_sorting_function(quick_sort, array_length)


