import os
# Open file name.txt in write mode
# write 5 name open per line entered by the user
# Then open the same file in read mode and print all names

def read_write_file(num):
    f = open("name.txt","w")
    for cnt in range(num):
        nm = input(f"Please enter {cnt+1} name:")
        f.writelines(nm + "\n")

    f.close()

    f1 = open("name.txt","r")
    content = f1.read()
    print(content)
    f1.close()


#read_write_file(5)

# Opens a file "log.txt" in append mode 
# Adds a new log every ( like "Program run successfully")
# Opens the file in read mode and prints all logs 

def add_log_to_logfile(log):
    f = None
    if not os.path.isfile("log.txt"):
        f = open("log.txt", "x+")
    else:
        f = open("log.txt", "a+")
    
    f.writelines(log + "\n")

    f.seek(0)
    content = f.read()
    print(content)

#add_log_to_logfile("Program run successfully!")

# Create a program that:
#   has list of humbers [5,10,15,20,25]
#   uses a list comprehension to create a new list with only numbers greater than 15
#   Prints the new list

def create_list_greater_number(num):
    l1 = [5,10,15,20,25]
    
    # list comprehension for numbers greater than 15
    l2 = [n for n in l1 if n> 15]
    #    assignment value       ittration        condition (optional)
    
    print(l2)

# create_list_greater_number(15)

# Create a python dictionary of 3 cities and their populations. Save it to cities.json
# then load the JSON and print each city and its population.
# Ask the user for a new city & its population - update this info in the JSON file.

import json
def city_population_file():
    cityDic = {
        "AAA":  "100000",
        "BBB":  "200000",
        "CCC":  "300000"
    }
    jCities = json.dumps(cityDic)

    with open("cities.json", "w") as f:
        json.dump(cityDic,f,indent=4)

    city = input("Enter city name:")
    pop = input("Enter Population:")
    cityDic[city] = pop

    with open("cities.json", "w") as f:
        json.dump(cityDic,f,indent=4)

#city_population_file()

# write a program that tries to open "data.txt" in read mode. If the file does not exist, catch the exception and print "file not found!".
# 

def file_not_found():
    try:
        with open("data.txt", "r") as f:
            context = f.read()
    except FileNotFoundError:   
        print("File not found!")
    finally:
        print("In finally block")

#file_not_found()

