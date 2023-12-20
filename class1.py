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


# arr = [1, 2, 3, 5, 5, 5, 6, 7]
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



### BANK CLIENT
# from time import time, strftime
# class Client:
#     def __init__(self, name, telnumber, amount):
#         self.balance = amount
#         self.name = name
#         self.telnumber = telnumber
#         self.data = []
    
#     def deduct(self, date, amount):
#         self.balance -= amount
#         self.data.append([date, amount])
    
#     def show_balance(self):
#         print("*"*30)
#         print(f"Client={self.name}'s balance")
#         print(self.balance)
#         print("*"*30)

#     def show_payments(self):
#         print("*"*20)
#         print(f"Client={self.name} payments history")
#         for i in self.data:
#             print(i)
#         print("*"*20)
        
#     def show_payments_between_interval(self, start, end):
#         print(f"Client = {self.name}'s payments for the period of {start} and {end}")
#         for date, amount in self.data:
#             if start <= date <= end:
#                 print(date, amount)





# bank = {}
# bank['bek'] = Client("Bekbolsun", "0555757555", 10000)
# bank['saadat'] = Client('Saadat', "0777555577", 3000)
# bank['bek'].deduct('2023-09-01', 2000)
# bank['bek'].deduct('2023-09-05', 1000)
# bank['saadat'].deduct('2023-10-01', 100)

# bank['bek'].show_balance()
# bank['bek'].show_payments()
# bank['bek'].show_payments_between_interval('2023-09-03', '2023-09-15')

# bank['akbar'] = Client("Akbar", "0777898933", 5000)
# bank['saadat'].deduct("2023-10-01", 2000)
# bank['saadat'].show_balance()



# ### SHOP
# from time import time

# items = {}
# def get_item(barcode):
#     if barcode in items:
#         return items[barcode]

# class Item:
#     def __init__(self, barcode, name, expiration_date, sell_cost):
#         self.barcode = barcode
#         self.name = name
#         self.expiration_date = expiration_date
#         self.sell_cost = sell_cost

#     def get_barcode(self):
#         return self.barcode

#     def get_name(self):
#         return self.name
    

# class Basket:
#     def __init__(self):
#         self.items = {}
#         self.time = time()
#         self.cost = 0
#         self.quantity = 0
#         self.item_quantity = {}
    
#     def add(self, barcode, quantity=1):
#         self.item_quantity[barcode] += quantity
#         self.quantity += quantity
#         self.cost += get_item(barcode).cost * quantity
    
#     def remove(self, barcode, quantity=1):
#         if barcode in self.item_quantity:
#             if self.item_quantity[barcode] == quantity:
#                 del self.item_quantity[barcode]
#                 self.cost -= get_item(barcode).cost * quantity

#             elif self.item_quantity[barcode] > quantity:
#                 self.item_quantity[barcode] -= quantity
#                 self.cost -= get_item(barcode).cost * quantity
    
#     def print_check(self):
#         print("*"*10, "CHECK", "*"*10)
#         for barcode, quantity in self.item_quantity.item():
#             print(barcode, get_item(barcode).get_name(), quantity)
#         print("Total quantity:", self.quantity)
#         print("Total cost:", self.cost)

# from time import time, sleep, strftime
# from datetime import datetime



# def my_sleep():
#     seconds = randint(0, 5)
#     print('Sleeping for ', seconds, 'seconds')
#     sleep(seconds)


# class Valuta:
#     def __init__(self, name, amount=0, avg_buy=0, avg_sell=0):
#         self.name = name
#         self.avg_buy = avg_buy
#         self.avg_sell = avg_sell
#         self.amount = amount
#         self.sell_amount = 0
#         self.history = []

    
#     def buy(self, amount, rate):
#         print('Buying: ', self.name, amount, rate)
#         self.avg_buy = (self.amount*self.avg_buy + amount * rate) / (self.amount + amount)
#         self.amount += amount
#         self.history.append([datetime.now(), amount, rate])
    
#     def sell(self, amount, rate):
#         print('Selling: ', self.name, amount, rate)
#         self.avg_sell = (self.sell_amount*self.avg_sell + amount * rate) / (self.sell_amount + amount)
#         self.amount -= amount
#         self.sell_amount += amount
#         self.history.append([datetime.now(), -amount, rate])

#     def show_profit(self):
#         profit = (self.avg_sell - self.avg_buy) * self.sell_amount
#         print('Profit for ',self.name, profit)
#         return profit
    
#     def show_history(self):
#         print('Showing history for', self.name)
#         for ts, amount, rate in self.history:
#             print(ts.strftime('%H:%M:%S'), amount, rate)

# from random import randint

# class Obemka:
#     def __init__(self, name):
#         self.data = {}
#         self.name = name
    
#     def buy(self, valuta, amount, rate):
#         if valuta in self.data:
#             self.data[valuta].buy(amount, rate)

    
#     def sell(self, valuta, amount, rate):
#         if valuta in self.data:
#             self.data[valuta].sell(amount, rate)
    
#     def add_valuta(self, name):
#         self.data[name] = Valuta(name)

#     def show_profit(self):
#         print()
#         total = 0
#         for name, valuta_obj in self.data.items():
#             total += valuta_obj.show_profit()
#         print('Total profit: ' , total)

#     def show_history(self):
#         print()
#         for name, obj in self.data.items():
#             obj.show_history()


# obmenka = Obemka('BEKObmen')
# obmenka.add_valuta('dollar')
# obmenka.buy('dollar', 100, 89.5)
# my_sleep()
# obmenka.buy('dollar',500, 89.6)
# my_sleep()
# obmenka.sell('dollar',100, 89.8)
# my_sleep()
# obmenka.buy('dollar',1000, 89.65)
# my_sleep()
# obmenka.sell('dollar',1500, 89.75)

# obmenka.add_valuta('euro')
# obmenka.buy('euro', 100, 100)
# my_sleep()
# obmenka.sell('euro', 50, 101)
# my_sleep()
# obmenka.add_valuta('rubl')
# obmenka.buy('rubl', 1000, .89)
# obmenka.sell('rubl', 500, .91)


# obmenka.add_valuta('kzt')
# obmenka.buy('kzt', 1000, 0.03)
# my_sleep()
# obmenka.buy('kzt', 5000, 0.04)
# my_sleep()
# obmenka.sell('kzt', 2000, 0.05)

# obmenka.show_profit()
# obmenka.show_history()

# class Glasses:
#     def aziz(self):
#         self.glass_frame = None
#         self.glass_size = None
#         self.optics = None
#         self.glass_type = None
#         self.glass_is_polorized = None
#         self.glass_country_of_origin = None
#         self.cost = None
    
#     def __init__(self):
#         self.aziz()

# class Shoe:
#     def __init__(self):
#         self.shoe_size = None
#         self.shoe_type = None
#         self.shoe_season = None
#         self.shoe_color = None
#         self.shoe_country_of_origin = None
#         self.shoe_cost = None

# class Hair:
#     def __init__(self):
#         self.hair = None
#         self.hair_length = None
#         self.hair_color = None
#         self.hair_is_painted = None
#         self.hair_last_time_trimmed = None


# class Person:
#     def __init__(self, lastname = None, name = None):
#         self.name = name
#         self.lastname = lastname
#         self.glasses = None
#         self.shoe = None
#         self.hair = None

#     def set_name(self, name):
#         self.name = name
    
#     def set_lastname(self, lastname):
#         self.lastname = lastname

#     def set_shoe_size(self, size):
#         if not self.shoe:
#             self.shoe = Shoe()
        
#         self.shoe.shoe_size = size
    
#     def set_shoe_color(self, color):
#         if not self.shoe:
#             self.shoe = Shoe()
#         self.shoe.color = color

#     def set_shoe(self, input_shoe):
#         self.shoe = input_shoe

#     def show(self):
#         print(f'First name : {self.name}\nLast name: {self.lastname}\n')
    


# krasovka = Shoe()
# krasovka.shoe_color = 'Black'
# krasovka.cost = 1500
# krasovka.shoe_size = 42



# c = Person('Saadat', 'YUZ')
# c.show()
# c.set_shoe(krasovka)


# a = Person()
# a.set_name('Saadat')
# a.set_lastname('YUZ')
# b = Person()

# a.show()
# a.set_name('Nuskaim')
# a.set_lastname('XYZ')
# a.show()


# class Class:
#     def __init__(self, id, name, credits = 3, limit = 2):
#         self.id = id
#         self.name = name
#         self.limit = limit
#         self.count = 0
#         self.credits = credits
    
# class Student:
#     def __init__(self):
#         self.info = {}
#         self.classes = {}
#         self.last = None
#         self.first = None
#         self.limit = 3
#         self.credit_limit = 18

#     def set(self, param, value):
#         self.info[param] = value

#     def add_class(self, year, enrolled_class):
#         if enrolled_class.limit > 0 and self.limit > 0 and self.credit_limit >= enrolled_class.credits:
#             self.classes[enrolled_class.id] = enrolled_class
#             self.last = enrolled_class
#             if  self.first is None:
#                 self.first = enrolled_class
#             enrolled_class.limit -= 1
#             self.limit -= 1
#             self.credit_limit -= enrolled_class.credits
#             print(f'{self.info["name"]} was successfully enrolled to {enrolled_class.name}, {enrolled_class.limit - enrolled_class.count} has left')
#         elif enrolled_class.limit == 0:
#             print(f'{enrolled_class.name} has a limit of {enrolled_class.limit}')
#         elif self.limit == 0:
#             print(f'{self.info["name"]} has reached the limit of classes')
#         elif self.credit_limit < enrolled_class.credits:
#             print(f'{self.info["name"]} cannot take {enrolled_class.name} who has {enrolled_class.credits} credits which is more than {self.credit_limit}')

#     def get_first_last_class(self):
#         return self.first, self.last

#     def remove_class(self, class_id):
#         self.classes.pop(class_id)
    
#     def print(self):
#         print(self.info)
#         print(self.classes.keys())


# x = Student()
# x.set('name', 'Bekbolsun')

# class101 = Class(101, 'Programming Language', 12)
# class201 = Class(201, 'Statistics', 6)
# class202 = Class(202, 'Operating System', 7)
# class102 = Class(102, 'Discrete mathematics', 6)

# y = Student()
# y.set('name', 'Saadat')
# z = Student()
# z.set('name', 'Aziz')

# x.add_class(2023, class101)
# x.add_class(2023, class201)
# x.add_class(2023, class202)

# y.add_class(2023, class101)

# z.add_class(2023, class201)
# z.add_class(2023, class202)
# z.add_class(2023, class102)
# z.add_class(2023, class101)


##### Probability distribution
# from random import randint
# from matplotlib import pyplot as plt
# import math

# tmp = []
# N = 200
# arr = [0]*(N+1)
# for i in range(100000):
#     s = sum([randint(0, 1) for j in range(N)])
#     tmp.append(s)
#     arr[s] += 1

# avg = sum(tmp)/len(tmp)
# var = sum([(avg - i)**2 for i in tmp])**0.5/N

# arr2 = [0]*N
# for x in range(N):
#     arr2[x] = 1/(var*(2*math.pi))*math.exp2(-1/2*((x-avg)/var)**2)


# #plt.plot(arr, color='red')
# plt.plot(arr2, color='green')
# plt.show()


### Stadium 
# from time import time
# class Ticket:
#     def __init__(self, cost) -> None:
#         self.timestamp = time
#         self.cost = cost

#     def show_info(self):
#         print(f'Ticket was sold in store for {self.cost} price')
# class User:
#     def __init__(self):
#         self.name = None
#         self.lastname = None
#         self.email = None
#         self.dateofbirth = None
#         self.phone = None

#     def show_info(self):
#         print(f'Name:{self.name}, Lastname:{self.lastname}, DOB:{self.dateofbirth}, email:{self.email}')

# class Seat:
#     def __init__(self):
#         self.material = None
#         self.color = None
#         self.type = None
    
#     def show_info(self):
#         print(f'Type:{self.type}, material:{self.material}')


# class TicketingSystem:
#     def __init__(self, timestamp):
#         self.name = None
#         self.prices = None
#         self.users = {}
#         self.seats = {}
#         self.prices = {}
#         self.data = {}
#         self.sold = 0
#         self.max_capacity = 0
#         self.eventdate = timestamp
#         self.discounts = []
    
#     def add_discounts(self, days_limit, discount):
#         self.discounts.append((days_limit, discount))

#     def add_seat(self, info, default_price = 500, quantity = 1):
#         for i in range(quantity):
#             seat_id = len(self.seats)
#             self.seats[seat_id] = info
#             self.max_capacity += 1
#             self.prices[seat_id] = default_price

#     def add_user(self, user_info):
#         self.users[len(self.users)] = user_info

#     def users_info(self):
#         for user_id, user_info in self.users.items():
#             print(user_id)
#             user_info.show_info()
#         print()

#     def get_discount(self):
#         arr = sorted(self.discounts, reversed=True)
#         for days, discount in arr:
#             if self.eventdate - time() > days*24*60*60:
#                 return discount 
#         return 0
    
#     def show_seats(self):
#         for id, info in self.seats.items():
#             if id not in self.data:
#                 print(id)
#                 info.show_info()
#                 print()
    
#     def buy_ticket_online(self, seat_id, user_id, price):
#         if seat_id not in self.data:
#             self.data[seat_id] = (user_id, price)
#             self.sold += 1
#         else:
#             print(f'Seat: {seat_id} is already sold to user {self.data[seat_id]}')
#             print()
    
#     def buy_ticket_in_store(self, seat_id, cost):
#         if seat_id not in self.data:
#             self.data[seat_id] = Ticket(cost)
#             self.sold += 1

#     def show_seat_id(self, seat_id):
#         if seat_id in self.data.items():
#             user_id = self.data[seat_id]
#             print(f'Seat: {seat_id} was sold to')
#             self.users[user_id].show_info()
#             print()



# stadion = TicketingSystem(time() + 60*60*24*20)

# stadion.add_discounts(15, 50)
# stadion.add_discounts(10, 30)
# stadion.add_discounts(5, 20)


# user1 = User()
# user1.name = 'Bek'
# user1.email = 'bek@gmail.com'

# user2 = User()
# user2.name = 'Aziz'
# user2.phone = '0555773334'

# user3 = User()
# user3.name = 'Asan'
# user3.email = 'asan@yahoo.com'

# stadion.add_user(user1)
# stadion.add_user(user2)
# stadion.add_user(user3)

# seat1 = Seat()
# seat1.type = 'Economy'

# seat2 = Seat()
# seat2.type = 'VIP'

# stadion.add_seat(seat1)
# stadion.add_seat(seat2)





# stadion.buy_ticket_in_store(0, 50)



# for i in range(5):
#     stadion.show_seats()
#     seat_id = int(input('Seat id:'))
#     stadion.users_info()
#     user_id = int(input('User id:'))
#     discount = stadion.get_discount()
#     price = stadion.prices[seat_id]
#     stadion.buy_ticket_online(seat_id, user_id, price*discount)
#     stadion.show_seat_id(seat_id)


# ### LIBRARY
# class User:
#     def __init__(self,id,name,phone):
#         self.id = id
#         self.name = name
#         self.phone = phone
#         self.firstname = name

#     def show_info(self):
#         print(f"ID:{self.id},Name:{self.name},Phone:{self.phone}")


# class Book:
#     def __init__(self, name, book_id, autor, year):
#         self.name = name
#         self.book_id = book_id
#         self.autor = autor
#         self.year = year
    
#     def show_info(self):
#         print(f"ID {self.book_id}, name: {self.name}, autor: {self.autor}, year: {self.year}")

# class library:
#     def __init__(self, name):
#         self.name = name
#         self.books = {}
#         self.users = {}
#         self.user_last_id = 0
#         self.data={}
#         self.booklog = []
        
#     def add_book(self, autor, name, year):
#         self.books[len(self.books)] = Book(name,len(self.books),autor,year)
        
#     def add_user(self, name, phone):
#         self.user_last_id += 1
#         self.users[self.user_last_id] = User(self.user_last_id, name, phone)

#     def taken_book(self,book_id,user_id):
#             if user_id not in self.data:
#                 self.data[user_id]=[]
#             self.data[user_id].append(book_id)
#             self.booklog.append(book_id)

#     def user_info(self, userid):
#         if userid in self.users:
#             self.users[userid].show_info()
#             if userid in self.data:
#                 for book in self.data[userid]:
#                     self.books[book].show_info()
#         else:
#             print('User is not in the DataBase')

#     def ShowaAvaliavility(self,BID):
#         if BID in self.booklog:
#             print(f"Book {BID} is already taken")
#         else:
#             print(f"Book {BID} is free to rent")


# class Item:
#     def __init__(self, brand, price, weight, location):
#         self.brand = brand
#         self.price = price
#         self.weight = weight
#         self.location = location
    
#     def get_location(self, location):
#         return self.location

#     def set_location(self, location):
#         self.location = location


#     def show_info(self):
#         pass

# class Car_v1(Item):
#     def set_cartype(self, type):
#         self.car_type = type
    
#     def set_color(self, color):
#         self.color = color

#     def show_info(self):
#         print(self.brand, self.price, self.weight, self.location, self.car_type, self.color)


# class Car_v2(Item):
#     def __init__(self, brand, price, weight, location, type, color):
#         super().__init__(brand, price, weight, location)
#         self.color = color
#         self.car_type = type
    
#     def show_info(self):
#         print(self.brand, self.price, self.weight, self.location, self.car_type, self.color)


# class Shampoo(Item):
#     def __init__(self, brand, price, weight, location, compound, gender):
#         super().__init__(brand, price, weight, location)
#         self.gender = gender
#         self.compound = compound

#     def show_info(self):
#         print(self.brand, self.price, self.weight, self.location, self.gender, self.compound)


# class TShirt(Item):
#     def __init__(self, brand, price, weight, location, material):
#         super().__init__(brand, price, weight, location)
#         self.material = material

#     def show_info(self):
#         print(self.brand, self.price, self.weight, self.location, self.material)


# def add_item(cart, item):
#     cart.append(item)


# def move(cart, location):
#     for item in cart:
#         item.set_location(location)


# car = Car_v2("BMW", 5000, 1500, "Bishkek", "sedan", "black")
# tshirt = TShirt("nike", 15, 0.1, "Bishkek", "cotton")
# shampoo = Shampoo("Clear", 5, 1, "Bishkek", "water", "male")
# tshirt2 = TShirt("adidas", 50, 0.1, "Bishkek", "silk")
# cart = []
# add_item(cart, car)
# add_item(cart, tshirt)
# add_item(cart, shampoo)
# add_item(cart, tshirt2)

# move(cart, "Almaty")


# tshirt2.show_info()



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit

# class AIT(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.label = QLabel("0")
#         self.edit = QLineEdit("0")

#         self.button = QPushButton("Increment")
#         self.button.clicked.connect(self.increment_label)

#         self.button2 = QPushButton("Koshup koy")
#         self.button2.clicked.connect(self.koshupkoy)

#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)
#         layout.addWidget(self.edit)
#         layout.addWidget(self.button2)

#         self.setLayout(layout)
#         self.setWindowTitle("Counter")
#         self.show()
    
#     def koshupkoy(self):
#         azirki = int(self.edit.text())
#         labeltext = int(self.label.text())
#         self.label.setText(str(azirki + labeltext))

#     def increment_label(self):
#         count = int(self.label.text())
#         count += 1
#         self.label.setText(str(count))

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     counter = AIT()
#     sys.exit(app.exec_())





# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.description = f'{name} : {price}'
#         self.english = self.translate(name, 'kyrgyz')
#         self.russian = self.translate(name, 'russian')
    
        
#     def translate(self, original, to_lang):
#         pass

#     def get_price(self):
#         return self.price

# class Shampoo(Item):
#     def __init__(self, name, price, gender):
#         super().__init__(name, price)
#         self.gender = gender

# class Skirt(Item):
#     def __init__(self, name, price, color):
#         self.name = name
#         self.price = price
#         self.color = color

# def total_cost(basket):
#     return sum([item.get_price() for item in basket])

# def add_item(basket, item):
#     basket.append(item)

# def total_count(basket):
#     return len(basket)

# basket = []
# shampoo = Shampoo("Dove", 100, "male")
# skirt = Skirt("Dior", 15000, "black")
# add_item(basket, shampoo)
# add_item(basket, skirt)


# print(total_cost(basket), total_count(basket))



# class Tripod(Item):
#     def __init__(self, name, price, length):
#         super().__init__(name, price)
#         self.length = length
    

# tripod = Tripod("Marafon", 1000, "silver")



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QFont

# from random import randint

# class AIT(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.label1 = self.create_label("label 1")
#         self.label2 = self.create_label("label 2")
#         self.equal = self.create_label('=')
#         self.operator = self.create_label("")

        
#         self.result = self.create_label('', QLineEdit) #QLineEdit("")
#         self.result.returnPressed.connect(self.check_result)
        
#         self.operation = QHBoxLayout()
#         self.operation.addWidget(self.label1)
#         self.operation.addWidget(self.operator)
#         self.operation.addWidget(self.label2)
#         self.operation.addWidget(self.equal)
#         self.operation.addWidget(self.result)


#         self.button_ok = self.create_button('OK', self.check_result)
#         self.button_retry = self.create_button('Retry', self.clear_result)
#         self.button_next = self.create_button('Next', self.generate_random_number)

#         self.buttons = QHBoxLayout()
#         self.buttons.addWidget(self.button_ok)
#         self.buttons.addWidget(self.button_retry)
#         self.buttons.addWidget(self.button_next)

#         self.layout = QVBoxLayout()
#         self.layout.addLayout(self.operation)
#         self.layout.addLayout(self.buttons)

#         self.generate_random_number()

#         self.setLayout(self.layout)
#         self.setWindowTitle("Вычеслител")
#         self.setFixedSize(QSize(750, 500))
#         self.show()

#     def create_button(self, text, func):
#         button = QPushButton(text)
#         font = QFont()
#         font.setPointSize(50)
#         button.setFont(font)
#         button.setStyleSheet('background-color: orange; border-radius: 50%')
#         button.clicked.connect(func)
#         return button

#     def create_label(self,name,type = QLabel):

#         font = QFont()
#         font.setPointSize(50)
#         label = type(name)
#         label.setFont(font)
#         return label

#     def check_result(self):
#         v1 = int(self.label1.text())
#         v2 = int(self.label2.text())
#         op = self.operator.text()
#         if op == '+':
#             result = v1 + v2
#         else:
#             result = v1 - v2
    
        

#         if result == int(self.result.text()):
#             self.result.setStyleSheet("background-color: green;")
#         else:
#             self.result.setStyleSheet("background-color: red;") 
 
        


#     def clear_result(self):
#         self.result.setText("")
#         self.result.setStyleSheet("background-color: white")

#     def generate_random_number(self):
#         self.result.setText("")
#         self.result.setStyleSheet("background-color : white")
#         val1 = randint(10, 99)
#         val2 = randint(10, 99)

#         op = ['+', '-'][randint(0,1)]
#         if op == '-':
#             if val1 < val2:
#                 val1, val2 = val2, val1
        
#         self.label1.setText(str(val1))
#         self.label2.setText(str(val2))
#         self.operator.setText(op)
        

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     counter = AIT()
#     sys.exit(app.exec_())

# from time import time
# import sys

# sys.setrecursionlimit(1000000)

# def fib(n, d):
#     # if n <= 1:
#     #     return n
#     if n in d:
#         return d[n]
#     #print("n=", n)
#     d[n] = fib(n-1, d) + fib(n-2, d)
#     return d[n]

# # tic = time()
# # d={0:0, 1:1}
# # print(fib(10000, d))
# # toc = time()
# # print('time = ', (toc - tic))


# arr=[11,7,8,3,6,4,2,1,0,9]
# def my_sorted(arr):
#     if len(arr)==0 or len(arr)==1:
#         return arr
#     left=[]
#     last=arr[-1]
#     central_arr=[]
#     right=[]
#     for i in arr:
#         if i>last:
#             right.append(i)
#         if i<last:
#             left.append(i)
#         if i==last:
#            central_arr.append(i)
#     return my_sorted(left)+central_arr+my_sorted(right)
# print(my_sorted(arr))


# def check_border(h, w, r, c):
#     return  0 <= r < h and 0 <= c < w

# def mark_island(arr, i, j, memory):
#     arr[i][j] = 0
#     #memory.add((i,j))
#     for r, c in [(i-1, j+0), (i+1, j+0), (i+0, j-1), (i+0, j+1)]:
#         if check_border(arr, r, c) and arr[r][c] == 1:
#             mark_island(arr, r, c, memory)

# count = 1
# memory = set()
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] == 1:
#             mark_island(arr, 0, 0, memory)
#             count += 1


# def factorization(n):
#     d={}
#     i=2
#     while n!=1:
#         if n%i==0:
#             if i not in d:
#                 d[i]=0
#             d[i]+=1
#             n=n/i
#         else:
#             i+=1
#     return d
# print(factorization(150))      

# def GCD(n1,n2):
#     d1=factorization(n1)
#     d2=factorization(n2)
#     n=1
#     keys=d1.keys()&d2.keys()
#     for key in keys:
#         for i in range(min(d1[key],d2[key])):
#             n=n*key
#     return n
# def GCD2(n1,n2):
#     if n2==0:
#         return n1
#     return GCD2(n2,n1%n2)
# a = 11111111111111111111
# b = 111111
# print(GCD2(a, b))

# # practice question 1
# balans = 100000
# monthly_payment = 8000
# interest = 22
# payoff_count = 15
# ## find how many month will I pay to payoff the debt


# # practice question 2
# balance = 100000
# interest = 22
# payoff_count = 12
# r = 22/12/100
# n = payoff_count
# monthly_payment = balance * (r*(1+r)**n) / ((1+r)**n-1)
# print(monthly_payment)



def median(arr):
    arr = sorted(arr)
    mid = len(arr) // 2    # int(len(arr)/2)
    if mid*2 == len(arr):
        return sum(arr[mid-1 : mid+1])/2
    else:
        return arr[mid]
    

# arr = [1, 6, 2, 8, 3, 1, 2, 0, 5, 6, 3, 5, 7, 9]


# def recursive_median(arr, mid):
#     n = arr[-1]
#     arr = arr[:-1]
#     left = []
#     right = []
#     .....


# def median(arr):
#     mid = len(arr) // 2
#     if mid*2 == len(arr):
#         m1 = recursive_median(arr, mid)
#         m2 = recursive_median(arr, mid+1)
#     else:
#         return recursive_median(arr, mid)


# med = sorted(arr[6])


# arr = [1, 6, 2, 8, 3, 1, 2, 0, 5, 6, 3, 5, 7]
# n = 2

# arr = [3, 2, 0, 1, 1, 2, [3], 5, 5, 6, 6, 7, 8]

# mid = 6


# left__ = [1, 1, 2, 0, [2]]  [3, [3], 5, 5, 6, 6, 7, 8]
# left = [1, 1, 2, 0]  
# n = 2
# right = [6, 8, 3, 5, 6, 3, 5, 7]
# right = [3, [3], 5, 5, 6, 6, 7, 8]

# mid = mid - (len(left) + 1) = 6 - (4 + 1) = 1

# arr = [6, 8, 3, 5, 6, 3, 5, 7]
# mid = 1
# n = 8
# left = [6, 3, 5, 6, 3, 5, 7]
# right = []

# arr = [6, 3, 5, 6, 3, 5, 7]
# mid = 1
# n = 5
# left = [3, 5, 3]
# right = [6, 6, 7]

# arr = [3, 5, 3]
# mid = 1
# n = 5
# left = [3, 3]
# right = []

# arr = [3, 3]
# mid = 1
# n = 3
# left = [3]
# right = []

## a ** b
def power(a, b):
    if b == 0:
        return 1, 0
    elif b == 1:
        return a, 0
    elif b % 2 == 1:
        x, cnt = power(a, b // 2)
        return x * x * a, 2 + cnt
    elif b % 2 == 0:
        x, cnt = power(a, b // 2)
        return x * x, 1 + cnt
    

def power2(a, b):
    cnt = 0
    res = 1
    for i in range(b):
        res *= a
        cnt += 1
    return res, cnt

N = 100000
# print(power(1, N))
# print(power2(1, N))






# 6 + 3 + 1
# 5 + 5
# 2 + 3 + 5
# 1 + 1 ... 1

def my_min(arr):
    if len(arr)>0:
        return min(arr)
    else:
        return (float('inf'), float('inf'))

arr = [ 2, 3, 5, 6, 7]
n = 10

x = []
def recur(n, arr, m):
    if n == 0:
        print(m)
        return (len(m), m)
    return my_min([recur(n - i, arr, m + [i]) for i in arr if i <= n])


#print('Result', recur(n, arr, []))


def recur_median(arr, index):
    if len(arr) < index:
        return -1
    
    p = arr[-1]
    left = []
    right = []
    for i in arr[:-1]:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    if len(left) == index:
        return p
    elif len(left) > index:
        return recur_median(left, index)
    else:
        return recur_median(right, index - len(left) - 1)


def median2(arr):
    n = len(arr)
    if n % 2 == 1:
        return recur_median(arr, n//2)
    else:
        a = recur_median(arr, n //2)
        b = recur_median(arr, n//2 - 1)
        return (a + b)/2


arr = [1, 5, 3, 2, 5, 1, 8, 8, 9, 9]
print(median(arr))
print(median2(arr))

class Student:
    def __init__(self, name, last, year, gender) -> None:
        self.name = name
        self.last = last
        self.year = year
        self.gender = gender
    
    def show(self):
        print(f'First name:{self.name}, Last name: {self.last}, Year of birth: {self.year}')
    

# students = []
# students.append(Student('Bek', 'Bolsun', 2005, 'Male'))


# #### 
# sorted_students = sorted(students, key = lambda x:x.year)
# N = 3
# ## 1
# sorted_students[-1].show()
# ## 2
# sorted_students[0].show()
# ## 7
# sorted_students[-N].show()
# ages = [s.year for s in sorted_students]
# ## 3
# print(2023 - sum(ages)/len(ages))
# ## 4
# if len(ages) % 2:
#     print(ages[len(ages)//2])
# else:
#     print(sum(ages[len(ages)//2-1:len(ages)//2+1])/2)
# ## 5
# from collections import defaultdict
# d = defaultdict(int)
# for s in students:
#     d[s.gender] += 1
# ## 6
# sorted(students, key=lambda x:len(x.name))[-1].show()


arr1 = [6, 9, 12]
arr2 = [1, 2, 3, 7, 8, 10, 11]

def merge(arr1, arr2, output=[]):
    print('compare', arr1, arr2, output)
    if not arr1:
        return output + arr2
    if not arr2:
        return output + arr1
    if arr1[0] < arr2[0]:
        return merge(arr1[1:], arr2, output+arr1[0:1])
    else:
        return merge(arr1, arr2[1:], output+arr2[0:1])
    

    

print(merge(arr1, arr2))
