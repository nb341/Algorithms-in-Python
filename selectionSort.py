"""
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
"""

def selectionSort(arr):
    for i in range(len(arr)):
        min_ = i
        for j in range(i+1, len(arr)):
            if(arr[j]<arr[min_]):
                min_ = j
        arr[i],arr[min_] = arr[min_],arr[i]
    return arr

if __name__=="__main__":
    a = [1,3,7,5,3,1,3,2,1,8,2,34,2,1]
    b = selectionSort(a)
    print(b)
