#INVENTORY FOR ITEMS/WEAPONS
inventory = []

def addToInventory(item):
    inventory.append(item)   

pickup = raw_input('>').strip().lower()

if pickup == "yes":
    addToInventory("flashlight")
else:
    print ("you can leave it")
print (inventory)

