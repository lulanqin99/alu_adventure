#keep track of current inventory
#update inventory
prices = {
    'butter': 1.50,
    'milk': 2.00,
    'bread': 3.00,
    'eggs': 7.00,
    'bacon': 7.00,
}

inventory = {

    'butter': 7,
    'milk': 7,
    'bread': 7,
    'eggs': 7,
    'bacon': 7,
}

shopping_list = raw_input('What is your shopping list? ').split(' ')

total = 0
for item in shopping_list:
    if item in prices and inventory[item] > 0:
    else:
        print "The item" + item + "is not available."
    total = total + prices[item]
    inventory[item] -= 1
print "Total is " + str(total)
