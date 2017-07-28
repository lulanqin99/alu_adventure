list1= ['a','b','c','e','f']
list2=[1, 2, 3, 4, 5]

if len(list1) < len(list2):   # len = length
    smaller = list1
    bigger = list2
else:
    smaller = list2
    bigger = list1
print smaller
print bigger

merged = []  # ranges go thru index
for i in range(0, len(smaller)):
    merged.append(smaller[i])
    merged.append(bigger[i])

# or or or or
##for i in range(len(smaller), len(bigger)):
##    merged.append(bigger[i])

# or or or
##for val in bigger[len(smaller):len(bigger)]:  #[] are sublist
##    merged.append(val)

# or or or

merged = merged + bigger[len(smaller):]
print smaller
print bigger
print merged
