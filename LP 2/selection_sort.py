
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])


n = int(input("No of elements : "))
data = []
for i in range(0,n):
    x = int(input())
    data.append(x)

size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)