import os
import time

# Median of three implementation to determine pivot value for partition
def medianOfThree(arr, leftPointer, rightPointer):
    length = rightPointer - leftPointer
    # get left, right, middle values of subarray
    leftIndex = leftPointer
    left = arr[leftIndex]
    rightIndex = rightPointer -1
    right = arr[rightIndex]
    if length % 2 == 0:
        middleIndex = int(leftPointer + length/2 - 1)
        middle = arr[middleIndex]
    else:
        middleIndex = int(leftPointer + length/2)
        middle = arr[middleIndex]
    
    # determine median of left, middle, right --> return pivot and index of pivot
    if left < middle:
        if middle < right:
            return middle, middleIndex
        elif left < right:
            return right, rightIndex
        else:
            return left, leftIndex
    else:
        if left < right:
            return left, leftIndex
        elif middle > right:
            return middle, middleIndex
        else:
            return right, rightIndex

#A method to partition around the median
def medianPartition(arr, leftPointer, rightPointer):
    pivot, pivotIndex = medianOfThree(arr, leftPointer, rightPointer)

    arr[pivotIndex] = arr[leftPointer]
    arr[leftPointer] = pivot

    updatedPivotIndex = leftPointer + 1
    for j in range(leftPointer + 1, rightPointer):
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[updatedPivotIndex]
            arr[updatedPivotIndex] = temp
            updatedPivotIndex += 1

    leftPointerval = arr[leftPointer]
    arr[leftPointer] = arr[updatedPivotIndex-1]
    arr[updatedPivotIndex-1] = leftPointerval
    return updatedPivotIndex - 1 


def quicksort(arr, leftindex, rightindex):
    if leftindex < rightindex:
        pivotIndex = medianPartition(arr, leftindex, rightindex) # location of pivot for partition
        quicksort(arr, leftindex, pivotIndex) # recurse on left subarray
        quicksort(arr, pivotIndex + 1, rightindex) # recurse on tight subarray

# Executes quicksort and times program
def tester(values):
    # arr = [3,4,0,1,4,6,7,8,9,4,5,6,2,3,4,56,7,7,4,3,2,5,6,8,9,0,234,2356,46,4678,235,46]
    arr = []
    for val in values:
        arr.append(int(val))
    startTime = time.time()
    quicksort(arr, 0, len(arr))
    # print(arr)
    elapsedMilli = (time.time() - startTime) * 1000
    return elapsedMilli    

# Handles reading and writing files for testing
def runner():
    for i in range(30):
        ################### UNSORTED ##########################
        # small
        with open('input/unsorted/small/unsorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/unsorted/quickSort_unsorted_small', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # medium
        with open('input/unsorted/medium/unsorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/unsorted/quickSort_unsorted_medium', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # large
        with open('input/unsorted/large/unsorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/unsorted/quickSort_unsorted_large', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
                
        ###################### Sorted ##########################
        # small
        with open('input/sorted/small/sorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/sorted/quickSort_sorted_small', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # medium
        with open('input/sorted/medium/sorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/sorted/quickSort_sorted_medium', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # large
        with open('input/sorted/large/sorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/sorted/quickSort_sorted_large', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
                
        ###################### Reverse ##########################
        # small
        with open('input/reverse/small/reverse{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/reverse/quickSort_reverse_small', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # medium
        with open('input/reverse/medium/reverse{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/reverse/quickSort_reverse_medium', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # large
        with open('input/reverse/large/reverse{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/quicksort/reverse/quickSort_reverse_large', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
      
                
if __name__ == '__main__':
    runner()