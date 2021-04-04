arr = [12, 15, 7, 11, 10]
qwerty = len(arr)
arr=sorted(arr)
i = 1
result=[]
while i < int((qwerty/2)+1):
    result.append(arr[0-i])
    result.append(arr[i-1])
    i+=1
if (qwerty % 2) == 1:
     result.append(arr[0-i])


print(result)
