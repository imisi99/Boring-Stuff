def show_inventory(inventory):
    print('Inventory: ')
    item_total = 0
    for x, y in inventory.items():
        print(f'{y} {x}')
        item_total += y
    print(f'Total items: {item_total}')


def add_to_inventory(inventory, loot):
    for i in loot:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory


invent = {'rope': 21, 'saw': 3, 'nail': 20}
invent_list = ['rope', 'rope', 'sword', 'banger']
inv = add_to_inventory(invent, invent_list)
show_inventory(inv)
