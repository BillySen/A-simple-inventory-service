#An Simple Inventory Program by Billy Lei
#another thinking is to use sqlite to create a database and use SQL command to implement operation
import os
import re
clear = lambda: os.system('cls')

##########################################
# dictionary for storage
# Parameters Explaination:
# dict key-> The name of item
# dict value[0] -> the quantity of item
# dict value[1] -> the price of item
##########################################



#newAdd = input("Operation Entry:\n Input 1 for adding new item\n Input 2 for removing an item \n Input 3 for updating information about one item")
inventoryItems = {"apple":[52,2.36],"pear":[20,1.89]}
#item_counter = len(inventoryItems)

def main(inventoryItems):
    print("INVENTORY SERVICE")
    print("--------------------")
    print()
    print("Available Options:")
    print()
    print("1 - View Inventory")
    print("2 - Add Items To Inventory")
    print("3 - Remove Items from Inventory")
    print("4 - Update Info for Items")
    print()
    while True:
        uChoice = input("Choose An Option: ")
        if uChoice == '1':
            listAllItem(inventoryItems) 
            break
        elif uChoice == '2':
            addItem(inventoryItems)
            break
        elif uChoice == '3':
            removeItem(inventoryItems)
            break
        elif uChoice == '4':
            updateItem(inventoryItems)
            break

def addItem(inventoryItems):
    print()
    print("-------------------------------")
    print("ADD ITEM")
    print("-------------------------------")
    print()
    print("Options for Adding:")
    print()
    print("1 - Multiple items")
    print("2 - Single item")

    while True:
        userChoice = input("Choose an option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        print()
        while True:
            numItems = input("How many items do you want to add: ")
            if numItems.isdigit():
                break
        numItems = int(numItems)
        for i in range(1, numItems+1):
            while True:
                print()
                item_name = input("Item Name: ")
                if item_name != '':
                    break
            while True:
                item_quantity = input("Item Quantity: ")
                if item_quantity.isdigit():
                    pass
                item_price = input("Item Price: ")
                if is_float(item_price):
                    break
            inventoryItems.update({item_name: [int(item_quantity),round(float(item_price),2)]})
        returnToMainMenu(f"Items Have Been Added",inventoryItems)
    elif userChoice == '2':
        print()
        while True:
            item_name = input("Item Name: ")
            if item_name != '':
                break
        while True:
            item_quantity = input("Item Quantity: ")
            if item_quantity.isdigit():
                pass
            item_price = input("Item Price: ")
            if is_float(item_price):
                break
        inventoryItems.update({item_name: [int(item_quantity),round(float(item_price),2)]})
        returnToMainMenu(f"Item {item_name} Has Been Added",inventoryItems)


def removeItem(inventoryItems):
    print()
    print("-------------------------------")
    print("REMOVE ITEM")
    print("-------------------------------")
    print()
    while True:
        itemToDelete = input("Enter The Name Of The Item To Delete: ")
        if itemToDelete in inventoryItems:
            break
        else:
            print("That Item Does Not Exist")
            print()

    while True:
       confirmation = input("CONFIRMATION: Are You Sure You Want To Delete This Item: ").lower()
       if confirmation in ['yes', 'no']:
           break
    if confirmation == 'yes':
        del inventoryItems[itemToDelete]
        returnToMainMenu(f"Item {itemToDelete} Has Been Deleted",inventoryItems)
    else:
        main(inventoryItems)



    

def updateItem(inventoryItems):
    print()
    print("-------------------------------")
    print("UPDATE INFO OF ITEM")
    print("-------------------------------")
    print() 
    print("Press (B) To Go Back")
    print()
    print("Options")
    print()
    print("1 - Edit Item Name")
    print("2 - Edit Item Quantity")
    print("3 - Edit Item Price")
    print()
    while True:
        userChoice = input("Choose An Option: ").lower()
        if userChoice in ['1', '2','3','b']:
            break
    if userChoice == 'b':
        main(inventoryItems)

    if userChoice == '1':
        print()
        while True:
            itemToUpdate = input("Enter The Name Of The Item To Edit: ")
            if itemToUpdate in inventoryItems:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newItemName = input("Enter The New Item Name to Replace: ")
            if newItemName != '':
                break
        inventoryItems.update({newItemName: inventoryItems[itemToChange]})
        del inventoryItems[itemToChange]
        returnToMainMenu(f"Item {itemToUpdate} Name Has Been Changed to {newItemName}",inventoryItems)

    elif userChoice == '2':
        print()
        while True:
            itemToChange = input("Enter The Name Of The Item To Edit: ")
            if itemToChange in inventoryItems:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newQuantity = input("Enter The New Item Amount: ")
            if newQuantity != '' and newQuantity.isdigit():
                break
        inventoryItems[itemToChange][0] = newQuantity
        returnToMainMenu(f"Item {itemToChange}'s Quantity Has Been Changed",inventoryItems)
    elif userChoice == '3':
        print()
        while True:
            itemToChange = input("Enter The Name Of The Item To Edit: ")
            if itemToChange in inventoryItems:
                break
            else:
                print("That Item Does Not Exist")
                print()

        while True:
            newPrice = input("Enter The New Item Amount: ")
            if newPrice != '' and is_float(newPrice):
                break
        inventoryItems[itemToChange][1] = newPrice
        returnToMainMenu(f"Item {itemToChange}'s Price Has Been Changed",inventoryItems)

def listAllItem(inventoryItems):
    print()
    print("-------------------------------")
    print("LIST ITEM")
    print("-------------------------------")
    i = 1
    for key,value in inventoryItems.items():
        print(f"Item {i}: [{key}]  Quantity: {value[0]}  Price: {value[1]}")
        i+=1
    print()
    returnToMainMenu("",inventoryItems)
    


def is_float(numStr):
    flag = False
    numStr = str(numStr).strip().lstrip('-').lstrip('+')    # get rid of "+" "-" sign
    try:
        reg = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
        res = reg.match(str(numStr))
        if res:
            flag = True
    except Exception as ex:
        print("is_float() - error: " + str(ex))
    return flag

def returnToMainMenu(message,inventoryItems):
    while True:
        print()
        back = input(f"{message}. Press (M) To Return To Main Menu: ").lower() if message != None else input("Press (M) To Return To Main Menu: ").lower()
        if back == 'm':
            main(inventoryItems)
            break

if __name__ == '__main__':
    main(inventoryItems)