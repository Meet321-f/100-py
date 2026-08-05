
'''
What is CSV ?
CSV = Comma Separated Values

name , age , city
meet , 25 , delhi
vansh , 21 , mumbai
krish , 20, gujarat

CSV mean Each values separated by comma.


'''

import csv

# data = [
#     ["Name", "Age", "City"],
#     ["writerows", 35, "Delhi"],
#     ["Rohit", 22, "Mumbai"],
#     ["Hardik", 31, "Surat"]
# ]

# # if we wont to write onlt one row then we use writerow().
# # if we wint to add mutiple rows in one time thet we use writerows().

# with open("s.csv" , "w" , newline="") as f:
#     write = csv.writer(f)

#     write.writerows(data)

# print("CSV file created successfully")    



# with open("s.csv" , "r" ) as f:
#     reader  = csv.reader(f)

#     for row in reader:
#         print(row)
#         print(type(row[1]))

# print only name from the csv file 
# with open("s.csv" , "r") as f:
#     reader = csv.reader(f)
#     next(reader) # Skip the header row

#     for row in reader:
#         print(row[0])

# # print names and ages
# with open("s.csv" , "r") as f:
#    reader = csv.reader(f)
#    next(reader)

#    for row in reader:
#     print(row[0], "is", row[1] , "years old")


# Diskreader 
# with open("s.csv" , "r") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         # print(row)        # print all the data in dictionary format
#         # print(row["Name"])  # if we wont to print onky name 
#         # print(row["Name"] , "Live in ", row["City"])

#        print(row["Name"], row["Age"], row["City"]) # print all the data in one line

# DictWriter()
with open("s.csv" , "w" , newline="") as f:
    fields = ["Name", "Age", "City"]
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()  # write the header row

    writer.writerow({
        "Name": "Virat",
        "Age": 35,
        "City": "Delhi"
    })

    writer.writerow({
        "Name": "Dhoni",
        "Age": 30,
        "City": "Ranchi"
    })

    writer.writerow({
        "Name": "Gill",
        "Age": 30,
        "City": "Fazilka"
    })








        

    


