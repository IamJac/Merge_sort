from array import *
def merge(data_array,left,mid,right):
    left_array_size=(mid-left)+1
    right_array_size=right-mid
    data2=array('i',[])
    data3=array('i',[])
    for l in range(left_array_size):
        data2.append(data_array[left+l])
    for m in range(right_array_size):
        data3.append(data_array[mid+1+m])
    n=int(0)
    o=int(0)
    p=left
    while n<left_array_size and o<right_array_size:
        if data2[n]<=data3[o]:
            data_array[p]=data2[n]
            n+=1
            p+=1
        else:
            data_array[p]=data3[o]
            o+=1
            p+=1
    while n<left_array_size:
        data_array[p]=data2[n]
        n+=1
        p+=1
    while o<right_array_size:
        data_array[p]=data3[o]
        o+=1
        p+=1

def merge_sort(data_array,left,right):
    if left<=right:
        mid=left+(right-left)//2
        merge_sort(data_array, left, mid-1)
        merge_sort(data_array, mid+1, right)
        merge(data_array,left,mid,right)
data=array('i',[])
size=int(input("Input size of the array"))
print("Input integral values into the array")
for i in range(size):
    num=int(input())
    data.append(num)
print("Unsorted array")
for j in data:
    print(j,end=" ")
merge_sort(data,0,size-1)
print("Sorted array")
for k in data:
    print(k,end=" ")
