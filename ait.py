
arr = [1, 2, 4, 6, 3, 4, 1]

# get minimum value
def min_value(arr):
    min = arr[0]
    for x in arr:
        if x < min:
            min = x
    return min

# get max value index
def get_max_index(arr):
    min_index = 0
    for i, val in enumerate(arr):
        if arr[min_index] < val:
            min_index = i
    return min_index

# change values locations in the array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


# get middle value in an array
def median(arr):
    arr = sorted(arr)
    mid = len(arr) // 2    # int(len(arr)/2)
    if mid*2 == len(arr):
        return sum(arr[mid-1 : mid+1])/2
    else:
        return arr[mid]
    


def add_two_arrays(arr1, arr2):
    return arr1 + arr2


def add_two_arrays2(arr1, arr2):
    for j in arr2:
        arr1.append(j)
    return arr1

arr1 = [1, 2, 3]
arr2 = [4, 5]

# print(add_two_arrays(arr1, arr2))
# # [1, 2, 3, 4, 5]
# print(add_two_arrays2(arr1, arr2))
# # [1, 2, 3, [4, 5]]
# arr1.append(arr2)
# print(arr1)


def merge_sorted_arrays(arr1, arr2):
    arr3 = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1   # i = i + 1
        else: 
            arr3.append(arr2[j])
            j += 1
    
    arr3 += arr1[i:]
    arr3 += arr2[j:]

    return arr3

arr1 = [1, 2, 3, 9]
arr2 = [4, 5]
# print("merge sort")
# print(arr1)
# print(arr2)
# print(merge_sorted_arrays(arr1, arr2))


def average1(arr):
    s = 0
    for i in arr:
        s += i
    
    return s / len(arr)


def average2(arr):
    s = 0
    i = 0
    while i < len(arr):
        s += arr[i]
        i += 1

    return s / i



def has_value(arr, value):
    for i in arr:
        if value == i:
            return True
    return False


def has_value2(arr, value):
    index = 0 
    while index < len(arr):
        if arr[index] == value:
            return True
        index += 1
    
    return False


arr = [1, 2, 3, 5, 6, 7]
def get_value_index(arr, value):
    index = -1
    for i, val in enumerate(arr):
        if value == val:
            index = i
    return index



def avg2(arr):
    sx, sy = 0, 0
    for x, y in arr:
        sx, sy = sx + x, sy + y
    return sx/len(arr), sy/len(arr)


def distance(p1, p2):
    dx = p1[0] - p2[0] # p2[0] - p1[0]
    dy = p1[1] - p2[1]
    return (dx ** 2 + dy **2 )**0.5

 
def max(arr):
    mx = arr[0]
    for i in arr:
        if mx < i:
            mx = i
    return mx


arr = [[1,2], [200,300], [3,4], [5, 6], [6,8], [100,100]]
# m = avg2(arr) # [20, 20]
# d = []
# for i in arr:
#     dist = distance(i, m)
#     d.append(int(dist))
# print(arr)
# print(m)
# print(d)
# index = get_max_index(d)
# print(index)
# print(d[index])
# print(arr[index])



arr = [[1,2], [200,300], [3,4], [5, 6], [6,8], [100,100]]


def max_distance(arr):
    s = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            d = int(distance(arr[i], arr[j]))
            s.append([i, j, d])
    return s

def max_value_v3(arr):
    max = arr[0]
    for x in arr:
        if x[2] > max[2]:
            max = x
    return max

print(arr)
d = max_distance(arr)
print()
print(d)
print()
print(max_value_v3(d))
