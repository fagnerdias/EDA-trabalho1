import timeit
import random
import numpy as np

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while(i>=0 and a[i]>key):
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
    return a

def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    
    for i in range(0,n1):
        L[i] = a[p + i]
    for j in range(0,n2):
        R[j] = a[q + 1 + j]


    i = 0
    j = 0

    k = p
    while i < n1 and j < n2 :
        if(L[i] <= R[j]):
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1

def merge_sort(a, p, r):
    if p < r:
        q = ((p+(r-1))//2)
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)

def max_heapify(a, n, i):
    l = 2*i+1
    r = (2*i)+2
    if l < n and a[l]>a[i]:
        largest = l
    else:
        largest = i
    if r< n and a[r]>a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest],a[i]
        max_heapify(a, n, largest)

def heapsort(a):
    n = len(a)
    
    for i in range(n,-1,-1):
        max_heapify(a, n,i)
    
    for i in range(n-1,0,-1):
        a[i], a[0] = a[0],a[i]
        max_heapify(a, i, 0)

def partition(a, l, h):
    i = l-1
    pivot = a[h]
    for j in range(l, h):
        
        if a[j] <= pivot:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[h] = a[h],a[i+1]
    return(i+1)

def quicksort(a, l, h):
    if l < h:
        pi = partition(a, l, h)
        quicksort(a, l, pi-1)
        quicksort(a, pi+1,h)

def hibrido_merge_insertion(a, p, r, size):
    if (r-1)-p < size:
        insertion_sort(a)
        
    elif p < r:
        q = ((p+(r-1))//2)
        hibrido_merge_insertion(a, p, q, size)
        hibrido_merge_insertion(a, q+1, r, size)
        merge(a, p, q, r)

def hibrido_quick_insertion(a, l, h, size):
    if l < h:
        if l - h < size:
            insertion_sort(a)
        else:
            pi = partition(a, l, h)
            hibrido_quick_insertion(a, l, pi-1, size)
            hibrido_quick_insertion(a, pi+1,h, size)


######################## INSERTION SORT #########################
times_is = [0] * 10

for i in range(0, 10):
    a = random.sample(range(0,500), 500)
    start = timeit.default_timer()
    ordered = insertion_sort(a)
    stop = timeit.default_timer()
    times_is[i] = stop - start

mean_is_500 = np.mean(times_is)

print("--------------INSERTION SORT--------------------")
print("Tempo medio para entrada de tamanho 500: ",mean_is_500)

for i in range(0, 10):
    a = random.sample(range(0,5000), 5000)
    start = timeit.default_timer()
    ordered = insertion_sort(a)
    stop = timeit.default_timer()

    times_is[i] = stop - start

mean_is_5000 = np.mean(times_is)
print("Tempo medio para entrada de tamanho 5000: ",mean_is_5000)

for i in range(0, 10):

    a = random.sample(range(0,10000), 10000)
    start = timeit.default_timer()
    ordered = insertion_sort(a)
    stop = timeit.default_timer()

    times_is[i] = stop - start

mean_is_10000 = np.mean(times_is)
print("Tempo medio para entrada de tamanho 10000: ",mean_is_10000)

########################### MERGESORT ###########################
times_ms = [0] * 10
for i in range(0, 10):
    a = random.sample(range(0,500), 500)
    start = timeit.default_timer()
    merge_sort(a, 0, len(a)-1)
    stop = timeit.default_timer()
    times_ms[i] = stop - start
    
mean_ms_500 = np.mean(times_ms)
print("--------------MERGE SORT--------------------")
print("Tempo medio para entrada de tamanho 500: ",mean_ms_500)


for i in range(0, 10):
    a = random.sample(range(0,5000), 5000)
    start = timeit.default_timer()
    merge_sort(a, 0, len(a)-1)
    stop = timeit.default_timer()
    times_ms[i] = stop - start

mean_ms_5000 = np.mean(times_ms)
print("Tempo medio para entrada de tamanho 5000: ",mean_ms_5000)

for i in range(0, 10):
    a = random.sample(range(0,10000), 10000)
    start = timeit.default_timer()
    merge_sort(a, 0, len(a)-1)
    stop = timeit.default_timer()
    times_ms[i] = stop - start

mean_ms_10000 = np.mean(times_ms)
print("Tempo medio para entrada de tamanho 10000: ",mean_ms_10000)

######################## HEAPSORT ##############################

times_hs = [0] * 10
for i in range(0, 10):
    a = random.sample(range(0,500), 500)
    start = timeit.default_timer()
    heapsort(a)
    stop = timeit.default_timer()
    times_hs[i] = stop-start
    
mean_hs_500 = np.mean(times_hs)
print("--------------HEAP SORT--------------------")

print("Tempo medio para entrada de tamanho 500: ",mean_hs_500)

for i in range(0, 10):

    a = random.sample(range(0,5000), 5000)
    start = timeit.default_timer()
    heapsort(a)
    stop = timeit.default_timer()
    times_hs[i] = stop-start

mean_hs_5000 = np.mean(times_hs)
print("Tempo medio para entrada de tamanho 5000: ",mean_hs_5000)


for i in range(0, 10):
    a = random.sample(range(0,10000), 10000)
    start = timeit.default_timer()
    heapsort(a)
    stop = timeit.default_timer()
    times_hs[i] = stop-start

mean_hs_10000 = np.mean(times_hs)
print("Tempo medio para entrada de tamanho 10000: ",mean_hs_10000)


######################## QUICKSORT #############################

times_qs = [0] * 10
for i in range(0, 10):
    a = random.sample(range(0,500), 500)
    start = timeit.default_timer()
    quicksort(a,0,len(a)-1)
    stop = timeit.default_timer()
    times_qs[i] = stop-start

mean_qs_500 = np.mean(times_qs)
print("--------------QUICK SORT--------------------")
print("Tempo medio para entrada de tamanho 500: ",mean_qs_500)


for i in range(0, 10):
    a = random.sample(range(0,5000), 5000)
    start = timeit.default_timer()
    quicksort(a,0,len(a)-1)
    stop = timeit.default_timer()
    times_qs[i] = stop-start

mean_qs_5000 = np.mean(times_qs)
print("Tempo medio para entrada de tamanho 5000: ",mean_qs_5000)



for i in range(0, 10):

    a = random.sample(range(0,10000), 10000)
    start = timeit.default_timer()
    quicksort(a,0,len(a)-1)
    stop = timeit.default_timer()
    times_qs[i] = stop-start

mean_qs_10000 = np.mean(times_qs)
print("Tempo medio para entrada de tamanho 10000: ",mean_qs_10000)



#################### HIBRIDO MERGE-INSERTION #####################

times_hmi = [0] * 10

for i in range(0, 10):
    a = np.random.normal(range(0,500), 500)
    start = timeit.default_timer()
    ordered = hibrido_merge_insertion(a,0,len(a)-1,10)
    stop = timeit.default_timer()

    times_hmi[i] = stop - start
mean_hmi_500 = np.mean(times_hmi)
print("--------------HIBRIDO MERGE-INSERTION--------------------")
print("Tempo medio para entrada de tamanho 500: ",mean_hmi_500)



for i in range(0, 10):
    a = random.sample(range(0,5000), 5000)
    start = timeit.default_timer()
    ordered = hibrido_merge_insertion(a,0,len(a)-1,10)
    stop = timeit.default_timer()

    times_hmi[i] = stop - start
mean_hmi_5000 = np.mean(times_hmi)
print("Tempo medio para entrada de tamanho 5000: ",mean_hmi_5000)



for i in range(0, 10):
    a = random.sample(range(0,10000), 10000)
    start = timeit.default_timer()
    ordered = hibrido_merge_insertion(a,0,len(a)-1,10)
    stop = timeit.default_timer()

    times_hmi[i] = stop - start
mean_hmi_10000 = np.mean(times_hmi)
print("Tempo medio para entrada de tamanho 10000: ",mean_hmi_10000)



################## HIBRIDO QUICK-INSERTION #######################


times_hqi = [0] * 10
for i in range(0, 10):

    a = np.random.normal(range(0,500), 500)
    start = timeit.default_timer()
    ordered = hibrido_quick_insertion(a,0,len(a)-1,10)
    stop = timeit.default_timer()

    times_hqi[i] = stop - start
mean_hqi_500 = np.mean(times_hqi)
print("--------------HIBRIDO QUICK-INSERTION--------------------")
print("Tempo medio para entrada de tamanho 500: ",mean_hqi_500)


for i in range(0, 10):
    a = np.random.normal(range(0,5000), 5000)
    start = timeit.default_timer()
    ordered = hibrido_quick_insertion(a,0,len(a)-1,10)
    stop = timeit.default_timer()

    times_hqi[i] = stop - start
mean_hqi_5000 = np.mean(times_hqi)
print("Tempo medio para entrada de tamanho 5000: ",mean_hqi_5000)


for i in range(0, 10):
    a = np.random.normal(range(0,10000), 10000)
    start = timeit.default_timer()
    ordered = hibrido_quick_insertion(a,0,len(a)-1,10)
    stop = timeit.default_timer()

    times_hqi[i] = stop - start
mean_hqi_10000 = np.mean(times_hqi)
print("Tempo medio para entrada de tamanho 10000: ",mean_hqi_10000)

    