
# arr = [1, 2, 4, 6, 3, 4, 1]

# # get minimum value
# def min_value(arr):
#     min = arr[0]
#     for x in arr:
#         if x < min:
#             min = x
#     return min

# # get max value index
# def get_max_index(arr):
#     min_index = 0
#     for i, val in enumerate(arr):
#         if arr[min_index] < val:
#             min_index = i
#     return min_index

# # change values locations in the array
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#     return arr


# # get middle value in an array
# def median(arr):
#     arr = sorted(arr)
#     mid = len(arr) // 2    # int(len(arr)/2)
#     if mid*2 == len(arr):
#         return sum(arr[mid-1 : mid+1])/2
#     else:
#         return arr[mid]
    


# def add_two_arrays(arr1, arr2):
#     return arr1 + arr2


# def add_two_arrays2(arr1, arr2):
#     for j in arr2:
#         arr1.append(j)
#     return arr1

# arr1 = [1, 2, 3]
# arr2 = [4, 5]

# # print(add_two_arrays(arr1, arr2))
# # # [1, 2, 3, 4, 5]
# # print(add_two_arrays2(arr1, arr2))
# # # [1, 2, 3, [4, 5]]
# # arr1.append(arr2)
# # print(arr1)


# def merge_sorted_arrays(arr1, arr2):
#     arr3 = []
#     i = 0
#     j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             arr3.append(arr1[i])
#             i += 1   # i = i + 1
#         else: 
#             arr3.append(arr2[j])
#             j += 1
    
#     arr3 += arr1[i:]
#     arr3 += arr2[j:]

#     return arr3

# arr1 = [1, 2, 3, 9]
# arr2 = [4, 5]
# # print("merge sort")
# # print(arr1)
# # print(arr2)
# # print(merge_sorted_arrays(arr1, arr2))


# def average1(arr):
#     s = 0
#     for i in arr:
#         s += i
    
#     return s / len(arr)


# def average2(arr):
#     s = 0
#     i = 0
#     while i < len(arr):
#         s += arr[i]
#         i += 1

#     return s / i # s / len(i)



# def has_value(arr, value):
#     for i in arr:
#         if value == i:
#             return True
#     return False


# def has_value2(arr, value):
#     index = 0 
#     while index < len(arr):
#         if arr[index] == value:
#             return True
#         index += 1
    
#     return False


# arr = [1, 2, 3, 5, 6, 7]
# def get_value_index(arr, value):
#     index = -1
#     for i, val in enumerate(arr):
#         if value == val:
#             index = i
#     return index



# def avg2(arr):
#     sx, sy = 0, 0
#     for x, y in arr:
#         sx, sy = sx + x, sy + y
#     return sx/len(arr), sy/len(arr)


# def distance(p1, p2):
#     dx = p1[0] - p2[0] # p2[0] - p1[0]
#     dy = p1[1] - p2[1]
#     return (dx ** 2 + dy **2 )**0.5

 
# def max2(arr):
#     mx = arr[0]
#     for i in arr:
#         if mx < i:
#             mx = i
#     return mx


# arr = [[1,2], [200,300], [3,4], [5, 6], [6,8], [100,100]]
# # m = avg2(arr) # [20, 20]
# # d = []
# # for i in arr:
# #     dist = distance(i, m)
# #     d.append(int(dist))
# # print(arr)
# # print(m)
# # print(d)
# # index = get_max_index(d)
# # print(index)
# # print(d[index])
# # print(arr[index])



# arr = [[1,2], [200,300], [3,4], [5, 6], [6,8], [100,100]]


# def max_distance(arr):
#     s = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             d = int(distance(arr[i], arr[j]))
#             s.append([i, j, d])
#     return s

# def max_value_v3(arr):
#     max = arr[0]
#     for x in arr:
#         if x[2] > max[2]:
#             max = x
#     return max

# # print(arr)
# # d = max_distance(arr)
# # print()
# # print(d)
# # print()
# # print(max_value_v3(d))

# def min_value3(arr):
#     min = arr[0]
#     for x in arr:
#         if x > min:
#             min = x
#     return min


# def max3(arr):
#     max = arr[0]

#     for i in arr:
#         if i[0] >= max[0] and i[1] >= max[1] and i[2] > max[2]:
#             max = i
#     return max


# arr = [[2005, 10, 10], [2005, 10, 9], [2005, 3, 18],
#        [2005, 12, 29], [2003, 1, 19], [2006, 7, 13]]

# # print(min_value3(arr))
# # print(max3(arr))
# # print(max(arr))


# def has_word(s, x):
#     for i in range(len(s)):
#         if x == s[i:i+len(x)]:
#             return True
#     return False


# s = "emilbek bilgazyev"
# x = "sbek"
# #print(has_word(s, x))

# # print(s.upper())
# # print(s.split(' '))

# s = '''
# 1914 translation by H. 
# "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."

# help@lipsum.com
# Privacy Policy · Do Not Sell My Personal Information · Change Consent

# AD'''

# # print(has_word(s, 'emil'))
# # print(len(s))
# words = s.split()

# # print(words)
# # print(len(words))
# # print('sails' in words)

# def get_word_lengths(words):
#     arr = []
#     for i in words:
#         length = len(i)
#         arr.append(len(i))
#     return arr

# def count_words(arr, d):
#     count = 0
#     for i in arr:
#         if i == d:
#             count += 1
#     return count

# arr = get_word_lengths(words)
# #print(arr)
# s = []
# for x in set(arr):
#     s.append([x, count_words(arr, x)])



# def get_max4(arr):
#     max = arr[0]
#     for i in arr:
#         if i[1] > max[1]:
#             max = i
#     return max

    
# # print(s)
# # print(get_max4(s)) 

# def my_split(s, sep):
#     x = ''
#     for c in s:
#         if c != sep:
#             x += c
#         else:
#             print(x)
#             x = ''
#     print('last', x)

# s = 'ab,cd,ef,gh,'
# # my_split(s, ',')


# from random import randint

# def experiment(N):
#     arr = [0]*13
#     varr = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
#     for i in range(N):
#         d1 = randint(1, 6)
#         d2 = randint(1, 6)
#         d = d1 + d2
#         arr[d] += 1

#     for k, (i, j) in enumerate(zip(arr, varr)):
#         print(k, i/N - j/36, i, i)



# # for N in [10, 100, 1000, 10000, 1000000, 10000000]:
# #     print("*****", N, "******")
# #     experiment(N)

# s = "a, b, cd, efg, abkg, abcdef"
# # print(s.split())
# # print(max(s.split(), key = lambda i:len(i)))


# # arr = (1, 2)
# # arr[0] = 2
# # print(arr)



# # #print(min_value([1,2,3,4]))
# # # arr = list(range(10))
# # # print(arr)
# # # print(arr[:5:-1])
# # # print(arr[5:2:-3])
# # # print(arr[::2])
# # # print(arr[::-2])


# # # arr = [1, 2, 3]
# # # arr.append(1, 5)
# # # print(arr)


# # salary = 8000

# # def printSalary():
# #   salary = 12000
# #   print("Salary:", salary)

# # def printSalary2():
# #   #salary = 10000
# #   print("Salary:", salary)
  
# # printSalary()
# # print("Salary:", salary)
# # printSalary2()


# from random import randint

# #print([randint(1, 18) for i in range(3)])


# def f(arr):
#     x = 0
#     for diana in arr:
#         if diana < x:
#             x = diana
#     return x

# arr = [1,2,3,2]
# #print('result:', f(arr))


# # s = "emil bilgazyev"
# # s[3], s[1] = s[2], s[5]
# #print(s)


# def f2(arr):
#     x = 1
#     for user, index in enumerate(arr):
#         if user == x:
#             print(index)

# arr = [1,2,3,2,1,5,6,2]
# #f2(arr)

# def f3(arr):
#     max = 0
#     for index in arr:
#         if len(index) < max:
#             max = len(index)
#     return max

# arr = ['abc', 'bc', 'd', 'ab']
# #print(f3(arr))

# arr1 = [1,2,3,1,2]
# arr2 = [1,2,2]

# def f4(arr1, arr2):
#     result = []
#     for val1, i in enumerate(arr1):
#         for val2, j in enumerate(arr2):
#             if i == j:
#                 result = [val1, val2]
#     return result

# #print(f4(arr1, arr2))


# arr1 = [1,2,3,3,4]
# arr2 = [2,3,5,5,5]


# #print((set(arr2) - set(arr1)))
# #print(arr2(2))
# #print( (set(arr1) & set(arr2(2))) | (set(arr2) - set(arr1)) )

# # def f():
#     # return 1

# # x = input('val1: ')
# # y = input('val2: ')
# # print('result:', max(x, y))

# x = [1,2,3,4,5,6]
# y = [0,0,0,0,0]

# x[0], y[1] = x[2], y[0]
# #print(x)

# arr = [1,2,3,4,5,2,1,6,2]
# #print('before', arr)
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]

# #print('after', arr)

# arr1 = list(range(1,19))
# from random import shuffle

# arr2 = list(range(1,19))
# shuffle(arr2)
# #print(list(zip(arr1,arr2)))

# from random import randint

# val1 = randint(0,10)
# val2 = randint(0,10)

# # s1 = "{} plus {} equals {}".format(val1, val2, val1+val2)
# # s2 = f"{val1} plus {val2} equals {val1+val2}"
# # print(s1)
# # print(s2)


# # fb = open("secondfile.txt", "w")

# # for i in range(100):
# #     val1 = randint(0,10)
# #     val2 = randint(0,10)
# #     s2 = f"{val1}+{val2}=\n"
# #     fb.write(s2)

# # fb.close()


# # fb = open("C:/Users/bekem/Downloads/testfile.xyz", "r")
# # for x in fb:
# #     print(x)
# # fb.close()



# # fb = open("file2.py", "r")
# # fnew = open('fil2_new.py', "w")

# # for x in fb:
# #     x = x.replace("arr", "massive")
# #     fnew.write(x)



# code = """
# from random import randint
# def calc():
#     a = int(input("Input first value:"))
#     b = int(input("Input second value:"))
#     x = a + b
#     s = f'{a} + {b} = '
#     result = int(input(s))
#     if result == x:
#        print("Pravilno")
#     else:
#        print("HEEEEEEET")

# while True: `
#   calc()
# """

# # fb = open('C:/Users/bekem/Downloads/aziz.py', 'w')
# # fb.write(code)
# # fb.close()


# def maxValue(arr):
#     mx = arr[0]
#     for i in arr:
#         if i > mx:
#             mx = i
#     return mx

# arr = [1,2,4,2]

# if maxValue(arr) == 4:
#     print("Manual test correct")
# else:
#     print("Manual Test incorrect")


# # for i in range(1,4):
# #     fb = open(f'C:/Users/bekem/Downloads/tests/test_{i}.txt', 'r')
# #     line = fb.read()
# #     first, second = line.split('\n')
# #     s_arr = first.split(',')
# #     arr = [int(i) for i in s_arr]
# #     max_val = int(second)
# #     print(arr, max_val)
# #     if max_val == maxValue(arr):
# #         print(f"test_{i}.txt passed")
# #     else:
# #         print(f"test_{i}.txt failed!!!")


# # fb = open('input.txt', 'r')
# # fb_hacked = open('hacked.txt', 'w')
# # line = fb.read()
# # words = line.split()

# # res = []
# # for word in words:
# #     res.append(word[::-1])

# # fb_hacked.write(' '.join(res))

    
# # print([randint(1,19) for i in range(2)])

# def mymax(sub_str):
#     sarr = sub_str.split(",")
#     x = []
#     for i in sarr:
#         x.append(int(i))
#     return max(x)

# # print("mymax 1,5,2", mymax("1,5,2"))

# # fin = open('input.txt', 'r')
# # fout  = open('output.txt', 'w')
# # line = fin.readlines()
# # out = []
# # for i in line:
# #     stripped_i = i.strip()
# #     x = f"{stripped_i},{mymax(stripped_i)}"
# #     out.append(x)
# # print(out)
# # fout.write('\n'.join(out))


# # s = '         emil  \n\n\n    '
# # print(s)
# # print(len(s))
# # stripped_s = s.strip()
# # print(stripped_s)
# # print(len(stripped_s))



# def bek(s, i):
#     if i == len(s):
#         # print(''.join(s))
#         x = ''.join(s)
#         if 'iu' not in x and 'ui' not in x:
#             print(x)
    
#     for a in range(i, len(s)):
#         s[a], s[i] = s[i], s[a]
#         bek(s, i+1)
#         s[a], s[i] = s[i], s[a]
        

# s = 'quiz'
# bek(list(s),0)

# # from itertools import permutations

# # s = 'quiz'
# # for i in permutations(list(s)):
# #     print(i)

# fi = open('output.txt')
# for i in fi: # "1,2,3" -> ["1", "2", "3"] -> [1,2,3]
#     arr = []
#     for j in i.split(","):
#         arr.append(int(j))
#     if sum(arr) == 15:
#         print(i)

# SIMILAR CODE TO ABOVE BUT IN ONE LINE
#print([i for i in open('output.txt') if sum([int(j) for j in i.split(",")])==15])

# REPLACE "arr" with "massive" word
# fi = open('input.txt', 'r')
# line = fi.read()
# new_line = line.replace("arr", "massive")

# fo = open("new_input.txt", 'w')
# fo.write(new_line)

# LISTING FILES IN THE DIRECTORY AND DELETING MATCHING FILES
import os
# files = os.listdir()
# print(list(files))
# for emil in list(files):
#     if 'txt' in emil:
#         os.remove(emil)

#os.remove('bek.html')

# COPY FILES 
# import shutil
# for i in range(100):
#     shutil.copyfile('index.html', f'index{i}.html')

# DELETE FILES
# import os
# files = os.listdir()
# for i in files:
#     if '.html' in i:
#         os.remove(i)


# READING CSV FILE AND PRINTING CONTENTS
# import csv
# fi = open('input.txt', 'r')
# vals = csv.reader(fi)
# for i in vals:
#     print(i)


# READING payments.txt and names.txt and printing 
# QUANTITY AND TOTAL AMOUNT

import csv
payments_reader = csv.reader(open('payments.txt'))
names_reader = csv.reader(open('names.txt'))
names = [name for id, name in names_reader]
amounts = [0]*len(list(names))
for id,date,payment in payments_reader:
    amounts[int(id)] += int(payment)

for name, amount in zip(names, amounts):
    print(name, amount)
