import os, time

# function to construct intital heap using bottom-up approach
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
   
# function to reheap recursively after swap occurs 
def reheap(end,root):   
    leftChild = 2 * root + 1 # index of roots left child
    rightChild = 2 * (root + 1) # index of roots right child
    
    largest=root # before testing parental dominance we assume parent is larger than children
    
    # if left child is greated than parent, largest is set to left child index
    if leftChild < end and arr[largest] < arr[leftChild]:   
        largest = leftChild   
    
    # if right child is greated than parent, largest is set to right child index
    if rightChild < end and arr[largest] < arr[rightChild]:   
        largest = rightChild   
        
    # after comparing left and right child, if root is no longer largest we swap and reheap since heap does not hold parental dominance
    if largest != root:   
        arr[root], arr[largest] = arr[largest], arr[root]  
        reheap(end, largest)   


def heapSort(arr):  
    bottomUpHeap(arr) # builds heap bottom-up with initial array structure 
       
    n = len(arr) - 1 
    # iterate through heap backwards  
    for i in range(n, 0, -1):   
        arr[i], arr[0] = arr[0], arr[i] # swaps ith element with first element in array
        reheap(i, 0)   
        
     
arr = [] 
# Executes quicksort and times program
def tester(values):
    arr.clear()
    for val in values:
        arr.append(int(val))
    startTime = time.time()
    heapSort(arr)
    elapsedMilli = (time.time() - startTime) * 1000
    return elapsedMilli    

# Handles reading and writing files for testing
def runner():
    for i in range(30):
        ################# UNSORTED ##########################
        # small
        with open('input/unsorted/small/unsorted{}'.format(i), 'r') as file:
            values = file.readlines()
            elapsedMilli = tester(values)
            with open('results/heapsort/unsorted/heapSort_unsorted_small', 'a+') as out:
                out.write((str(elapsedMilli))+'\n')
        # medium
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
                
        ##################### Sorted ##########################
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
                
        ##################### Reverse ##########################
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