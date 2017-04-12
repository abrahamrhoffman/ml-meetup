#!/usr/bin/python
# To run this file, try python a_great_suggestion.py

import random
from heapq import nsmallest

# Create our dataset - Part 1: List of users #
# Add as many names as you would like to this Python List #
hs0 = ['yournamehere']
hs = hs0

# Create our dataset - Part 2: #
# List some items - try adding your own! #
babyformula  = 'babyformula'
diaper       = 'diaper'
battery      = 'battery'
rccar        = 'rccar'

# Initialize our Dictionary #
# Don't forget to add the items you added above down here #
hsd = {}
for people in hs:
    hsd[people] = random.choice([babyformula, diaper, battery, rccar])

#def binary(num, length=4):
    #return format(num, '0{}b'.format(length))

### Create our dataset - Part 3: Add 'binary' features to items ##
baby           = 8  #binary(8)  #1000
newmom         = 4  #binary(4)  #0100
fun            = 2  #binary(2)  #0010
toys           = 1  #binary(1)  #0001
## Manually Add Features for Product Categories #
babyformula    = 12 #binary(12) #1100
diaper         = 12 #binary(12) #1100
battery        = 3  #binary(3)  #0011
rccar          = 3  #binary(3)  #0011

# Initialize our features with our products #
items      = {'babyformula': babyformula, 'diaper': diaper, 'battery': battery, 'rccar': rccar }
categories = {'baby': baby, 'newmom': newmom, 'fun': fun, 'toys': toys}

# This is our main function #
def a_great_suggestion():
    # Loop through each user one at a time #
    for k0, v0 in hsd.items():
        # Print the user's name and what we randomly had them purchase #
        print '%s purchased: %s' % (k0.title(), v0.title())
        # Create a new list of a single value: What the user purchased #
        purchase = [v0]
        # Loop through the "items" dictionary
        # Find the item that the customer purchased
        for k1, v1 in items.items():
            # Create a new list to store the user's item's value
            itemlist = []
            # Store the user's purchase value in the new list
            if v0 in (k1, v1):
                itemlist.append(v1)
            # Create a new list to store the user's item's category value
            nummatch = []
            # Search for the number that is closest to the item's category number
            for number in itemlist:
                thing = nsmallest(1, categories.values(), key=lambda x: abs(x-number))
                # Send this number to the list 'nummatch' that we created
                nummatch.append(thing[0])
            # Create a new list to hold the closest matching items in the category number we just retrieved
            matchitem = []
            # Search for the items that most closely match the item category we just searched for
            for number in nummatch:
                thing = nsmallest(1, items.values(), key=lambda x: abs(x-number))
                matchitem.append(thing[0])
            # Search the 'matchitem' list for item names based on the number in matchitem list
            for number in matchitem:
                # Append all the names to the purchase list that match the number we just stored in matchitem
                for k2, v2 in items.items():
                    if number in (k2, v2):
                        purchase.append(k2)
        # Remove any duplicates
        while v0 in purchase: purchase.remove(v0)
        # Print the values as strings in Uppercase first characters
        greatrec = ' '.join(purchase)
        # Print to STDOUT the item recommendation
        print 'We recommend: %s' % greatrec.title()
        print

# Standard Python Syntax #
if __name__ == '__main__':
    a_great_suggestion()
