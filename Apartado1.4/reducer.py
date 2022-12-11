#!/usr/bin/python

import sys

max_values = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total
    if thisKey not in max_values.keys():
        max_values[thisKey]=float(thisSale)
    else:
     max_values[thisKey] += float(thisSale)

# Escribe o ultimo par, unha vez rematado o bucle
for thisKey, thisSale in max_values.items():
    print(thisKey + "\t" + str(thisSale))
