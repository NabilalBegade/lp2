
n = int(input("No of Jobs : "))
arr = [[]]

for i in range(0,n):
    x = []
    a = input()
    a.append(x)
    b = input()
    b.append(x)
    c = input()
    c.append(x)

def jobScheduling(arr,time):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if(arr[j][2] < arr[j+1][2]):
                (arr[j],arr[j+1]) = (arr[j+1],arr[j])

    result = [False]*time

    job = ['-1']*time

    for i in range(len(arr)):
        for j in range(min(time-1,arr[i][1])-1,-1):
            if result[j] == False:
                result[j] = True
                job[j] = arr[i][0]
                break

    print(job)

print("Maximum Profit Sequence : ")
jobScheduling(arr,n)
