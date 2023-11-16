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
def median(arr):
    arr = sorted(arr)
    mid = len(arr) // 2    # int(len(arr)/2)
    if mid*2 == len(arr):
        return sum(arr[mid-1 : mid+1])/2
    else:
        return arr[mid]
    


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

# ### GET MIN VALUE WHERE EACH ELEMENT CONTAINS THREE VALUES
# def min_value3(arr):
#     min = arr[0]
#     for x in arr:
#         if x > min:
#             min = x
#     return min
# ### GET MAX VALUE WHERE EACH ELEMENT CONTAINS THREE VALUES
# def max3(arr):
#     max = arr[0]
#     for i in arr:
#         if i[0] >= max[0] and i[1] >= max[1] and i[2] > max[2]:
#             max = i
#     return max

# arr = [[2005, 10, 10], [2005, 10, 9], [2005, 3, 18],
#        [2005, 12, 29], [2003, 1, 19], [2006, 7, 13]]

# print(min_value3(arr))
# print(max3(arr))
# print(max(arr))


# ### CHECK THE WORD
# def has_word(s, x):
#     for i in range(len(s)):
#         if x == s[i:i+len(x)]:
#             return True
#     return False
# ### TEST
# s = "emilbek bilgazyev"
# x = "sbek"
# print(has_word(s, x))

# ### UPPER, SPLIT
# print(s.upper())
# print(s.split(' '))

# s = '''
# What is Lorem Ipsum?
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# '''
# words = s.split()
# print(words)
# print(len(words))
# print('sails' in words)
# ### GIVEN AN ARRAY OF WORDS RETURN EACH WORDS LENGTH
# def get_word_lengths(words):
#     arr = []
#     for i in words:
#         length = len(i)
#         arr.append(len(i))
#     return arr
# ### COUNT HOW MANY WORDS IN AN ARRAY MATCH TO A GIVEN ARRAY
# def count_words(arr, d):
#     count = 0
#     for i in arr:
#         if i == d:
#             count += 1
#     return count

# arr = get_word_lengths(words)
# print(arr)
# ### FOREACH WORD COUNT HOW MANY TIMES IT OCCURED
# s = []
# for x in set(arr):
#     s.append([x, count_words(arr, x)])
# ### GET MAX LENGTH
# def get_max4(arr):
#     max = arr[0]
#     for i in arr:
#         if i[1] > max[1]:
#             max = i
#     return max

# print(s)
# print(get_max4(s)) 

# ### CUSTOM SPLITTING 
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
# my_split(s, ',')

# ### RUNNING EXPERIMENTS TO TRY MULTIPLE 
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

# for N in [10, 100, 1000, 10000, 1000000, 10000000]:
#     print("*****", N, "******")
#     experiment(N)


# ### USING LAMBDA FUNCTION TO FIND LONGEST LENGHT OF WORD
# s = "a, b, cd, efg, abkg, abcdef"
# print(s.split())
# print(max(s.split(), key = lambda i:len(i)))


# ### TUPLE CANNOT BE CHANGED
# arr = (1, 2)
# arr[0] = 2
# print(arr)


# ### SUB ARRAY, ARRAY MANIPULATIONS
# arr = list(range(10))
# print(arr)
# print(arr[:5:-1])
# print(arr[5:2:-3])
# print(arr[::2])
# print(arr[::-2])


# arr = [1, 2, 3]
# arr.append(1, 5)
# print(arr)


# ### GLOBAL VS LOCAL VALUES, GLOBAL VALUES WONT BE CHANGED IF IT IS USED IN LOCAL E.G. salary is declared globally and locally
# salary = 8000
# def printSalary():
#   salary = 12000
#   print("Salary:", salary)

# def printSalary2():
#   #salary = 10000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)
# printSalary2()


# ### IT WILL ALWAYS RETURN 0 UNLESS ARR CONTAINS NEGATIVE VALUES, E.G. IT WILL RETURN SMALLEST VALUE THAT IS SMALLER THAN 0
# def f(arr):
#     x = 0
#     for diana in arr:
#         if diana < x:
#             x = diana
#     return x

# arr = [1,2,3,2]
# print('result:', f(arr))

# ### STRING VALUES CONNOT BE CHANGED, WILL RESULT IN ERROR
# s = "emil bilgazyev"
# s[3], s[1] = s[2], s[5]
# print(s)

# ###  RETURN FIRST INDEX E.G. user == x (1==1)
# def f2(arr):
#     x = 1
#     for user, index in enumerate(arr):
#         if user == x:
#             print(index)

# arr = [1,2,3,2,1,5,6,2]
# f2(arr)

# ### RETURNS 0 (MIN VALUE) SINCE CONDITION IS INCORRECT TO RETURN MAX LEN
# def f3(arr):
#     max = 0
#     for index in arr:
#         if len(index) < max:
#             max = len(index)
#     return max

# arr = ['abc', 'bc', 'd', 'ab']
# print(f3(arr))


### RETURN LAST MATCHED INCICES BETWEEN TWO ARRAYS
# def f4(arr1, arr2):
#     result = []
#     for val1, i in enumerate(arr1):
#         for val2, j in enumerate(arr2):
#             if i == j:
#                 result = [val1, val2]
#     return result

# arr1 = [1,2,3,1,2]
# arr2 = [1,2,2]
# print(f4(arr1, arr2))


### SET OPERATIONS: BEK VALUNTEERED TO SOLVE IT WHICH HE WAS NOT ABLE TO 
# arr1 = [1,2,3,3,4]
# arr2 = [2,3,5,5,5]
# print((set(arr2) - set(arr1)))
# print(arr2(2))
# print( (set(arr1) & set(arr2(2))) | (set(arr2) - set(arr1)) )


# ### CONFUSING STUDENTS
# def f():
#    return 1

# x = input('val1: ')
# y = input('val2: ')
# print('result:', max(x, y))

# ### MULTIPLE ASSIGNMENTS IN ONE ROW
# x = [1,2,3,4,5,6]
# y = [0,0,0,0,0]
# x[0], y[1] = x[2], y[0]
# print(x)


# ### SORTING ARRAY
# arr = [1,2,3,4,5,2,1,6,2]
# print('before', arr)
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print('after', arr)

# ### GENERATE A FUNCTION TO MOVE PEOPLE AROUND
# arr1 = list(range(1,19))
# from random import shuffle
# arr2 = list(range(1,19))
# shuffle(arr2)
# print(list(zip(arr1,arr2)))


# ### FORMATTING A STRING
# from random import randint
# val1 = randint(0,10)
# val2 = randint(0,10)
# s1 = "{} plus {} equals {}".format(val1, val2, val1+val2)
# s2 = f"{val1} plus {val2} equals {val1+val2}"
# print(s1)
# print(s2)


# ### WRITE MULTIPLE ADDITION QUESTIONS E.G. "4+5=" TO A FILE
# fb = open("secondfile.txt", "w")
# for i in range(100):
#     val1 = randint(0,10)
#     val2 = randint(0,10)
#     s2 = f"{val1}+{val2}=\n"
#     fb.write(s2)

# fb.close()

# ### ALTERNATIVE WAY TO READ A FILE WITHOUT fb.read
# fb = open("C:/Users/bekem/Downloads/testfile.xyz", "r")
# for x in fb:
#     print(x)
# fb.close()


# ### REPLACING "arr" WITH "massive" IN A FILE AND WRITING TO A NEW FILE
# fb = open("file2.py", "r")
# fnew = open('fil2_new.py', "w")

# for x in fb:
#     x = x.replace("arr", "massive")
#     fnew.write(x)


# ### WRITING A SCRIPT TO A FILE WHERE WE CAN RUN IT LATER
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

# fb = open('C:/Users/bekem/Downloads/aziz.py', 'w')
# fb.write(code)
# fb.close()


# ### MAX
# def maxValue(arr):
#     mx = arr[0]
#     for i in arr:
#         if i > mx:
#             mx = i
#     return mx

# ### TESTING maxValue
# arr = [1,2,4,2]
# if maxValue(arr) == 4:
#     print("Manual test correct")
# else:
#     print("Manual Test incorrect")


# ### READING MULTIPLE FILES. e.g. we have test_1.txt, test_2.txt, test_3.txt ... and testing maxValue function above
# ### EACH file first row contains number "1,5,3,2,1" second line contains "max value"
# for i in range(1,4):
#     fb = open(f'C:/Users/bekem/Downloads/tests/test_{i}.txt', 'r')
#     line = fb.read()
#     first, second = line.split('\n')
#     s_arr = first.split(',')
#     arr = [int(i) for i in s_arr]
#     max_val = int(second)
#     print(arr, max_val)
#     if max_val == maxValue(arr):
#         print(f"test_{i}.txt passed")
#     else:
#         print(f"test_{i}.txt failed!!!")


# ### GENERATING CORRUPTED FILE: OPEN AN INPUT TEXT AND REVERSE EACH WORD AND WRITE TO A NEW FILE
# fb = open('input.txt', 'r')
# fb_hacked = open('hacked.txt', 'w')
# line = fb.read()
# words = line.split()
# res = []
# for word in words:
#     res.append(word[::-1])
# fb_hacked.write(' '.join(res))


# ### GENERATE TWO RANDOM NUMBERS
# from random import randint
# print([randint(1,19) for i in range(2)])


# ### GIVEN A STRING with numbers e.g. "1,2,3,4" finds max value in it
# def mymax(sub_str):
#     sarr = sub_str.split(",")
#     x = []
#     for i in sarr:
#         x.append(int(i))
#     return max(x)

# print("mymax 1,5,2", mymax("1,5,2"))

# ### READS FILES WHERE EACH ROW IS COMMA SEPERATED NUMBERS AND RETURNS MAX VALUE FOR EACH AND WRITES TO FILE
# fin = open('input.txt', 'r')
# fout  = open('output.txt', 'w')
# line = fin.readlines()
# out = []
# for i in line:
#     stripped_i = i.strip()
#     x = f"{stripped_i},{mymax(stripped_i)}"
#     out.append(x)
# print(out)
# fout.write('\n'.join(out))


# ### STRIP: remove empty spaces, tabs, new lines
# s = '         emil  \n\n\n    '
# print(s)
# print(len(s))
# stripped_s = s.strip()
# print(stripped_s)
# print(len(stripped_s))



# ### PERMUTATIONS
# def my_permute(s, i):
#     if i == len(s):
#         # print(''.join(s))
#         x = ''.join(s)
#         if 'iu' not in x and 'ui' not in x:
#             print(x)
    
#     for a in range(i, len(s)):
#         s[a], s[i] = s[i], s[a]
#         my_permute(s, i+1)
#         s[a], s[i] = s[i], s[a]
        

# s = 'quiz'
# my_permute(list(s),0)

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

# ###SIMILAR CODE TO ABOVE BUT IN ONE LINE
#print([i for i in open('output.txt') if sum([int(j) for j in i.split(",")])==15])

# ###REPLACE "arr" with "massive" word
# fi = open('input.txt', 'r')
# line = fi.read()
# new_line = line.replace("arr", "massive")

# fo = open("new_input.txt", 'w')
# fo.write(new_line)

# ###LISTING FILES IN THE DIRECTORY AND DELETING MATCHING FILES
# import os
# files = os.listdir()
# print(list(files))
# for emil in list(files):
#     if 'txt' in emil:
#         os.remove(emil)

#os.remove('bek.html')

# ###COPY FILES 
# import shutil
# for i in range(100):
#     shutil.copyfile('index.html', f'index{i}.html')

# ###DELETE FILES
# import os
# files = os.listdir()
# for i in files:
#     if '.html' in i:
#         os.remove(i)


# ### READING CSV FILE AND PRINTING CONTENTS
# import csv
# fi = open('input.txt', 'r')
# vals = csv.reader(fi)
# for i in vals:
#     print(i)


# ### READING payments.txt and names.txt and printing 
# ### QUANTITY AND TOTAL AMOUNT

# import csv
# payments_reader = csv.reader(open('payments.txt'))
# names_reader = csv.reader(open('names.txt'))
# names = [name for id, name in names_reader]
# amounts = [0]*len(list(names))
# for id,date,payment in payments_reader:
#     amounts[int(id)] += int(payment)

# for name, amount in zip(names, amounts):
#     print(name, amount)


# ###COMBINATIONS: order matters
# arr = [0, 1, 2, 3, 4]
# n = 0
# for i in range(0, 5):
#     for j in range(i+1, 5):
#         for k in range(j+1, 5):
#             n += 1
#             print(i, j, k)
# print('total combinations:', n)



# ### PERMUTATIONS: order does not matter
# n = 0
# for i in range(0, 5):
#     for j in range(0, 5):
#         for k in range(0, 5):
#             if not (i==j or j == k or i == k):
#                 n += 1
#                 print(i, j, k)
# print('total permutations:', n)


# ### ALL VARIATIONS: reuse of values
# n = 0
# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             n += 1
#             print(i,j,k)

# print('total variations: ', n)


### READING FILES personal_info.txt, transactions.txt

# import csv
# reader_personal = csv.reader(open("personal.txt"))
# reader_transactions = csv.reader(open("transactions.txt"))

# names = [name for id,name,tel,address in reader_personal]
# super_arr = [[] for i in range(len(names))]
# print(super_arr)
# for id, date, amount in reader_transactions:
#     super_arr[int(id)].append(int(amount))
#     print(id, date, amount, super_arr)

# def myavg(arr):
#     s = 0
#     c = 0
#     for val in arr:
#         c += 1
#         s += val
#     return s/c

# for name, arr in zip(names, super_arr):
#     print(name, arr, sum(arr), max(arr), len(arr), myavg(arr), sum(arr)/len(arr))


# import csv
# reader_students = csv.reader(open(f"students.txt"))
# reader_classes = csv.reader(open(f"classes.txt"))
# reader_classes_taken= csv.reader(open(f"taken.txt"))

# stud = list(reader_students)
# print('students', stud)

# students = [(id, name) for id, name in reader_students]
# classes = [(id, class_name) for id, class_name in reader_classes]
# taken = [[student_id, class_id] for student_id, class_id, year in reader_classes_taken]

# ### HOW MANY CLASSES EACH STUDENT TOOK?
# arr = []
# for sid, name in students:
#     taken_classes = []
#     all_classes = set([id for id, name in classes])
#     for student_id, class_id in taken:
#         if sid == student_id:
#             taken_classes.append(class_id) 
#     print(name, len(taken_classes))
#     print(name, taken_classes)
#     non_taken_classes = all_classes - set(taken_classes)
#     print(name, non_taken_classes)
#     print(name, [classes[int(id)][1] for id in non_taken_classes])


# print()
# ### FOR EACH CLASS HOW MANY STUDENTS TAKEN? 
# arr = []
# for id, class_name in classes:
#     count = 0
#     for student_id, class_id in taken:
#         if class_id == id:
#             count += 1
#     print(class_name, count)
#     #arr.append((clas_name, count))
# ## open("classes_taken.txt").write("\n".join(arr))


# print()
# ### FOR EACH STUDENT WHICH CLASSES DIDNT TAKE?
# for sid, name in students:
#     all_classes = set([id for id, name in classes])
#     #taken_classes = set()
#     for student_id, class_id in taken:
#         if sid == student_id:
#             all_classes.remove(class_id)
#         #taken_classes.add(class_id)
#     print(name, [classes[int(i)][1] for i in all_classes])
#     #print(name, all_classes - taken_classes)



# import csv
# trans = list(csv.reader(open("transactions.txt")))
# valuta = 'usd,kzt,euro,rubl'.split(',')
# x = 0
# for cur in valuta:
#     count = 0
#     balance = 0
#     for val, amount, cost in trans:
#         if cur == val:
#             count += 1
#             balance += int(amount)
#     print(f"{cur}:, count={count}, balance={balance}")



# # get max value index
# def get_max_index(arr):
#     min_index = 0
#     for i, val in enumerate(arr):
#         if abs(int(arr[min_index][2])) < abs(int(val[2])):
#             min_index = i
#     return min_index


# som = 10000
# for i, (val, amount, cost) in enumerate(trans):
#     if x < abs(int(cost)):
#         x = abs(int(cost))
#         id = i
#     som += int(cost)

# som = 10000

# max_index = get_max_index(trans)
# print('get_max_index:', trans[max_index])
# print('som', som)
# print('max transaction:', trans[id])



### 1. avg time per student
### 2. who was late in certain date
### 3. how many times student was late (per student)
### 4. how many times the student missed the classes? 


# import csv
# timetable = list(csv.reader(open("timetable.txt")))
# students = set([name for name, x, y in timetable]) or set(['emil'])
# dates = set([date for name, date, time in timetable])


# def avg_time(arr):
#     if len(arr):
#         s = 0
#         for hour, minute in arr:
#             s+= hour * 60 + minute
#         avg = s / len(arr)
#         return f'{int(avg / 60)}:{int(avg % 60)}'


# def late_count(arr, time):
#     count = 0
#     if len(arr):
#         hour, minute = time.split(':')
#         threshold = int(hour) * 60 + int(minute)
#         for hour, minute in arr:
#             t = hour * 60 + minute
#             if t > threshold:
#                 count += 1
#         return count

# def who_was_late(arr, time, input_date):
#     late_students = []
#     hour, minute = time.split(':')
#     threshold = int(hour) * 60 + int(minute)
#     for name, date, time in arr:
#         hour, minute = time.split(':')
#         t = int(hour) * 60 + int(minute)
#         if input_date == date and t > threshold:
#             print(name, date, time)


# def filter_table(arr, student_name):
#     sub_arr = []
#     attended_dates = set()

#     for name, date, time in arr:
#         if name == student_name:
#             hour, minute = time.split(':')
#             sub_arr.append((int(hour), int(minute)))
#             attended_dates.add(date)
#     print(student_name, 'missed dates', dates - attended_dates)
#     print(student_name, 'avg time', avg_time(sub_arr))
#     print(student_name, 'was late', late_count(sub_arr, '10:00'))

# for student_name in students:
#     filter_table(timetable, student_name)

# print('LATE STUDENTS')
# who_was_late(timetable, '10:05', '2023-10-10')


# ### sales.txt, calculate profit for certain day
# ### no dictionary

# import csv
# items = list(csv.reader(open("sales.txt")))

# purchased_items = []
# for date, name, quantity, price in items:
#     if int(quantity) > 0:
#         purchased_items.append((name, price))

# def get_price(purchased_items, name):
#     for item_name, item_price in purchased_items:
#         if name == item_name:
#             return int(item_price)
# input_date = input('insert the date:')    
# viruchka = 0
# for date, name, quantity, sale_price in items:
#     if int(quantity) < 0 and date == input_date:
#         purchase_price = get_price(purchased_items, name)
#         print(quantity, purchase_price, int(sale_price))
#         viruchka +=(purchase_price - int(sale_price)) * int(quantity)
# print("Viruchka : ", viruchka)



### sales.txt, calculate profit for certain day
### no dictionary

# import csv
# items = list(csv.reader(open("sales.txt")))
# d = {name:int(price) for d, name, q, price in items if int(q) > 0}
# res = [(d[n] - int(p)) * int(q) for dt, n, q, p in items if int(q) < 0 and dt == '2.10.23']
# print("Viruchka : ", sum(res))


# from random import randint

# x = '9999999999999999999999999999999999999'
# x += x
# x += x
# t = ''.join([x + str(randint(0,9)) for i in range(100000)])
# s = '6666' + x + '9999'
# t += s

# from time import time

# print(len(t), len(s))
# tic = time()
# for i in range(len(t)):
#     if s == t[i:i+len(s)]:
#         print(i)
# toc = time()
# print(toc - tic)


### OBMENKA

# import csv
# d = {}
# lines = csv.reader(open("obmenka.txt", "r"))

# for curr, quan, price in lines:
#     if curr not in d:
#         d[curr] = []
#     d[curr].append((int(quan), float(price)))

# print(d)


# for curr in d:
#     arr = d[curr]
#     quantity_buy = sum([a for a, b in arr if a > 0])
#     quantity_sell = sum([a for a, b in arr if a < 0])
#     buy_cost = sum([a*b for a, b in arr if a > 0])
#     sell_cost = sum([a*b for a, b in arr if a < 0])
#     avg_b = buy_cost/quantity_buy
#     avg_s = sell_cost/ quantity_sell
#     print(curr, avg_b, avg_s, quantity_sell*(avg_b-avg_s), quantity_buy, quantity_sell)

# def func1(arr):
#     for i in arr:
#         if 40 - i in arr:
#             return True

# def func2(arr):
#     d = {}
#     for i in arr:
#         if 40 - i in d:
#             return True
#         d[i] = True
    
# from time import time
# from random import randint
# arr = [randint(0,10) for i in range(10**6)]
# arr = arr + [20,20]

# tic = time()
# #a = func1(arr)
# a = func2(arr)
# toc = time()
# print(toc - tic)

### EXAM 10/30/23

# from collections import defaultdict
# import csv
# d = defaultdict(list)
# student = {}
# lines = csv.reader(open("student_list_27.txt", 'r'))
# class_reader = list(csv.reader(open("class_list_28.txt", 'r')))
# class_name = {cl_id:cl_name for cl_id, cl_name, credits in class_reader}
# class_credits = {cl_id: int(credits) for cl_id, cl_name, credits in class_reader}
# for st_id, st_name, year, semester, cl_id in lines:
#     d[st_id].append((year, cl_id))
#     student[st_id] = st_name


# medians = []
# ## avg per student
# for st_id, arr in d.items():
#     credits = [class_credits[cl_id] for year, cl_id in arr]
#     print(student[st_id], 'average', sum(credits) / len(credits))
#     print(student[st_id], 'missing credits', 240 - sum(credits))
#     taken_classes = defaultdict(int)
#     for year, cl_id in arr:
#         taken_classes[year] += class_credits[cl_id]
#     print(student[st_id], 'min', min(taken_classes.values()))
#     print(student[st_id], 'max', max(taken_classes.values()))
#     medians.append(median(credits))

# given_student_id = input('insert student_id : ')
# taken_classes = [class_name[cl_id] for year, cl_id in d[given_student_id]]
# print(student[given_student_id], 'take classes', taken_classes)

# print('median of median credits', median(medians))


# from random import randint


# def my_random():
#     x1 = randint(0,9)
#     x2 = randint(0,9)
#     x = x1 * 10 + x2
#     d = x // 7
#     y = d * 7

#     cnt = 1
#     while x > y:
#         cnt, x = my_random()
#         cnt += 1
#     return cnt, d

# mx = 0
# for i in range(1000000):
#     mx = max(mx, my_random())

# print(mx)


# class my_set():
#     def __init__(self, arr):
#         self.data = []
#         for i in arr:
#             self.my_add(i)
    
#     def my_add(self, i):
#         if i not in self.data:
#             self.data.append(i)
#             self.my_sort()
    
#     def show(self):
#         print(self.data)
    
#     def compare(self, obj, n=-1):
#         return self.data[:n] == obj.data[:n]

#     def my_sort(self):
#         self.data = sorted(self.data)
    
#     def show_cubes(self):
#         for i in self.data:
#             print(i**3, end=',')
#         print()
    
# s = my_set([3,3,3,3,3,1,2])
# s.show()
# s.my_add(5)
# s.show()

# s.my_add(2)
# s.show()

# s.show_cubes()

# print(len(s))

# class Unit():
#     def __init__(self, input):
#         self.value = input
#         self.left = None
#         self.right = None


# arr = [7, 11, 2, 3, 8, 18, 13, 21, 4, 32, 31, 45]

# root = Unit(7)
# root.right = Unit(11)
# root.left = Unit(2)
# root.left.right = Unit(3)
# root.right.left = Unit(8)
# root.right.right = Unit(18)
# root.right.right.left = Unit(13)
# root.right.right.right = Unit(21)
# root.left.right.right = Unit(4)
# root.right.right.right.right = Unit(32)
# root.right.right.right.right.left = Unit(31)
# root.right.right.right.right.right = Unit(45)


# def bek(root):
#     if not root:
#         return
#     bek(root.left)
#     print(root.value, end = ', ')
#     bek(root.right)


# def nus(curr_unit, input):
#     if not curr_unit:
#         return Unit(input)
    
#     if curr_unit.value > input:
#         curr_unit.left = nus(curr_unit.left, input)
#     else:
#         curr_unit.right = nus(curr_unit.right, input)

#     return curr_unit
    
# root = None
# for i in arr:
#     root = nus(root, i)


# bek(root)



# result = defaultdict(list)
# def groups(graph, source, group_id):
#     visited = set()
#     for destination in graph[source]:
#         if destination not in visited:
#             visited.add(destination)
#             result[group_id].append(destination)
#             groups(graph, destination, group_id)

# cnt = 0
# for src in graph:
#     groups(graph, src, cnt)
#     cnt += 1
            

# from time import time

# class Group():
    
#     def __init__(self, name, description = ""):
#         if len(name) > 0:
#             self.name = name
#         else:
#             self.name = "HEEEEEEEET"
#         self.members = []
#         self.admins = []
#         self.created_time = time()
#         self.description = description

#     def get_name(self):
#         return self.name.upper()
    
#     def set_name(self, name):
#         if len(name) > 0:
#             self.name = name
    
#     def get_description(self):
#         return self.description 
    
#     def set_description(self, description):
#         self.description = description

#     def remove(self, user):
#         self.members.remove(user)
    
#     def add(self, user):
#         self.members.append(user)

#     def add_admin(self, user):
#         if user in self.members and user not in self.admins:
#             self.admins.append(user)
    
#     def remove_admin(self, user):
#         if user in self.admins:
#             self.admins.remove(user)
    
#     def show_info(self):
#         print("******", self.name.upper(), "*****")
#         print("members", self.members)
#         print("admins", self.admins)
#         print()

#     def __len__(self):
#         return len(self.name)
    
#     def len(self):
#         return len(self.name)

# arr = ["Inter", "Real Madrid", "Barcelona", "Arsenal", "Dordoi", "Semetey", ""]

# groups = {}

# for name in arr:
#     groups[name] = Group(name)

# groups['Real Madrid'].add("Ronaldo")
# groups['Barcelona'].add('Messi')
# groups['Dordoi'].add("Baymatov")
# groups['Arsenal'].add("arshavin")


# for name in groups:
#     groups[name].show_info()

# group = Group("Emil")
# group.show_info()
# print(len(group))
# print(group.len())


### FEQUENCY PLOT
# from math import log2
# from random import randint
# from collections import defaultdict

# salaries = []
# for j in range(50):
#     count = randint(0, 100000)
#     avg = randint(0, 10000)
#     salaries += [randint(avg, avg+200) for i in range(count)]


# d = defaultdict(int)
# for i in salaries:
#     d[i//200] += 1

# frequencies = sorted(d.items())
# for k, v in frequencies:
#     print('%05d'%((k+1)*200), "*"*int(log2(v)+1))
from time import time, strftime
class Client:
    def __init__(self, name, telnumber, amount):
        self.balance = amount
        self.name = name
        self.telnumber = telnumber
        self.data = []
    
    def deduct(self, date, amount):
        self.balance -= amount
        self.data.append([date, amount])
    
    def show_balance(self):
        print("*"*30)
        print(f"Client={self.name}'s balance")
        print(self.balance)
        print("*"*30)

    def show_payments(self):
        print("*"*20)
        print(f"Client={self.name} payments history")
        for i in self.data:
            print(i)
        print("*"*20)
        
    def show_payments_between_interval(self, start, end):
        print(f"Client = {self.name}'s payments for the period of {start} and {end}")
        for date, amount in self.data:
            if start <= date <= end:
                print(date, amount)





bank = {}
bank['bek'] = Client("Bekbolsun", "0555757555", 10000)
bank['saadat'] = Client('Saadat', "0777555577", 3000)
bank['bek'].deduct('2023-09-01', 2000)
bank['bek'].deduct('2023-09-05', 1000)
bank['saadat'].deduct('2023-10-01', 100)

bank['bek'].show_balance()
bank['bek'].show_payments()
bank['bek'].show_payments_between_interval('2023-09-03', '2023-09-15')

bank['akbar'] = Client("Akbar", "0777898933", 5000)
bank['saadat'].deduct("2023-10-01", 2000)
bank['saadat'].show_balance()


from time import time

items = {}
def get_item(barcode):
    if barcode in items:
        return items[barcode]

class Item:
    def __init__(self, barcode, name, expiration_date, sell_cost):
        self.barcode = barcode
        self.name = name
        self.expiration_date = expiration_date
        self.sell_cost = sell_cost

    def get_barcode(self):
        return self.barcode

    def get_name(self):
        return self.name
    

class Basket:
    def __init__(self):
        self.items = {}
        self.time = time()
        self.cost = 0
        self.quantity = 0
        self.item_quantity = {}
    
    def add(self, barcode, quantity=1):
        self.item_quantity[barcode] += quantity
        self.quantity += quantity
        self.cost += get_item(barcode).cost * quantity
    
    def remove(self, barcode, quantity=1):
        if barcode in self.item_quantity:
            if self.item_quantity[barcode] == quantity:
                del self.item_quantity[barcode]
                self.cost -= get_item(barcode).cost * quantity

            elif self.item_quantity[barcode] > quantity:
                self.item_quantity[barcode] -= quantity
                self.cost -= get_item(barcode).cost * quantity
    
    def print_check(self):
        print("*"*10, "CHECK", "*"*10)
        for barcode, quantity in self.item_quantity.item():
            print(barcode, get_item(barcode).get_name(), quantity)
        print("Total quantity:", self.quantity)
        print("Total cost:", self.cost)




    


    
