
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

    return s / i # s / len(i)



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

 
def max2(arr):
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

# print(arr)
# d = max_distance(arr)
# print()
# print(d)
# print()
# print(max_value_v3(d))

def min_value3(arr):
    min = arr[0]
    for x in arr:
        if x > min:
            min = x
    return min


def max3(arr):
    max = arr[0]

    for i in arr:
        if i[0] >= max[0] and i[1] >= max[1] and i[2] > max[2]:
            max = i
    return max


arr = [[2005, 10, 10], [2005, 10, 9], [2005, 3, 18],
       [2005, 12, 29], [2003, 1, 19], [2006, 7, 13]]

# print(min_value3(arr))
# print(max3(arr))
# print(max(arr))


def has_word(s, x):
    for i in range(len(s)):
        if x == s[i:i+len(x)]:
            return True
    return False


s = "emilbek bilgazyev"
x = "sbek"
#print(has_word(s, x))

# print(s.upper())
# print(s.split(' '))

s = '''
Հայերեն Shqip ‫العربية Български Català 中文简体 Hrvatski Česky Dansk Nederlands English Eesti Filipino Suomi Français ქართული Deutsch Ελληνικά ‫עברית हिन्दी Magyar Indonesia Italiano Latviski Lietuviškai македонски Melayu Norsk Polski Português Româna Pyccкий Српски Slovenčina Slovenščina Español Svenska ไทย Türkçe Українська Tiếng Việt
Lorem Ipsum
"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
"There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."

AD
What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.

Where can I get some?
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.

5
	paragraphs
	words
	bytes
	lists
	Start with 'Lorem
ipsum dolor sit amet...'

Translations: Can you help translate this site into a foreign language ? Please email us with details if you can help.
There is a set of mock banners available here in three colours and in a range of standard banner sizes:
BannersBannersBanners
Donate: If you use this site regularly and would like to help keep the site on the Internet, please consider donating a small sum to help pay for the hosting and bandwidth bill. There is no minimum donation, any sum is appreciated - click here to donate using PayPal. Thank you for your support.
Donate Bitcoin: 16UQLq1HZ3CNwhvgrarV6pMoA2CDjb4tyF
NodeJS Python Interface GTK Lipsum Rails .NET Groovy
The standard Lorem Ipsum passage, used since the 1500s
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

1914 translation by H. Rackham
"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"

Section 1.10.33 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

1914 translation by H. 
"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."

help@lipsum.com
Privacy Policy · Do Not Sell My Personal Information · Change Consent

AD'''

# print(has_word(s, 'emil'))
# print(len(s))
words = s.split()

# print(words)
# print(len(words))
# print('sails' in words)

def get_word_lengths(words):
    arr = []
    for i in words:
        length = len(i)
        arr.append(len(i))
    return arr

def count_words(arr, d):
    count = 0
    for i in arr:
        if i == d:
            count += 1
    return count

arr = get_word_lengths(words)
#print(arr)
s = []
for x in set(arr):
    s.append([x, count_words(arr, x)])



def get_max4(arr):
    max = arr[0]
    for i in arr:
        if i[1] > max[1]:
            max = i
    return max

    
# print(s)
# print(get_max4(s)) 

def my_split(s, sep):
    x = ''
    for c in s:
        if c != sep:
            x += c
        else:
            print(x)
            x = ''
    print('last', x)

s = 'ab,cd,ef,gh,'
# my_split(s, ',')


from random import randint

def experiment(N):
    arr = [0]*13
    varr = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    for i in range(N):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        d = d1 + d2
        arr[d] += 1

    for k, (i, j) in enumerate(zip(arr, varr)):
        print(k, i/N - j/36, i, i)



# for N in [10, 100, 1000, 10000, 1000000, 10000000]:
#     print("*****", N, "******")
#     experiment(N)

s = "a, b, cd, efg, abkg, abcdef"
# print(s.split())
# print(max(s.split(), key = lambda i:len(i)))


# arr = (1, 2)
# arr[0] = 2
# print(arr)



# #print(min_value([1,2,3,4]))
# # arr = list(range(10))
# # print(arr)
# # print(arr[:5:-1])
# # print(arr[5:2:-3])
# # print(arr[::2])
# # print(arr[::-2])


# # arr = [1, 2, 3]
# # arr.append(1, 5)
# # print(arr)


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


from random import randint

#print([randint(1, 18) for i in range(3)])


def f(arr):
    x = 0
    for diana in arr:
        if diana < x:
            x = diana
    return x

arr = [1,2,3,2]
#print('result:', f(arr))


# s = "emil bilgazyev"
# s[3], s[1] = s[2], s[5]
#print(s)


def f2(arr):
    x = 1
    for user, index in enumerate(arr):
        if user == x:
            print(index)

arr = [1,2,3,2,1,5,6,2]
#f2(arr)

def f3(arr):
    max = 0
    for index in arr:
        if len(index) < max:
            max = len(index)
    return max

arr = ['abc', 'bc', 'd', 'ab']
#print(f3(arr))

arr1 = [1,2,3,1,2]
arr2 = [1,2,2]

def f4(arr1, arr2):
    result = []
    for val1, i in enumerate(arr1):
        for val2, j in enumerate(arr2):
            if i == j:
                result = [val1, val2]
    return result

#print(f4(arr1, arr2))


arr1 = [1,2,3,3,4]
arr2 = [2,3,5,5,5]


#print((set(arr2) - set(arr1)))
#print(arr2(2))
#print( (set(arr1) & set(arr2(2))) | (set(arr2) - set(arr1)) )

# def f():
    # return 1

# x = input('val1: ')
# y = input('val2: ')
# print('result:', max(x, y))

x = [1,2,3,4,5,6]
y = [0,0,0,0,0]

x[0], y[1] = x[2], y[0]
#print(x)

arr = [1,2,3,4,5,2,1,6,2]
#print('before', arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

#print('after', arr)

arr1 = list(range(1,19))
from random import shuffle

arr2 = list(range(1,19))
shuffle(arr2)
#print(list(zip(arr1,arr2)))

from random import randint

val1 = randint(0,10)
val2 = randint(0,10)

# s1 = "{} plus {} equals {}".format(val1, val2, val1+val2)
# s2 = f"{val1} plus {val2} equals {val1+val2}"
# print(s1)
# print(s2)


# fb = open("secondfile.txt", "w")

# for i in range(100):
#     val1 = randint(0,10)
#     val2 = randint(0,10)
#     s2 = f"{val1}+{val2}=\n"
#     fb.write(s2)

# fb.close()


# fb = open("C:/Users/bekem/Downloads/testfile.xyz", "r")
# for x in fb:
#     print(x)
# fb.close()



# fb = open("file2.py", "r")
# fnew = open('fil2_new.py', "w")

# for x in fb:
#     x = x.replace("arr", "massive")
#     fnew.write(x)



code = """
from random import randint
def calc():
    a = int(input("Input first value:"))
    b = int(input("Input second value:"))
    x = a + b
    s = f'{a} + {b} = '
    result = int(input(s))
    if result == x:
       print("Pravilno")
    else:
       print("HEEEEEEET")

while True: `
  calc()
"""

# fb = open('C:/Users/bekem/Downloads/aziz.py', 'w')
# fb.write(code)
# fb.close()


def maxValue(arr):
    mx = arr[0]
    for i in arr:
        if i > mx:
            mx = i
    return mx

arr = [1,2,4,2]

if maxValue(arr) == 4:
    print("Manual test correct")
else:
    print("Manual Test incorrect")


for i in range(1,4):
    fb = open(f'C:/Users/bekem/Downloads/tests/test_{i}.txt', 'r')
    line = fb.read()
    first, second = line.split('\n')
    s_arr = first.split(',')
    arr = [int(i) for i in s_arr]
    max_val = int(second)
    print(arr, max_val)
    if max_val == maxValue(arr):
        print(f"test_{i}.txt passed")
    else:
        print(f"test_{i}.txt failed!!!")

