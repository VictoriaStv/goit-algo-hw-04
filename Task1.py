import random
import timeit

def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

sizes = [100, 1000, 10000]
results = {}

for size in sizes:
    random_list = generate_random_list(size)
    
    merge_sort_time = timeit.timeit(lambda: merge_sort(random_list.copy()), number=1)
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(random_list.copy()), number=1)
    timsort_time = timeit.timeit(lambda: sorted(random_list.copy()), number=1)
    
    results[size] = {
        "Merge Sort": merge_sort_time,
        "Insertion Sort": insertion_sort_time,
        "Timsort": timsort_time
    }

for size, timing in results.items():
    print(f"Array Size: {size}")
    for algorithm, time_taken in timing.items():
        print(f"{algorithm}: {time_taken:.6f} seconds")
    print()
