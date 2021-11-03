# Name: Phillip Hoang PSID: 1877593

# importing csv and other stuff that I need to get the code working
# i think i was supposed to do this with classes but i couldn't
import csv
from operator import itemgetter
from datetime import date

#------------------ part a ------------------

#  making some empty lists to save all the information from the csv files
manu_list = []
price_list = []
date_list = []
# opening each csv file and appending them to the empty lists
with open("ManufacturerList.csv") as manulist:
    manu_reader = csv.reader(manulist)
    for line in manu_reader:
        manu_list.append(line)
with open("PriceList.csv") as pricelist:
    price_reader = csv.reader(pricelist)
    for line in price_reader:
        price_list.append(line)
with open("ServiceDatesList.csv") as datelist:
    service_reader = csv.reader(datelist)
    for line in service_reader:
        date_list.append(line)
# sorting each list alphabetically and saving the list as the sorted list
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
full_inventory = (sorted(final_list, key=itemgetter(1)))
# writing the complete full inventory into FullInventory.csv
with open('FullInventory.csv', 'w') as fullList:
    fullwrite = csv.writer(fullList)
    for x in range(0, len(full_inventory)):
        fullwrite.writerow(full_inventory[x])

#------------------ part b ------------------

# making an empty list for each item type
tower_list = []
laptop_list = []
phone_list = []
# making an if statement to find the item types and appending them to the empty lists
for x in range(0, len(final_list)):
    if final_list[x][2] == "tower":
        tower_list.append(final_list[x])
    elif final_list[x][2] == "phone":
        phone_list.append(final_list[x])
    else:
        laptop_list.append(final_list[x])
# sorting each list by ID (assumed least to greatest)
tower_list = (sorted(tower_list, key=itemgetter(0)))
laptop_list = (sorted(laptop_list, key=itemgetter(0)))
phone_list = (sorted(phone_list, key=itemgetter(0)))
# writing a file for each item type
with open('LaptopInventory.csv', 'w') as laptopList:
    laptop_write = csv.writer(laptopList)
    for x in range(0, len(laptop_list)):
        laptop_write.writerow(laptop_list[x])
with open('PhoneInventory.csv', 'w') as phoneList:
    phone_write = csv.writer(phoneList)
    for x in range(0, len(phone_list)):
        phone_write.writerow(phone_list[x])
with open('TowerInventory.csv', 'w') as towerList:
    tower_write = csv.writer(towerList)
    for x in range(0, len(tower_list)):
        tower_write.writerow(tower_list[x])

#------------------ part c ------------------

# used this function to get the present date and put the format to the same as the csv files
today = date.today().strftime('%d/%m/%Y')
# making an empty list for the dates
pastdate = []
# went through the service dates column to find if today's date is greater than it
for x in range(0, len(final_list)):
    if final_list[x][4] < today:
        pastdate.append(item_type[x])
# sorting the file by date
pastdate = (sorted(pastdate, key=itemgetter(-1), reverse=True))
# writing each past service date to PastServiceDateInventory.csv
with open('PastServiceDateInventory.csv', 'w') as date_List:
    pswrite = csv.writer(date_List)
    for x in range(0, len(pastdate)):
        pswrite.writerow(pastdate[x])

#------------------ part d ------------------

# made an empty list to hold all damaged items
damagedlist = []
# went through the damaged indicator column to find if it's damaged and appended it
for x in range(0, len(final_list)):
    if final_list[x][5] == "damaged":
        damagedlist.append(final_list[x])
# sorted the damaged list by most expensive to least
damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))
# writing a damaged products to DamagedInventory.csv
with open('DamagedInventory.csv', 'w') as damaged_List:
    diwrite = csv.writer(damaged_List)
    for x in range(0, len(damagedlist)):
        diwrite.writerow(damagedlist[x])