"""
Name : Cooper Williamson
Course : ICS4U
Date : 2024-11-19
File Name : main.py
Desc :

History : 2024-11-19 / created
"""
#imports

import time
import copy
import random as ran
import bogo_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort

#variables

arr = []
count = 0
isSorted = False

#functions
def genArr(arr, count) :
    """Generates an array using the Random module,
        change the count to 0 for a list of 10, 1 for 100, and anything over for 1000."""
    if count == 0 :
        
        for i in range(10) :
            arr.append(ran.randint(0,10))
            
    elif count == 1 :
        
        for i in range(100) :
            arr.append(ran.randint(0,100))
            
    else :
        
        for i in range(1000) :
            arr.append(ran.randint(0,1000))
            
    return(arr, count)

def printArr(arr, isSorted) :
    """Print any array for sorting passed through."""
    
    print('\n'*5)
    
    if isSorted :
        print('\tSorted List\t')
        
    else : print('\tUn-Sorted List\t')
    
    for i in range(len(arr)) :
        print('INDEX :\t',str(i),'\tVALUE :\t',str(arr[i]))

def bogo(arr) :
    """Bogo sorting algorithm"""
    bogo_sort.bogosort(arr)
    return(arr)

def bubble(arr) :
    """Bubble sorting algorithm"""
    bubble_sort.bubbleSort(arr)
    return(arr)

def insertion(arr) :
    """Insertion sorting algorithm"""
    insertion_sort.insertion_sort(arr)
    return(arr)

def merge(arr) :
    """Merge sorting algorithm"""
    merge_sort.merge_sort(arr, 0, len(arr) -1 )
    return(arr)

def quick(arr) :
    """Quick sorting algorithm"""
    size = len(arr)
    quick_sort.quickSort(arr, 0, size - 1)
    return(arr)

def selection(arr) :
    """Selection sorting algorithm"""
    selection_sort.selection_sort(arr)
    return(arr)

def sorting_bogo(arr) :
    #bogo
    bogoL = copy.copy(arr)
    bogo(bogoL)
    printArr(bogoL, isSorted=True)

def sorting_bubble(arr) :
    #bubble
    bubbleL = copy.copy(arr)
    bubble(bubbleL)
    printArr(bubbleL, isSorted=True)

def sorting_insertion(arr) :
    #insertion
    insertionL = copy.copy(arr)
    insertion(insertionL)
    printArr(insertionL, isSorted=True)

def sorting_merge(arr) :
    #merge
    mergeL = copy.copy(arr)
    merge(mergeL)
    printArr(mergeL, isSorted=True)

def sorting_quick(arr) :
    #quick
    quickL = copy.copy(arr)
    quick(quickL)
    printArr(quickL, isSorted=True)

def sorting_selection(arr) :
    #selection
    selectionL = copy.copy(arr)
    selection(selectionL)
    printArr(selectionL, isSorted=True)
    
def runSorts(arr, count) :
    if count == 0:
        print('\n\n\n\n\nMerge sorting :')
        sorting_merge(arr)
    elif count == 1:
        print('\n\n\n\n\nBogo sorting :')
        sorting_bogo(arr)
    elif count == 2:
        print('\n\n\n\n\nBubble sorting :')
        sorting_bubble(arr)
    elif count == 3:
        print('\n\n\n\n\nInsertion sorting :')
        sorting_insertion(arr)
    elif count == 4:
        print('\n\n\n\n\nQuick sorting :')
        sorting_quick(arr)
    elif count == 5:
        print('\n\n\n\n\nSelection sorting :')
        sorting_selection(arr)
    else : raise IndexError

def update(num) :
    genArr(arr, count=num)
    printArr(arr, isSorted=False)
    runSorts(arr, count=0)
    print('\n'*5)
    runSorts(arr, count=1)
    print('\n'*5)
    runSorts(arr, count=2)
    print('\n'*5)
    runSorts(arr, count=3)
    print('\n'*5)
    runSorts(arr, count=4)
    print('\n'*5)
    runSorts(arr, count=5)
    print('\n'*5)
    return
#main driver

update(0)
time.sleep(5)
update(1)
time.sleep(5)
update(2)
