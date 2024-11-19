"""
Name: Hudson Graham
File: Graham_Hudson_4U_EX0302_I_didnt_choose_this
Course: ICS4U-01
Desc: This is selection sort , kinda useless ngl cause python has .sort
"""

import random
def selection_sort(theList):
    for i in range(len(theList)):
        min_index = i
 
        for j in range(i + 1, len(theList)):
            # select the minimum element in every iteration
            if theList[j] < theList[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (theList[i], theList[min_index]) = (theList[min_index], theList[i])
    return theList