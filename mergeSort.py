import os
import time

def mergeSort(arr):
    if len(arr) > 1:
        left = arr[:len(arr) // 2] # left half
        right = arr[len(arr) // 2:] # right half

        mergeSort(left) # recursive call on left side
        mergeSort(right) # recursive call on right side

        i = 0 # array index pointer
        l = 0 # left subarry index pointer
        r = 0 # right subarray index pointer
        # compare and add smaller value
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
              arr[i] = left[l]
              l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1
        # if either pointer has not reached end, append remaining
        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1
        while r < len(right):
            arr[i]=right[r]
            r += 1
            i += 1

def tester(values):
    for val in values:
        arr.append(str(val))
    startTime = time.time()
    mergeSort(arr)
    elapsedMilli = (time.time() - startTime) * 1000
    return elapsedMilli    

def runner():
    for i in range(30):
        #### UNSORTED ####
        arr = []
        # small
        with open('input/unsorted/small/unsorted{}'.format(i), 'r') as file:
            values = file.readline()
            elapsedMilli = tester(values)
            with open('results/mergesort/unsorted/small/mergeSort_unsorted_small', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        arr = []
        # medium
        with open('input/unsorted/medium/unsorted{}'.format(i), 'r') as file:
            values = file.readline()
            elapsedMilli = tester(values)
            with open('results/mergesort/unsorted/medium/mergeSort_unsorted_medium', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        arr = []
        # large
        with open('input/unsorted/large/unsorted{}'.format(i), 'r') as file:
            values = file.readline()
            elapsedMilli = tester(values)
            with open('results/mergesort/unsorted/large/mergeSort_unsorted_large', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
                
if __name__ == '__main__':
    runner()
            

    