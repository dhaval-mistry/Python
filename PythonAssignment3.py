# check given string is palindrome or not
def is_string_palindrome(str):
    revStr = ""
    l = len(str)
    l = l-1
    while(l >= 0):
        revStr += str[l]
        l -= 1
    if(revStr == str):
        return True
    else:
        return False
    
#print(is_string_palindrome("dhaval"))

#Givenalistofintegerscomputetheaverageofallnumbersinthelist

def calculate_avg_of_list(list):
    l = len(list)
    print(l)
    tot = 0
    for n in list:
        tot += n
    return tot/l

#print(calculate_avg_of_list([1,2,3]))

# input two list and merge into one, sort the list 

def merge_list_sort_it(list1, list2):
    mergeList = list1 + list2 
    print(mergeList)
    mergeList.sort()
    return mergeList

#print(merge_list_sort_it([1,2,7],[2,4,5]))

#Given tuples, create
# a tuple of all even number
# a tuple of all odd number
def create_even_odd_tuple(tupList):
    eveTup = ()
    oddTup = ()
    for val in tupList:
        if val % 2 == 0:
            eveTup = eveTup + (val,)
        else:
            oddTup = oddTup + (val,)
    print(eveTup)
    print(oddTup)

#create_even_odd_tuple((1,2,3,4,5,6))

# given list of words, create dictionary that maps each word to its length

def cal_length_list_val(list):
    disc1 = {}
    for a in list:
        disc1[a] = len(a)
    print(disc1)

#cal_length_list_val(["apple","banana","kiwi","cherry","mango"])

def check_sets_has_common(set1, set2):
    if not set1.intersection(set2) :
        print("share no common elements")
    else:
        print("share common elements")

#check_sets_has_common({1,2,3,4,5},{4,6,7,8})

#given list, print all element that appear more than once in the list. hint use sets

def print_duplicate(list):
    dupSet = set()
    for val in list:
        if val in dupSet:
            print(val)
        else:
            dupSet.add(val)
    print(dupSet)

#print_duplicate([1,2,3,4,5,6,7,8,9,1,2,3])

# ask the user for string and print: all unique characters, the count of uniqe characters 
def print_unique_char(str):
    strSet = set()
    for s in str:
        strSet.add(s)
    print(len(strSet))
    print(strSet)

#print_unique_char("This is test string")

#

def student_disctionary():
    ext = ""
    stdList = {}
    while(ext != 'E'):
        print("A - Add a student")
        print("B - Update marks")
        print("C - Search for a student")
        print("D - Display all student and marks")
        print("E - Exit")

        ext = input("Select Your choice: ")

        if ext == "A":
            stdName = input("Student Name: ")
            stdMarks = input("Student Marks: ")
            stdList[stdName] = stdMarks
        elif ext == "B":
            stdName = input("Update Student Name: ")
            stdMarks = input("Update Marks: ")
            stdList[stdName] = stdMarks
        elif ext == "C":
            stdName = input("Find Student Name: ")
            print(stdList[stdName])
        elif ext == "D":
            print("Student Name   \tMarks")
            for key, value in stdList.items():
                print(key +"   \t" +  value)

#student_disctionary()