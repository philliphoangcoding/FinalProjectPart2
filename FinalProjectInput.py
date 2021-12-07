# Name: Phillip Hoang PSID: 1877593

# importing csv and other stuff that I need to get the code working
# i think i was supposed to do this with classes but i couldn't
import csv
from operator import itemgetter
from datetime import date

#------------------ part a ------------------

# making some empty lists to save all the information from the csv files
manu_list = []
price_list = []
date_list = []
# opening each csv file and appending them to the empty lists
with open("ManufacturerList.csv") as manulist:
    manu_reader = csv.reader(manulist)
    for x in manu_reader:
        manu_list.append(x)
with open("PriceList.csv") as pricelist:
    price_reader = csv.reader(pricelist)
    for x in price_reader:
        price_list.append(x)
with open("ServiceDatesList.csv") as datelist:
    service_reader = csv.reader(datelist)
    for x in service_reader:
        date_list.append(x)
# sorting each list by ID and saving the list as the sorted list
manu_list = (sorted(manu_list, key=itemgetter(0)))
price_list = (sorted(price_list, key=itemgetter(0)))
date_list = (sorted(date_list, key=itemgetter(0)))
# creating the final list
final_list = manu_list
# putting all the lists together
for x in range(0, len(final_list)):
    manu_list[x].append(price_list[x][1])
for x in range(0, len(final_list)):
    manu_list[x].append(date_list[x][1])
# appending a copy of the damaged part to the end of the list
for x in range(0, len(final_list)):
    manu_list[x].append(final_list[x][3])
# removing the first damaged part of the list
for x in range(0, len(final_list)):
    manu_list[x].pop(3)
full_inventory = (sorted(final_list, key=itemgetter(0)))
#making a seperated list for the sorted full_inventory
def Extract1(lst):
    return [item[0] for item in lst]
def Extract2(lst):
    return [item[1] for item in lst]
def Extract3(lst):
    return [item[2] for item in lst]
def Extract4(lst):
    return [item[3] for item in lst]
id_list = Extract1(full_inventory)
manufacturer_list = Extract2(full_inventory)
type_list = Extract3(full_inventory)
cost_list = Extract4(full_inventory)
#------------------ part b ------------------
while True:
    #prompt the user for the query
    user = input("Type a query or q to quit: ")
    #if the user enters q exit the program
    if(user == "q"):
        break
    user = user.split()
    manu = ""
    type = ""
    for word in user:
        #iterate over manu list
        for i in manufacturer_list:
            if str(i).lower() == str(word).lower():
                #assign the manufacturer to item
                manu = i
        #iterate over type list
        for i in type_list:
            if str(i).lower() == str(word).lower():
                #assign the type
                type = i
    #if either item or type is empty print it
    if(manu == "" or type == ""):
        print("No such item in inventory")
    else:
        #initialize the list to store the values
        temp_list_final = []
        #iterate over amount of data we have
        for i in range(len(id_list)):
            #check the data of manufacturer and type in the data
            if(manufacturer_list[i] == manu and type_list[i] == type):
                temp_list = []
                temp_list.append(cost_list[i])
                temp_list.append(id_list[i])
                temp_list.append(manufacturer_list[i])
                temp_list.append(type_list[i])
                temp_list_final.append(temp_list)
        #sort the list
        output = (sorted( temp_list_final,key=itemgetter(0),reverse=True))
        print("Your item is " + str(output[0][1]) + " " + str(output[0][2]) + " " + str(output[0][3]) + " " + str(output[0][0]))
        #create a list to store the recommended items
        extra = ["", "", "", 0]
        #iterate over the amount of data we have
        for i in range(len(id_list)):
            #check all the items of same type and different manufacturer
            if(type_list[i] == type and manufacturer_list[i] != manu):
                extra[0] = id_list[i]
                extra[1] = manufacturer_list[i]
                extra[2] = type_list[i]
                extra[3] = cost_list[i]
                print("You may also like " + str(extra[0]) + " " + str(extra[1]) + " " + str(extra[2]) + " " + str(extra[3]))