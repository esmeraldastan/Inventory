class Inventory(object):
    def __init__(self):
        self.items = {}
        
    def add_items(self, item):
        self.items[item.name] = item
        
    def print_items(self):
        print "Name: \nAttack:"