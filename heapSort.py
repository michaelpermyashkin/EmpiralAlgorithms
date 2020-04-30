import os, time

sortedHeap = []
def bottomUpHeap(arr):
    n = len(arr)
    for i in range(n//2, 0, -1):
        k = i # parent node index
        parentValue = arr[k-1] # value of parent
        heap = False
        while not heap and 2*k <= n:
            j = 2*k
            if j < n: # there are 2 children
                if arr[j-1] < arr[j]:
                    j+=1
            if parentValue >= arr[j-1]: # checks parental dominence 
                heap = True
            else:
                arr[k-1] = arr[j-1]
                k = j
        arr[k-1] = parentValue
            
def heapSort(arr):
    bottomUpHeap(arr)
    n = len(arr)-1
    for i in range (n, 0, -1):
        # swap 
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        sortedHeap.insert(0, arr[i])
        arr.pop(i)
        # rebuild heap
        bottomUpHeap(arr)
    sortedHeap.insert(0, arr[0])
      
      
# Executes quicksort and times program
def tester(values):
    arr = []
    for val in values:
        arr.append(int(val))
    startTime = time.time()
    heapSort(arr)
    elapsedMilli = (time.time() - startTime) * 1000
    return elapsedMilli    

# Handles reading and writing files for testing
def runner():
    for i in range(30):
        ################### UNSORTED ##########################
        # # small
        # with open('input/unsorted/small/unsorted{}'.format(i), 'r') as file:
        #     values = file.readlines()
        #     elapsedMilli = tester(values)
        #     with open('results/heapsort/unsorted/heapSort_unsorted_small', 'a+') as out:
        #         out.write((str(elapsedMilli))+'\n')
        # # medium
        with open('input/unsorted/medium/unsorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/unsorted/heapsort_unsorted_medium', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # large
        with open('input/unsorted/large/unsorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/unsorted/heapsort_unsorted_large', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
                
        ###################### Sorted ##########################
        # small
        with open('input/sorted/small/sorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/sorted/heapsort_sorted_small', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # medium
        with open('input/sorted/medium/sorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/sorted/heapsort_sorted_medium', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # large
        with open('input/sorted/large/sorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/sorted/heapsort_sorted_large', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
                
        ###################### Reverse ##########################
        # small
        with open('input/reverse/small/reverse{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/reverse/heapsort_reverse_small', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # medium
        with open('input/reverse/medium/reverse{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/reverse/heapsort_reverse_medium', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # large
        with open('input/reverse/large/reverse{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/reverse/heapsort_reverse_large', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
      
                
if __name__ == '__main__':
    runner()  

# arr = [2,9,7,6,9,100,1,-1,6,5,8]
# print('Before: {}'.format(arr))
# heapSort(arr)
# print('After: {}'.format(sortedHeap))