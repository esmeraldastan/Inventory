#INVENTORY FOR ITEMS
inventory = []
<<<<<<< HEAD
weight = 200
=======
print "there are coins in the fround. yes or no"
>>>>>>> origin/master

def addToInventory(item):
    inventory.append(item)   

pickup = raw_input('>').strip().lower()

if pickup == "yes":
    addToInventory("coin")
else:
    print ("okay ")
print (inventory)

#INVENTORY FOR WEAPONS

class player(object):
    
    def __init__(self, name, max_items, item):
        self.name = name
        self.max_items = max_items
        self.item = item
        
    def inventory(self):
        for item in self.items:
            print item
            
    def take(self, new_item):
        if len(self.items)<self.max_items:
            self.items.append(new_item)
        else: 
            print "You have reach a weight limit.\nYou can't carry anymore weapons"
            
    def leave(self, old_item):
        if old_item in self.items:
            self.items.remove(old_item)
        else:
            print "Not found."
        
            
        
