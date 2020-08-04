
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i] 
        j=i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key


if __name__ == "__main__":
    
    arr = [1,4,5,6,1,2,5,7,3,1]
    insertionSort(arr)
    print(arr)

        

