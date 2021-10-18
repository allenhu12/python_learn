import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'arrow', 'arrow', 'arrow']
pp = pprint.PrettyPrinter(indent=4)

def addInventory(inventory, addedItem):
    for loot in addedItem:
        inventory.setdefault(loot,0)
        inventory[loot] = inventory[loot]+1

def displayInventory(inventory):
    print('Inventories:')
    for k, v in inventory.items():
        print('{0} {1}'.format(v, k))

if __name__ == '__main__':
    addInventory(stuff,dragonLoot)
    pp.pprint(stuff)
    displayInventory(stuff)